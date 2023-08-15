import winreg

def add_to_registry(extension, name, command):
    # 获取 HKEY_CURRENT_USER\Software\Classes 所对应的键
    classes_key = winreg.OpenKey(
    winreg.HKEY_CURRENT_USER, 'Software\Classes', 0, winreg.KEY_WRITE)

    # 创建指定扩展名的键
    extension_key = winreg.CreateKey(classes_key, extension)

    # 获取文件类型的默认值，例如 ".pth" 所对应的默认值可能是 "Python.File"
    file_type, _ = winreg.QueryValueEx(extension_key, '')
    # 关闭 "extension" 键
    winreg.CloseKey(extension_key)

    # 创建文件类型键
    file_type_key = winreg.CreateKey(classes_key, file_type)

    # 创建 "shell" 子项
    shell_key = winreg.CreateKey(file_type_key, 'shell')

    # 创建命令项
    app_key = winreg.CreateKey(shell_key, name)
    command_key = winreg.CreateKey(app_key, 'command')
    winreg.SetValueEx(app_key, 'Icon', 0, winreg.REG_SZ, command)

    # 设置命令项的默认值
    winreg.SetValueEx(command_key, '', 0, winreg.REG_SZ, command)

    # 关闭所有打开的键
    winreg.CloseKey(command_key)
    winreg.CloseKey(app_key)
    winreg.CloseKey(shell_key)
    winreg.CloseKey(file_type_key)
    winreg.CloseKey(classes_key)

add_to_registry('.pth', '使用Detection打开', r'D:\桌面\Detection.exe "%1"')
add_to_registry('.cpth', '使用Detection打开', r'D:\桌面\Detection.exe "%1"')
add_to_registry('.ctrt', '使用Detection打开', r'D:\桌面\Detection.exe "%1"')
