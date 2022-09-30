
import cv2
img_2d_path = r"D:\桌面\pth\2_00PCBGDN01L09CC980001755_03-12-27.bmp.bmp"
img_lum_path = r"D:\桌面\pth\2-00PCBGDN01L09CC980001755-20220912-031231.png"

from sonic.utils_func import cv_img_read

img_2d = cv_img_read(img_2d_path)
img_lum = cv_img_read(img_lum_path)

img_2d = cv2.copyMakeBorder(
                    img_2d, 0, 200, 0, 200, cv2.BORDER_REPLICATE)

x = 1454
y = 973

r = 900

h_lum, w_lum = img_lum.shape[:2]
h_2d, w_2d = img_2d.shape[:2]

img_lum_res = img_lum[y - r:y + r, x - r:x + r].copy()
img_2d_res = img_2d[150:1570, 450:1870].copy()

up = y - 0
down = 2100 - y
left = x - 0
right = 2200 - x

cv2.namedWindow('2d', 0)
cv2.namedWindow('lum', 0)
cv2.resizeWindow('2d', 600, 600)
cv2.resizeWindow('lum', 600, 600)
cv2.imshow('2d', img_2d_res)
cv2.imshow('lum', img_lum_res)
cv2.waitKey(0)