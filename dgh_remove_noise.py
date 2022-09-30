import time
from multiprocessing.dummy import Pool as ThreadPool
from pathlib import Path

import cv2
import halcon as ha
import numpy as np
from sonic.utils_func import cv_img_read, glob_extensions, make_dirs

thread_num = 16

input_path = r'D:\桌面\顶盖焊预处理'
output_path = r'D:\桌面\img'

img_path_list = glob_extensions(input_path)


def pre_process(task):
    img_path = task.get('img_path', None)
    if img_path is None:
        return
    if Path(img_path).name.split('.')[0][-1] == 'G':
        img = ha.read_image(img_path)

        start_time1 = time.time()
        Regions = ha.threshold(img, 68, 255)
        RegionClosing = ha.closing_rectangle1(Regions, 15, 55)
        RegionOpening = ha.opening_rectangle1(RegionClosing, 5, 5)
        ConnectedRegions = ha.connection(RegionOpening)
        SelectedRegions = ha.select_shape(
            ConnectedRegions, 'area', 'and', 300000, 400000)
        if len(SelectedRegions) != 1:
            return
        y, x = ha.get_region_contour(SelectedRegions)
        points = np.column_stack((x, y))
        end_time1 = time.time()

        image = cv_img_read(img_path)

        start_time2 = time.time()
        h, w = image.shape[:2]
        img = np.zeros((h, w), dtype=np.uint8)
        cv2.fillPoly(img, [points.astype(int)], 255)
        end_time2 = time.time()

        img_h_path_name = Path(img_path).name.split('.')[0][:-1]
        img_h_path = f'{Path(img_path).parent}/{img_h_path_name}H{Path(img_path).suffix}'

        img_h = cv_img_read(img_h_path)

        start_time3 = time.time()
        img_h[img == 0] = 0
        img_h = cv2.medianBlur(img_h, 5)
        # h1_img = cv2.Sobel(img_h, cv2.CV_64F, 0, 1, ksize=21)
        # h2_img = cv2.Sobel(img_h, cv2.CV_64F, 0, 2, ksize=21)
        # plt.subplot(1, 2, 1), plt.imshow(h1_img, cmap='gray')
        # plt.title('Sobel Y1'), plt.xticks([]), plt.yticks([])
        # plt.subplot(1, 2, 2), plt.imshow(h2_img, cmap='gray')
        # plt.title('Sobel Y2'), plt.xticks([]), plt.yticks([])
        # plt.show()
        end_time3 = time.time()

        h_output_path = Path(
            output_path,
            Path(img_h_path).relative_to(Path(input_path)))
        make_dirs(Path(h_output_path).parent)
        g_output_path = Path(
            output_path,
            Path(img_path).relative_to(Path(input_path)))
        make_dirs(Path(h_output_path).parent)

        cv2.imencode('.tiff', img_h)[1].tofile(h_output_path)
        cv2.imencode('.tiff', image)[1].tofile(g_output_path)

        all_time = end_time3 - start_time3 + end_time2 - start_time2 + end_time1 - start_time1
        # print(all_time)


n = len(img_path_list)
with ThreadPool(processes=thread_num) as pool:
    tasks = [{
        'img_path': img_path,
    } for img_path in img_path_list]
    for i, result in enumerate(pool.imap_unordered(pre_process, tasks)):
        if i % 10 == 0:
            print(i / n * 100)
