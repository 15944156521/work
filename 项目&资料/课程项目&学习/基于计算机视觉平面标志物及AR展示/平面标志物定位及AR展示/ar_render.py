import cv2
import numpy as np
from pose_estimation import estimate_pose

def fill_convex_poly_alpha(img, pts, color, alpha):
    """在img上以alpha混合方式填充多边形"""
    overlay = img.copy()
    cv2.fillConvexPoly(overlay, pts, color)
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

def draw_axes(img, rvec, tvec, mtx, dist, axis_len=3.0):
    axis_pts = np.float32([
        [0,0,0],           # 原点
        [axis_len,0,0],    # X轴端点
        [0,axis_len,0],    # Y轴端点
        [0,0,-axis_len],   # Z轴端点（注意Z轴向外为负）
    ])
    imgpts_axis, _ = cv2.projectPoints(axis_pts, rvec, tvec, mtx, dist)
    imgpts_axis = imgpts_axis.reshape(-1,2).astype(int)
    # X轴-红，Y轴-绿，Z轴-蓝
    cv2.line(img, tuple(imgpts_axis[0]), tuple(imgpts_axis[1]), (0,0,255), 4)
    cv2.line(img, tuple(imgpts_axis[0]), tuple(imgpts_axis[2]), (0,255,0), 4)
    cv2.line(img, tuple(imgpts_axis[0]), tuple(imgpts_axis[3]), (255,0,0), 4)

def draw_cube(img, rvec, tvec, mtx, dist, size=2.0, center_offset=None):
    # 立方体8个顶点
    cube = np.float32([
        [0,0,0], [0,0,-size], [0,size,0], [0,size,-size],
        [size,0,0], [size,0,-size], [size,size,0], [size,size,-size]
    ])
    if center_offset is not None:
        cube += center_offset
    imgpts, _ = cv2.projectPoints(cube, rvec, tvec, mtx, dist)
    imgpts = imgpts.reshape(-1,2).astype(int)
    faces = [
        [0,1,3,2], [4,5,7,6], [0,1,5,4],
        [2,3,7,6], [0,2,6,4], [1,3,7,5]
    ]
    # 找到最靠近棋盘格的面（z均值最小的面）
    R, _ = cv2.Rodrigues(rvec)
    verts_cam = (R @ cube.T).T + tvec.reshape(1,3)
    min_z = float('inf')
    min_face_idx = -1
    for idx, face in enumerate(faces):
        z_mean = np.mean(verts_cam[face,2])
        if z_mean < min_z:
            min_z = z_mean
            min_face_idx = idx
    # 主色调
    base_color = np.array([120, 80, 40], dtype=np.float32)
    highlight_color = np.array([255, 255, 220], dtype=np.float32)
    super_highlight = np.array([255, 255, 255], dtype=np.float32)
    alpha = 0.5
    highlight_alpha = 0.8  # 底面更突出
    camera_dir = np.array([0, 0, -1.0])
    camera_dir = R.T @ camera_dir
    for idx, face in enumerate(faces):
        v0, v1, v2 = cube[face[0]], cube[face[1]], cube[face[2]]
        normal = np.cross(v1 - v0, v2 - v0)
        normal = normal / np.linalg.norm(normal)
        brightness = np.dot(normal, camera_dir)
        brightness = np.clip(brightness, 0, 1)
        if idx == min_face_idx:
            color = super_highlight * 0.7 + highlight_color * 0.3
            fill_convex_poly_alpha(img, imgpts[face], color.tolist(), highlight_alpha)
        else:
            color = base_color * (0.5 + 0.5*brightness) + highlight_color * (0.2 * brightness)
            fill_convex_poly_alpha(img, imgpts[face], color.tolist(), alpha)
    draw_axes(img, rvec, tvec, mtx, dist)
    return img

