from sonic.utils_func import glob_extensions

target_img_path = r''
copy_json_path = r''

img_path_list = glob_extensions(target_img_path)
json_path_list = glob_extensions(copy_json_path, ['.json'])