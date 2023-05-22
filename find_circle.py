import halcon as ha
from sonic.utils_func import glob_extensions, cv_img_read

r = 780

Image = ha.read_image('D:/桌面/img/01-OK/23年05月08日-13时53分27秒200_2D1C.bmp')
ROI = ha.gen_circle(987.57, 1328.72, 843.136)
ImageReduced = ha.reduce_domain(Image, ROI)

Edges = ha.edges_sub_pix(ImageReduced, 'canny', 1, 40, 70)
ModelID = ha.create_shape_model_xld(
    Edges, 'auto', -180, 180, 'auto', 'auto', 'ignore_local_polarity', 1)

img_path_list = glob_extensions(r'D:/桌面/img')
for img_path in img_path_list:
    try:
        Image = ha.read_image(img_path)
        Width, Height = ha.get_image_size(Image)
        Row, Column, Angle, Scale, Score1, Model = ha.find_scaled_shape_models(
            Image, ModelID, -180, 180, 1, 1, 0.5, 1, 0, 'least_squares', 0,
            0.9)
        x = round(Row[0])
        y = round(Column[0])

        img = cv_img_read(img_path)
        h, w = img.shape[:2]
        res_img = img[max(0, y - r):min(h, y + r),
                      max(0, x - r):min(w, x + r)].copy()

    except:
        print(img_path)
