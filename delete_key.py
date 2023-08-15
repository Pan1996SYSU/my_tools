import winreg

def main():
    # 删除菜单项
    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, "Software\\Classes\\Directory\\Background\\shell\\Open with LabelMe\\command")
    except Exception as e:
        print(f"删除菜单项时发生错误：{e}")
    try:
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, "Software\\Classes\\Directory\\Background\\shell\\Open with LabelMe")
    except Exception as e:
        print(f"删除菜单项时发生错误：{e}")

if __name__ == "__main__":
    main()