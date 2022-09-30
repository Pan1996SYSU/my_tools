import os.path
import re
import traceback
from glob import glob
from multiprocessing.dummy import Pool as ThreadPool
from pathlib import Path

from sonic.utils_func import extensions

num_thread = 8

input_2d_path = r"D:\桌面\pth"
input_3d_lum_path = r"D:\桌面\20220920-113904_mfd_markhole_img\NG"
input_h_lum_path = r"D:\桌面\img"


def match_path_dict(
        img_path_list_2d, json_path_list_lum, img_path_list_lum,
        img_path_list_h):
    path_dict = {}

    for x in img_path_list_2d:
        key = re.findall(r'[-_]([A-Z0-9]{24})[-_]', str(x))
        if len(key) != 1:
            continue
        key = key[0]

        if key not in path_dict:
            path_dict[key] = {}

        path_dict[key]['img1'] = str(x)

    for x in json_path_list_lum:
        key = re.findall(r'[-_]([A-Z0-9]{24})[-_]', str(x))
        if len(key) != 1:
            continue
        key = key[0]

        if key not in path_dict:
            path_dict[key] = {}

        path_dict[key]['json'] = str(x)

    for x in img_path_list_lum:
        key = re.findall(r'[-_]([A-Z0-9]{24})[-_]', str(x))
        if len(key) != 1:
            continue
        key = key[0]

        if key not in path_dict:
            path_dict[key] = {}

        path_dict[key]['img2_Lum'] = str(x)

    for x in img_path_list_h:
        key = re.findall(r'[-_]([A-Z0-9]{24})[-_]', str(x))
        if len(key) != 1:
            continue
        key = key[0]

        if key not in path_dict:
            path_dict[key] = {}

        path_dict[key]['img2_H'] = str(x)

    return path_dict


