import os
import traceback
from collections import defaultdict
from multiprocessing.dummy import Pool as ThreadPool
from pathlib import Path

import cv2
import halcon as ha
from sonic.utils_func import cv_img_read, load_json, save_json, make_dirs

input_path = r'D:\桌面\未裁图'
output_path = r'D:\桌面\img'
thread_num = 16

extensions = [
    '.bmp', '.gif', '.jpeg', '.jpg', '.pbm', '.png', '.tif', '.tiff', '.json'
]

padding = 100


def get_files_from_dir(path):
    if not os.path.exists(path):
        return ''

    file_path_dict = defaultdict(list)
    for root, directories, files in os.walk(path):
        for filename in files:
            s = Path(filename).suffix
            filename = str(filename)
            if s in extensions:
                if 'C01_P01' in filename:
                    name_key = str(filename).split('_C01_P01')[0]
                    filepath = os.path.join(root, filename)
                    file_path_dict[name_key].append(filepath)
                else:
                    print('文件名不存在‘C01_P01’')
                    print(filename)
    return file_path_dict


def cut_json(json_data, x1, x2):
    import numpy as np
    try:
        w = int(x2 - x1)
        json_data["imageWidth"] = w
        for k, shape in enumerate(json_data["shapes"]):
            points = np.array(shape['points'])
            points[:, 0] = points[:, 0] - x1
            points[points[:, 0] >= w, 0] = w - 3
            points[points[:, 0] <= 0, 0] = 3
            json_data["shapes"][k]['points'] = points.tolist()
    except Exception as e:
        print(e)
        print(traceback.format_exc())
    return json_data


def crop_img(task):
    try:
        file_key = task.get('file_list', None)
        if file_key is None:
            return
        file_list = file_dict[file_key]
        file_len = len(file_list)
        if file_len != 4:
            return
        img_list = file_list
        base_img_path = img_list[2]
        Image = ha.read_image(base_img_path)
        Regions = ha.threshold(Image, 149, 255)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(
            ConnectedRegions, 'area', 'and', 8000000, 16000000)
        y1, x1, y2, x2 = ha.smallest_rectangle1(SelectedRegions)
        if len(y1) != 1:
            print('阈值分割失败，将使用默认坐标')
            print(img_list)
            x1 = [1760]
            x2 = [6200]
        for img_path in img_list:
            try:
                img = cv_img_read(img_path)
                h, w = img.shape[:2]
                res_img = img[
                    0:h,
                    max(0, int(x1[0] - padding)):min(w, int(x2[0] +
                                                            padding))].copy()
                output_img_path = Path(
                    output_path,
                    Path(img_path).relative_to(Path(input_path)))
                suffix = Path(img_path).suffix
                output_parent = Path(output_img_path).parent
                make_dirs(output_parent)
                cv2.imencode(suffix, res_img)[1].tofile(output_img_path)
            except Exception as e:
                print(e)
                print(traceback.format_exc())
                print(img_path)
        # if json_list:
        #     json_data = load_json(json_list)
        #     json_res_data = cut_json(
        #         json_data, x1[0] - padding, x2[0] + padding)
        #     output_json_path = Path(
        #         output_path,
        #         Path(json_list).relative_to(Path(input_path)))
        #     output_parent = Path(output_json_path).parent
        #     make_dirs(output_parent)
        #     save_json(output_json_path, json_res_data)
    except Exception as e:
        print(e)
        print(traceback.format_exc())


if __name__ == '__main__':
    file_dict = get_files_from_dir(input_path)
    num = len(file_dict)
    n = max(1, num // 100)
    with ThreadPool(processes=thread_num) as pool:
        tasks = [{
            'file_list': file_list,
        } for file_list in file_dict]
        for i, result in enumerate(pool.imap_unordered(crop_img, tasks)):
            if i % n == 0:
                print(i / num * 100)
