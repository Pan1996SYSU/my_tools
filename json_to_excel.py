import json
from glob import glob

import pandas as pd

input_path = r"D:\桌面\密封钉数据分析\20220821-185055_CYS.220301-密封钉检测3D_旋转_raw-OK\NG"
json_path_list = glob(f'{input_path}/**/*.json', recursive=True)

json_data_list = [json.load(open(x, encoding='utf-8')) for x in json_path_list]

excel_2D = []
excel_3D = []
excel_2D3D = []

for json_data in json_data_list:
    category_name_set = set()
    img_name = json_data['img_name']
    results_data = []
    for result in json_data["result"]:
        r_data = [
            result['category_name'], result['area'], result['bbox'][0],
            result['bbox'][1], result['bbox'][2], result['bbox'][3],
            result['center_distance'], result['delta'], result['height'],
            result['max_area'], result['mean_foreground'],
            result['min_height'], result['min_width'], result['score'],
            result['volume'], result['width'], img_name
        ]
        category_name_set.add(result['category_name'][:2])
        results_data.append(r_data)
    if len(category_name_set) == 1:
        if list(category_name_set)[0] == '2D':
            for r in results_data:
                excel_2D.append(r)
        elif list(category_name_set)[0] == '3D':
            for r in results_data:
                excel_3D.append(r)
        else:
            print(f'{list(category_name_set)[0]}, {img_name}')
    else:
        for r in results_data:
            excel_2D3D.append(r)

# data_2D = pd.DataFrame(data=excel_2D)
# file_path = pd.ExcelWriter(
#     f'D:/桌面/test/OK/2D汇总.xlsx')
# data_2D.to_excel(
#     file_path,
#     sheet_name='2D',
#     encoding='utf-8',
#     index=False)
# file_path.save()
#
# data_3D = pd.DataFrame(data=excel_3D)
# file_path = pd.ExcelWriter(
#     f'D:/桌面/test/OK/3D汇总.xlsx')
# data_3D.to_excel(
#     file_path,
#     sheet_name='3D',
#     encoding='utf-8',
#     index=False)
# file_path.save()

data_2D3D = pd.DataFrame(data=excel_2D3D)
file_path = pd.ExcelWriter(f'D:/桌面/test/OK/2D3D汇总.xlsx')
data_2D3D.to_excel(file_path, sheet_name='OK', encoding='utf-8', index=False)
file_path.save()