def mfd_transformation(tasks):
    stem_prefix = tasks.get('stem_prefix', None)
    x = path_dict[stem_prefix]
    json_path = x.get('json', None)
    img_path_2d = x.get('img1', None)
    img_path_lum = x.get('img2_Lum', None)
    img_path_h = x.get('img2_H', None)
    if img_path_2d and img_path_lum and img_path_h and json_path:
        from sonic.utils_func import cv_img_read, load_json
        img_2d = cv_img_read(img_path_2d)
        json_lum = load_json(json_path)
        img_lum = cv_img_read(img_path_lum)
        img_h = cv_img_read(img_path_h)

        score_list = []

        if not json_lum:
            return

        for r in json_lum["result"]:
            score_list.append(r['score'])

        max_index = score_list.index(max(score_list))

        try:
            bbox = json_lum["result"][max_index]["bbox"]
            category_name = json_lum["result"][max_index]["category_name"]
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            bbox = None
            category_name = None
        if bbox is not None and category_name is not None:
            x, y, w, h = bbox
            x = int(x + w / 2)
            y = int(y + h / 2)
            x += 200
            y += 200
            if category_name == '漏钉mark孔':
                import cv2
                y0_2d_scale = 150 / 2020
                x0_2d_scale = 450 / 2014
                y1_2d_scale = 1570 / 2020
                x1_2d_scale = 1870 / 2014
                lum_radius = 900

                img_2d = cv2.copyMakeBorder(
                    img_2d, 0, 200, 0, 200, cv2.BORDER_REPLICATE)
                h_2d, w_2d = img_2d.shape[:2]

                y0 = int(y0_2d_scale * h_2d)
                x0 = int(x0_2d_scale * w_2d)
                y1 = int(y1_2d_scale * h_2d)
                x1 = int(x1_2d_scale * w_2d)

                img_2d = cv2.copyMakeBorder(
                    img_2d, 0, 200, 0, 200, cv2.BORDER_REPLICATE)

                img_lum_mb = cv2.copyMakeBorder(
                    img_lum, 200, 200, 200, 200, cv2.BORDER_REPLICATE)
                img_h_mb = cv2.copyMakeBorder(
                    img_h, 200, 200, 200, 200, cv2.BORDER_REPLICATE)

                img_lum_res = img_lum_mb[y - lum_radius:y + lum_radius,
                                         x - lum_radius:x + lum_radius].copy()
                img_h_res = img_h_mb[y - lum_radius:y + lum_radius,
                                     x - lum_radius:x + lum_radius].copy()
                img_2d_res = img_2d[y0:y1, x0:x1]

                h_res, w_res = img_lum_res.shape[:2]
                img_2d_res = cv2.resize(img_2d_res, (w_res, h_res))

                img_h_res = cv2.blur(img_h_res, (3, 20))

                if not os.path.exists("D:/桌面/xwd"):
                    os.makedirs("D:/桌面/xwd")
                cv2.imencode('.tiff', img_lum_res)[1].tofile(
                    fr"D:/桌面/xwd/{stem_prefix}_Lum.tiff")
                cv2.imencode(
                    '.tiff',
                    img_h_res)[1].tofile(fr"D:/桌面/xwd/{stem_prefix}_H.tiff")
                cv2.imencode(
                    '.tiff',
                    img_2d_res)[1].tofile(fr"D:/桌面/xwd/{stem_prefix}_2D.tiff")
            elif category_name == 'mark孔':
                h_2d, w_2d = img_2d.shape[:2]
                import cv2
                y0_2d_scale = 150 / 1812
                x0_2d_scale = 185 / 1840
                y1_2d_scale = 1670 / 1812
                x1_2d_scale = 1700 / 1840
                lum_radius = 960

                y0 = int(y0_2d_scale * h_2d)
                x0 = int(x0_2d_scale * w_2d)
                y1 = int(y1_2d_scale * h_2d)
                x1 = int(x1_2d_scale * w_2d)

                img_lum_mb = cv2.copyMakeBorder(
                    img_lum, 200, 200, 200, 200, cv2.BORDER_REPLICATE)
                img_h_mb = cv2.copyMakeBorder(
                    img_h, 200, 200, 200, 200, cv2.BORDER_REPLICATE)

                img_lum_res = img_lum_mb[y - lum_radius:y + lum_radius,
                                         x - lum_radius:x + lum_radius].copy()
                img_h_res = img_h_mb[y - lum_radius:y + lum_radius,
                                     x - lum_radius:x + lum_radius].copy()
                img_2d_res = img_2d[y0:y1, x0:x1]

                h_res, w_res = img_lum_res.shape[:2]
                img_2d_res = cv2.resize(img_2d_res, (w_res, h_res))

                img_h_res = cv2.blur(img_h_res, (3, 20))

                if not os.path.exists("D:/桌面/xwd"):
                    os.makedirs("D:/桌面/xwd")
                cv2.imencode('.tiff', img_lum_res)[1].tofile(
                    fr"D:/桌面/xwd/{stem_prefix}_Lum.tiff")
                cv2.imencode(
                    '.tiff',
                    img_h_res)[1].tofile(fr"D:/桌面/xwd/{stem_prefix}_H.tiff")
                cv2.imencode(
                    '.tiff',
                    img_2d_res)[1].tofile(fr"D:/桌面/xwd/{stem_prefix}_2D.tiff")


path_list_t = glob(f'{input_2d_path}/**/*', recursive=True)
path_list_2d = [Path(x) for x in path_list_t]

img_path_list_2d = [x for x in path_list_2d if x.suffix in extensions]

path_list_t = glob(f'{input_3d_lum_path}/**/*', recursive=True)
path_list_3d = [Path(x) for x in path_list_t]

json_path_list_lum = [x for x in path_list_3d if x.suffix == '.json']
img_path_list_lum = [x for x in path_list_3d if x.suffix in extensions]

path_list_t = glob(f'{input_h_lum_path}/**/*', recursive=True)
path_list_3d = [Path(x) for x in path_list_t]

img_path_list_h = [x for x in path_list_3d if x.suffix in extensions]
img_path_list_h = [
    x for x in img_path_list_h
    if x.stem.endswith('H') or x.parent.name.endswith('H')
]

path_dict = match_path_dict(
    img_path_list_2d, json_path_list_lum, img_path_list_lum, img_path_list_h)

with ThreadPool(processes=num_thread) as pool:
    tasks = [{
        'stem_prefix': stem_prefix,
    } for stem_prefix in path_dict]
    n = len(tasks)
    for i, result in enumerate(pool.imap_unordered(mfd_transformation, tasks)):
        if i % 10 == 0:
            print(i / n * 100)