def draw_icosahedron(img, rvec, tvec, mtx, dist, size=2.0, chessboard_size=(9,6), mesh_path=None, render_type='icosahedron'):
    if render_type == 'cube':
        # 渲染立方体
        center_offset = np.array([
            (chessboard_size[0]-1)/2.0,
            (chessboard_size[1]-1)/2.0,
            0
        ], dtype=np.float32)
        return draw_cube(img, rvec, tvec, mtx, dist, size=size, center_offset=center_offset)

    # 20面体顶点
    phi = (1 + 5 ** 0.5) / 2
    verts = np.array([
        [-1,  phi, 0], [1,  phi, 0], [-1, -phi, 0], [1, -phi, 0],
        [0, -1,  phi], [0, 1,  phi], [0, -1, -phi], [0, 1, -phi],
        [ phi, 0, -1], [ phi, 0, 1], [-phi, 0, -1], [-phi, 0, 1]
    ], dtype=np.float32)
    verts *= size / np.linalg.norm(verts[0])  # 缩放
    # 计算棋盘格中心（以内角点为单位，原点在左上角）
    center_offset = np.array([
        (chessboard_size[0]-1)/2.0,
        (chessboard_size[1]-1)/2.0,
        0
    ], dtype=np.float32)
    verts = verts + center_offset  # 平移到棋盘格中心

    # 20面体面
    faces = [
        [0,11,5],[0,5,1],[0,1,7],[0,7,10],[0,10,11],
        [1,5,9],[5,11,4],[11,10,2],[10,7,6],[7,1,8],
        [3,9,4],[3,4,2],[3,2,6],[3,6,8],[3,8,9],
        [4,9,5],[2,4,11],[6,2,10],[8,6,7],[9,8,1]
    ]

    imgpts, _ = cv2.projectPoints(verts, rvec, tvec, mtx, dist)
    imgpts = imgpts.reshape(-1,2).astype(int)

    # 计算相机方向（z轴负方向）
    R, _ = cv2.Rodrigues(rvec)
    camera_dir = np.array([0, 0, -1.0])
    camera_dir = R.T @ camera_dir  # 转到世界坐标系

    # 找到最靠近棋盘格平面的面（z均值最小的面）
    verts_cam = (R @ verts.T).T + tvec.reshape(1,3)
    min_z = float('inf')
    min_face_idx = -1
    for idx, face in enumerate(faces):
        z_mean = np.mean(verts_cam[face,2])
        if z_mean < min_z:
            min_z = z_mean
            min_face_idx = idx

    # 主色调（深蓝色，BGR）
    base_color = np.array([120, 80, 40], dtype=np.float32)
    # 高光色（亮蓝色，BGR）
    highlight_color = np.array([255, 255, 220], dtype=np.float32)
    # 更亮的突出色
    super_highlight = np.array([255, 255, 255], dtype=np.float32)

    alpha = 0.5  # 所有面透明度
    highlight_alpha = 0.7  # 底面更突出

    # 伪光照：每个面根据法线与相机夹角调整亮度
    for idx, face in enumerate(faces):
        v0, v1, v2 = verts[face]
        normal = np.cross(v1 - v0, v2 - v0)
        normal = normal / np.linalg.norm(normal)
        brightness = np.dot(normal, camera_dir)
        brightness = np.clip(brightness, 0, 1)
        if idx == min_face_idx:
            color = super_highlight * 0.7 + highlight_color * 0.3
            fill_convex_poly_alpha(img, imgpts[face], color.tolist(), highlight_alpha)
        else:
            color = base_color * (0.5 + 0.5*brightness) + highlight_color * (0.2 * brightness)
            fill_convex_poly_alpha(img, imgpts[face], color.tolist(), alpha)

    draw_axes(img, rvec, tvec, mtx, dist)
    return img

def ar_on_image(img_path, param_path='camera_params.npz', render_type='icosahedron', mesh_path=None, shift_x=0, shift_y=0):
    img = cv2.imread(img_path)
    if img is None:
        print(f"无法读取图片: {img_path}")
        # 输出“无法读取图片: test.jpg”说明你的 test.jpg 文件不存在于当前目录（c:\Users\86159\Desktop\big work），或者文件名拼写有误，或者图片损坏无法读取。
        # 解决方法：
        # 1. 确认 test.jpg 文件确实存在于 c:\Users\86159\Desktop\big work 目录下。
        # 2. 检查文件名是否完全一致（包括大小写和扩展名）。
        # 3. 如果图片在其它目录，请提供正确的路径给 ar_on_image 函数。
        # 4. 你也可以用 web_server.py 上传图片，系统会自动处理并显示结果。
        return None, None, None
    params = np.load(param_path)
    mtx, dist = params['mtx'], params['dist']
    print("开始姿态估计...")
    chessboard_size = (9,6)
    rvec, tvec, corners = estimate_pose(img, chessboard_size=chessboard_size, param_path=param_path)
    if rvec is not None:
        # 新增：平移
        tvec = tvec.copy()
        tvec[0][0] += shift_x
        tvec[1][0] += shift_y
        img = draw_icosahedron(img, rvec, tvec, mtx, dist, size=2.0, chessboard_size=chessboard_size, mesh_path=mesh_path, render_type=render_type)
        return img, rvec, tvec
    else:
        return None, None, None

if __name__ == '__main__':
    img = ar_on_image('test.jpg')
    if img is not None:
        cv2.imwrite('ar_result.jpg', img)
    else:
        print("未生成输出图片。")
# 你的输出显示：
# - findChessboardCorners: ret=True
# - 检测到角点数量: 54
# - 棋盘格参数为(9,6)，即9列6行内角点
# - 检测到棋盘格，渲染二十面体
# 这说明棋盘格检测和姿态估计都已成功，二十面体已渲染在图片上。
# 你可以在当前目录下找到 ar_result.jpg，打开即可看到带有二十面体的AR效果图。
# 如果需要批量处理或网页展示，直接用 web_server.py 上传图片即可。
