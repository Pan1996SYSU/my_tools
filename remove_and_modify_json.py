import os
import shutil
import traceback
from glob import glob
from multiprocessing.pool import ThreadPool
from pathlib import Path

from sonic.utils_func import make_dirs, save_json, load_json

buffer_size = 102400
thread_num = 16
input_path = r'Z:\5-标注数据\CYS.220301-密封钉检测\3D旋转'
output_path = r'C:\Users\cys01\Desktop\img'

json_path_list = glob(f'{input_path}/**/*.json', recursive=True)

json_output_path_list = []


def remove_file(task):
    json_path = task.get('json_path')

    json_output_path = Path(
        output_path,
        Path(json_path).relative_to(Path(input_path)))
    make_dirs(Path(json_output_path).parent)

    json_output_path_list.append(json_output_path)

    json_name = os.path.basename(json_path).split('.')[0]

    img_2d_path = f'{Path(json_path).parent}/{json_name}_2D.tiff'
    img_2d_output_path = Path(
        output_path,
        Path(img_2d_path).relative_to(Path(input_path)))

    img_h_path = f'{Path(json_path).parent}/{json_name}_H.tiff'
    img_h_output_path = Path(
        output_path,
        Path(img_h_path).relative_to(Path(input_path)))

    img_lum_path = f'{Path(json_path).parent}/{json_name}_Lum.tiff'
    img_lum_output_path = Path(
        output_path,
        Path(img_lum_path).relative_to(Path(input_path)))

    with open(json_path, 'rb') as f_in:
        with open(json_output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out, buffer_size * 1024)
    try:
        with open(img_2d_path, 'rb') as f_in:
            with open(img_2d_output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out, buffer_size * 1024)
    except Exception as e:
        print(e)
        traceback.print_exc()

    try:
        with open(img_h_path, 'rb') as f_in:
            with open(img_h_output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out, buffer_size * 1024)
    except Exception as e:
        print(e)
        traceback.print_exc()

    try:
        with open(img_lum_path, 'rb') as f_in:
            with open(img_lum_output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out, buffer_size * 1024)
    except Exception as e:
        print(e)
        traceback.print_exc()


def modify_json(task):
    json_output_path = task.get('json_output_path')
    data = load_json(json_output_path)
    image_path_list = []
    json_name = os.path.basename(json_output_path).split('.')[0]
    img_2d_name = f'{json_name}_2D.tiff'
    image_path_list.append(img_2d_name)
    img_h_name = f'{json_name}_H.tiff'
    image_path_list.append(img_h_name)
    img_lum_name = f'{json_name}_Lum.tiff'
    image_path_list.append(img_lum_name)

    data["image_path_list"] = image_path_list
    data["channels"] = int(3)
    data["imagePath"] = img_2d_name

    save_json(json_output_path, data)


if __name__ == '__main__':
    with ThreadPool(processes=thread_num) as pool:
        tasks = [{
            'json_path': json_path,
        } for json_path in json_path_list]
        for i, result in enumerate(pool.imap_unordered(remove_file, tasks)):
            pass

    with ThreadPool(processes=thread_num) as pool:
        tasks = [
            {
                'json_output_path': json_output_path,
            } for json_output_path in json_output_path_list
        ]
        for i, result in enumerate(pool.imap_unordered(modify_json, tasks)):
            pass
