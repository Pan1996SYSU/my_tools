import os


def check_duplicate_files(folder_path):
    """
    检查指定文件夹下所有文件是否有重名情况
    """
    file_dict = {}

    # 遍历文件夹下所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 获取文件名
            file_name = os.path.basename(file)
            # 如果文件名已经存在，则将其添加到字典中
            if file_name in file_dict:
                file_dict[file_name].append(os.path.join(root, file))
            else:
                file_dict[file_name] = [os.path.join(root, file)]

    # 输出有重名的文件
    for file_name, file_paths in file_dict.items():
        if len(file_paths) > 1:
            print(f"文件名 {file_name} 存在重名，路径为:")
            for file_path in file_paths:
                print(f"\t{file_path}")


check_duplicate_files(r"Z:\5-标注数据\CYS.220818-利元亨南京国轩整线-顶盖焊\4线")
