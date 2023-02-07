import traceback
from multiprocessing.pool import ThreadPool
import halcon as ha
import cv2
from sonic.utils_func import glob_extensions, cv_img_read
from pathlib import Path

input_path = r"Z:/2-现场取图/CYS.221102-绿胶AI增值ATL-2/19-长胶2-左-绿胶-分离"
output_path = r"D:\桌面\pth"
img_path_list = glob_extensions(input_path)

y_add = 80
padding = 50
n = 470


def func(task):
    img_path = task.get('img_path', None)
    try:
        SearchImage = ha.read_image(img_path)
        Image1, Image2, Image3 = ha.decompose3(SearchImage)
        Regions = ha.threshold(Image3, 118, 224)
        ConnectedRegions = ha.connection(Regions)
        SelectedRegions = ha.select_shape(ConnectedRegions, 'height', 'and', 10, 1000)
        SelectedRegions1 = ha.select_shape(SelectedRegions, 'column1', 'and', 0, 1000)
        SelectedRegions2 = ha.select_shape(SelectedRegions1, 'width', 'and', 200, 99999)
        RegionUnion = ha.union1(SelectedRegions2)
        Rows, Columns = ha.get_region_points(RegionUnion)
        x1 = 0
        x2 = max(Columns)
        y1 = min(Rows)
        y2 = max(Rows)
        img = cv_img_read(img_path)
        h, w = img.shape[:2]
        img_res = img[max(0, y1 + y_add):min(h, y1 + 470), max(0, x1 - padding):min(w, x2 + padding)].copy()
        suffix = Path(img_path).suffix
        output_img_path = Path(
            output_path,
            Path(img_path).relative_to(Path(input_path)))
        cv2.imencode(suffix, img_res)[1].tofile(output_img_path)
    except Exception as e:
        print(e)
        print(img_path)
        print(traceback.print_exc())


if __name__ == '__main__':
    with ThreadPool(processes=16) as pool:
        tasks = [{
            'img_path': img_path,
        } for img_path in img_path_list]
        for i, result in enumerate(pool.imap_unordered(func, tasks)):
            pass
