from flask import Flask, request, render_template, send_file, jsonify, session
import os
from ar_render import ar_on_image
import numpy as np

app = Flask(__name__)
app.secret_key = 'ar_secret_key'  # 用于session

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        files = request.files.getlist('file')
        render_type = request.form.get('render_type', 'icosahedron')
        mesh_path = request.form.get('mesh_path', None)
        result_files = []
        for f in files:
            img_path = os.path.join(UPLOAD_FOLDER, f.filename)
            f.save(img_path)
            base_name, ext = os.path.splitext(f.filename)
            shifts = {
                'center': (0, 0),
                'up': (0, -1),
                'down': (0, 1),
                'left': (-1, 0),
                'right': (1, 0)
            }
            for key, (shift_x, shift_y) in shifts.items():
                result_img, rvec, tvec = ar_on_image(
                    img_path, render_type=render_type, mesh_path=mesh_path,
                    shift_x=shift_x, shift_y=shift_y
                )
                result_fname = f"{base_name}_{key}{ext}"
                result_path = os.path.join(RESULT_FOLDER, result_fname)
                import cv2
                cv2.imwrite(result_path, result_img)
                save_pose(result_fname, rvec, tvec)
            # 只把center图加入主展示列表
            result_files.append(f"{base_name}_center{ext}")
        return render_template('result.html', img_files=result_files)
    # 展示历史渲染结果
    result_files = []
    for fname in os.listdir(RESULT_FOLDER):
        if fname.lower().endswith('_center.jpg') or fname.lower().endswith('_center.jpeg') or fname.lower().endswith('_center.png'):
            result_files.append(fname)
    result_files.sort()
    return render_template('index.html', img_files=result_files)

@app.route('/results/<filename>')
def result_img(filename):
    return send_file(os.path.join(RESULT_FOLDER, filename), mimetype='image/jpeg')

@app.route('/pose/<filename>')
def get_pose(filename):
    pose_path = os.path.join(RESULT_FOLDER, filename + '.npz')
    if not os.path.exists(pose_path):
        return jsonify({'error': 'No pose data'}), 404
    data = np.load(pose_path)
    rvec = data['rvec'].tolist()
    tvec = data['tvec'].tolist()
    return jsonify({'rvec': rvec, 'tvec': tvec})

@app.route('/all_results')
def all_results():
    # 展示results目录下所有图片（20-30张）
    result_files = []
    for fname in os.listdir(RESULT_FOLDER):
        if fname.lower().endswith(('.jpg', '.jpeg', '.png')):
            result_files.append(fname)
    result_files.sort()
    return render_template('all_results.html', img_files=result_files)

# 在保存渲染结果时也保存rvec/tvec
def save_pose(filename, rvec, tvec):
    pose_path = os.path.join(RESULT_FOLDER, filename + '.npz')
    np.savez(pose_path, rvec=rvec, tvec=tvec)

if __name__ == '__main__':
    app.run(debug=True)