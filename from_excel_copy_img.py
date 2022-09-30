import pandas as pd
from pathlib import Path
import os
import shutil

df = pd.read_excel('瑞浦顶盖焊.xls', sheet_name='NG',usecols='a')
output_path = r'D:\桌面\NG'
buffer_size = 102400


mylist = df.values.tolist()
img_path_list=[]
for i in mylist:
    img_path_list.append(i[0])

for img_path in img_path_list:
    img_2d_path = Path(img_path)
    img_name = os.path.basename(img_2d_path).split('.')[0][:-2]
    img_2d_parent = img_2d_path.parent
    img_h_path = f'{img_2d_path.parent}/{img_name}H.tiff'
    img_g_path = f'{img_2d_path.parent}/{img_name}Lum.tiff'

    img_2d_basename = os.path.basename(Path(img_2d_path))
    img_g_basename = os.path.basename(Path(img_g_path))
    img_h_basename = os.path.basename(Path(img_h_path))

    d_output_path = f'{output_path}/{img_2d_basename}'
    g_output_path = f'{output_path}/{img_g_basename}'
    h_output_path = f'{output_path}/{img_h_basename}'

    with open(img_2d_path, 'rb') as f_in:
        with open(d_output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out, buffer_size * 1024)
    with open(img_g_path, 'rb') as f_in:
        with open(g_output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out, buffer_size * 1024)
    with open(img_h_path, 'rb') as f_in:
        with open(h_output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out, buffer_size * 1024)