from sonic.utils_func import glob_extensions, make_dirs
from pathlib import Path
import cv2

paths = glob_extensions(r"D:\baidu\ikonate_blue")
for p in paths:
    img = cv2.imread(p,cv2.IMREAD_UNCHANGED)
    img[:, :, 3][img[:, :, 3] > 180] = 180
    p = Path(p)
    suffix = p.suffix
    output_img_path = Path(r"D:\桌面\icons", Path(p).relative_to(Path(r"D:\baidu")))
    make_dirs(output_img_path.parent)
    cv2.imencode(suffix, img)[1].tofile(output_img_path)