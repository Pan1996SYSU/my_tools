import os
from PIL import Image
from datetime import datetime


def read_images_from_path(path):
    # 获取指定路径下的所有文件名
    filenames = os.listdir(path)

    for filename in filenames:
        # 检查文件是否为图片文件
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            # 拼接完整的文件路径
            image_path = os.path.join(path, filename)

            # 读取图像并计算读取时间
            start_time = datetime.now()
            image = Image.open(image_path)
            end_time = datetime.now()
            read_time = (end_time - start_time).total_seconds()

            if read_time > 0.5:
                # 打印图像的路径和读取时间
                print(f"图像路径：{image_path}")
                print(f"读取时间：{read_time}\n")


# 指定要读取的图像路径
image_path = r"Z:\5-标注数据\CYS.230118-柳州瑞浦-极耳翻折\极耳褶皱"

# 调用函数读取图像并打印读取时间
read_images_from_path(image_path)