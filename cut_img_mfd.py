import json
import numpy as np
from glob import glob
import os
import cv2
from pathlib import Path

img_path = r'C:\Users\cys01\Desktop\密封钉裁图\input'
predict_json = r'C:\Users\cys01\Desktop\密封钉裁图\predict'
output_path = r'C:\Users\cys01\Desktop\密封钉裁图\output'

img_list = glob(img_path + '/**', recursive=True)
predict_json_list = glob(predict_json + '/**', recursive=True)
predict = {}

for js in predict_json_list:
    if js[-4:] == 'json':
        file_name = js.split('\\')[-1].rsplit('.', 1)[0]
        predict[file_name] = js

for path in img_list:
    if path[-3:] == 'jpg':
        img = cv2.imdecode(np.fromfile(path, dtype=np.uint8), -1)
        key = path.split('\\')[-1].rsplit('.', 1)[0]
        json_path = predict[key]
        with open(json_path, "r", encoding='utf-8') as f1:
            js1 = json.load(f1)
            if "result" in js1:
                result = js1["result"][0]
                if "bbox" in result:
                    points = result["bbox"]
                    x = points[0]
                    y = points[1]
                    w = points[2]
                    h = points[3]
                    real_x = max(int(x - 200), 0)
                    real_y = max(int(y - 200), 0)
                    real_w = int(w + 400)
                    real_h = int(h + 400)
                    retval = img[real_y:real_y + real_h,
                                 real_x:real_x + real_w].copy()
                    if os.path.exists(path[:-3] + 'json'):
                        with open(path[:-3] + 'json', "r",
                                  encoding='utf-8') as f2:
                            js2 = json.load(f2)
                            js2["imageHeight"] = real_h
                            js2["imageWidth"] = real_w
                            for i in range(len(js2["shapes"])):
                                for j in range(len(
                                        js2["shapes"][i]["points"])):
                                    js2["shapes"][i]["points"][j][0] = js2[
                                        "shapes"][i]["points"][j][0] - real_x
                                    js2["shapes"][i]["points"][j][1] = js2[
                                        "shapes"][i]["points"][j][1] - real_y
                            for i in range(len(js2["shapes"])):
                                new_points = []
                                for j in range(len(
                                        js2["shapes"][i]["points"])):
                                    if real_w > js2["shapes"][i]["points"][j][
                                            0] > 0 and real_h > js2["shapes"][
                                                i]["points"][j][1] > 0:
                                        new_points.append(
                                            js2["shapes"][i]["points"][j])
                                js2["shapes"][i]["points"] = new_points
                            file_path = path.rsplit('\\', 1)[0]
                            relative = Path(file_path).relative_to(
                                Path(img_path))
                            output = str(Path(output_path, relative))
                            if not os.path.exists(output):
                                os.makedirs(output)
                            with open(output + '/' + key + '.json', 'w',
                                      encoding='utf8') as f3:
                                json.dump(
                                    js2, f3, ensure_ascii=False, indent=4)
                        cv2.imencode(
                            '.jpg',
                            retval)[1].tofile(output + '/' + key + '.jpg')
                    else:
                        file_path = path.rsplit('\\', 1)[0]
                        relative = Path(file_path).relative_to(Path(img_path))
                        output = str(Path(output_path, relative))
                        if not os.path.exists(output):
                            os.makedirs(output)
                        cv2.imencode(
                            '.jpg',
                            retval)[1].tofile(output + '/' + key + '.jpg')
