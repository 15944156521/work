import cv2
import numpy as np

def estimate_pose(img, chessboard_size=(9,6), square_size=1.0, param_path='camera_params.npz'):
    print(f"estimate_pose: chessboard_size={chessboard_size}, square_size={square_size}")
    params = np.load(param_path)
    mtx, dist = params['mtx'], params['dist']
    objp = np.zeros((chessboard_size[0]*chessboard_size[1],3), np.float32)
    objp[:,:2] = np.mgrid[0:chessboard_size[0],0:chessboard_size[1]].T.reshape(-1,2)
    objp *= square_size

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, chessboard_size, None)
    print(f"findChessboardCorners: ret={ret}")
    if ret:
        print(f"检测到角点数量: {len(corners)}")
        # 可视化检测结果，调试用
        vis = img.copy()
        cv2.drawChessboardCorners(vis, chessboard_size, corners, ret)
        cv2.imwrite('debug_chessboard_detect.jpg', vis)
    else:
        print("未检测到角点，请检查棋盘格参数和图片内容。")
        # 可选：保存灰度图调试
        cv2.imwrite('debug_gray.jpg', gray)
        return None, None, None
    ret, rvec, tvec = cv2.solvePnP(objp, corners, mtx, dist)
    return rvec, tvec, corners

# 用法示例
if __name__ == '__main__':
    img = cv2.imread('test.jpg')
    rvec, tvec, corners = estimate_pose(img)
    print("rvec:", rvec, "tvec:", tvec)
