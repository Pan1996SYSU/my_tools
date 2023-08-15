import winreg


def main():
    # 删除菜单项
    try:
        winreg.DeleteKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\Classes\\sonic_suffix_cpth\\shell\\使用Detection打开\\command"
        )
    except Exception as e:
        print(f"删除11菜单项时发生错误：{e}")
    try:
        winreg.DeleteKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\Classes\\sonic_suffix_cpth\\shell\\使用Detection打开")
    except Exception as e:
        print(f"删除13菜单项时发生错误：{e}")

    # 删除菜单项
    try:
        winreg.DeleteKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\Classes\\sonic_suffix_pth\\shell\\使用Detection打开\\command"
        )
    except Exception as e:
        print(f"删除21菜单项时发生错误：{e}")
    try:
        winreg.DeleteKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\Classes\\sonic_suffix_pth\\shell\\使用Detection打开")
    except Exception as e:
        print(f"删除23菜单项时发生错误：{e}")

    # 删除菜单项
    try:
        winreg.DeleteKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\Classes\\sonic_suffix_ctrt\\shell\\使用Detection打开\\command"
        )
    except Exception as e:
        print(f"删除31菜单项时发生错误：{e}")
    try:
        winreg.DeleteKey(
            winreg.HKEY_CURRENT_USER,
            "Software\\Classes\\sonic_suffix_ctrt\\shell\\使用Detection打开")
    except Exception as e:
        print(f"删除33菜单项时发生错误：{e}")


if __name__ == "__main__":
    main()
