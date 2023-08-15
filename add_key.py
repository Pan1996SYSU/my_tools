import os
import winreg


def main():
    my_app_path = os.path.abspath(r"D:\桌面\LabelMe.exe")
    icon_path = os.path.abspath(r"D:\桌面\icon.ico")

    # 创建右键菜单项
    key = winreg.CreateKey(
        winreg.HKEY_CURRENT_USER,
        "Software\\Classes\\Directory\\Background\\shell\\Open with LabelMe")
    winreg.SetValue(key, "", winreg.REG_SZ, "使用 LabelMe 打开")
    winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, icon_path)

    # 创建命令项，并将选中目录的路径作为参数
    key_cmd = winreg.CreateKey(key, "command")
    winreg.SetValue(key_cmd, "", winreg.REG_SZ, f'"{my_app_path}" "%V"')


if __name__ == "__main__":
    main()
