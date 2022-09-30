from glob import glob
from pathlib import Path
import numpy as np
from sonic.utils_func import load_json

# df = pd.read_excel('瑞浦顶盖焊.xls', sheet_name='过杀',usecols='a')
# output_path = r'D:\桌面\顶盖焊\过杀'
# buffer_size = 102400
#
#
# mylist = df.values.tolist()
# img_path_list=[]
# for i in mylist:
#     img_path_list.append(i[0])

json_path = r'D:\桌面\20220908-162438_20220907_152159_01-NG标注\NG\json'

json_path_list = glob(f'{json_path}/**/*.json', recursive=True)
i = 0
bbox_w = []
name = "max_height_diff"
for json_path in json_path_list:
    json_data = load_json(json_path)
    results = json_data["result"]
    num = len(results)
    for result in results:
        w = result[name]
        # if w < 50 and num == 1:
        #     i += 1
        if not np.isnan(w):
            if num == 1:
                bbox_w.append(w)

import pandas as pd
import matplotlib.pyplot as plt

data = bbox_w
df = pd.DataFrame(data)
print(df.describe())
df.plot.box(title="Box Chart")
plt.grid(linestyle="--", alpha=0.3)
plt.show()


print('ok')
