import sys
import os
from PyQt5.QtWidgets import QApplication

def add_context_menu_registry_entry():
    app_name = "MyApp"
    app_path = r"D:\桌面\labelme\release\LabelMe.exe"  # 将路径替换为您的应用程序路径

    key_path = f"Directory\\shell\\{app_name}"
    command_key_path = f"{key_path}\\command"

    try:
        import winreg
    except ImportError:
        print("winreg module is not available. This script only works on Windows.")
        return

    try:
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path) as key:
            winreg.SetValue(key, None, winreg.REG_SZ, app_name)

        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, command_key_path) as key:
            winreg.SetValue(key, None, winreg.REG_SZ, f'"{app_path}" "%1"')
    except Exception as e:
        print(f"Failed to add context menu entry: {e}")
        return

    print("Context menu entry added successfully.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 添加右键菜单项
    add_context_menu_registry_entry()
    sys.exit(app.exec_())
