import cv2
from sonic.utils_func import cv_img_read, show_img

# img_path = r"D:\桌面\1_001CE230000001CC90305909_17-28-42.bmp.bmp"
# img = cv_img_read(img_path)
#
# crop_img = img[237:2294, 1133:3157].copy()
# cv2.imencode('.bmp', crop_img)[1].tofile(r"D:\桌面\1.bmp")

img_path = r"D:\桌面\1-001CE230000001CC90305909-20221211-052841-Lum.png"
img = cv_img_read(img_path)
img_flip = cv2.flip(img, 1)
h, w = img.shape[:2]
img_res = img_flip[60:h - 40, 200:w - 210].copy()
print(60, h - 40, 200, w - 210)
show_img(img_res)
