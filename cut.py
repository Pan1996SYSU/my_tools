import cv2
from sonic.utils_func import cv_img_read

img = cv_img_read(
    r'D:/桌面/无为-2D-虚焊/0JBMBPE4M272KDC9X3300120_0017_14-00-00-89_Lum.tiff')
crop_img = img[720:1270, 700:1390]
cv2.imencode('.tiff', crop_img)[1].tofile(r'D:/桌面/img/1.tiff')
