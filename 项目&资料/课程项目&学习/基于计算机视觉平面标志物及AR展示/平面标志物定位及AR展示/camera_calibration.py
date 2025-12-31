import cv2
import numpy as np
import glob

def calibrate_camera(chessboard_size=(9, 6), square_size=1.0, img_dir='calib_imgs/*.jpg', save_path='camera_params.npz'):
    objp = np.zeros((chessboard_size[0]*chessboard_size[1],3), np.float32)
    objp[:,:2] = np.mgrid[0:chessboard_size[0],0:chessboard_size[1]].T.reshape(-1,2)
    objp *= square_size

    objpoints = []
    imgpoints = []

    images = glob.glob(img_dir)
    print(f"找到图片数量: {len(images)}")
    for fname in images:
        img = cv2.imread(fname)
        if img is None:
            print(f"无法读取图片: {fname}")
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)
        if ret:
            objpoints.append(objp)
            imgpoints.append(corners)
            print(f"检测到角点: {fname}")
        else:
            print(f"未检测到角点: {fname}")
    if len(objpoints) == 0:
        print("没有任何图片检测到角点，请检查棋盘格尺寸参数和图片内容！")
        return
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    np.savez(save_path, mtx=mtx, dist=dist)
    print("Calibration done. Params saved to", save_path)

if __name__ == '__main__':
    # 正确的参数应为(10, 7)表示10列7行内角点（即7行10列内角点）
    calibrate_camera(chessboard_size=(9, 6))
