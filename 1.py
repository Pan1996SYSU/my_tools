import os

def count_lines(directory):
    total_lines = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()
                    total_lines += len(lines)

    return total_lines


# 调用函数统计代码行数
lines_of_code = count_lines(r"D:\桌面\plugin-imagewatch-master")

print("该路径下的Java项目代码行数为:", lines_of_code)
