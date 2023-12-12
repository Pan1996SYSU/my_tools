import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import json


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login')

        self.label_username = QLabel('Username:', self)
        self.label_username.move(50, 30)

        self.entry_username = QLineEdit(self)
        self.entry_username.move(150, 30)

        self.label_password = QLabel('Password:', self)
        self.label_password.move(50, 70)

        self.entry_password = QLineEdit(self)
        self.entry_password.setEchoMode(QLineEdit.Password)
        self.entry_password.move(150, 70)

        self.button_login = QPushButton('Login', self)
        self.button_login.move(150, 120)
        self.button_login.clicked.connect(self.login)

        self.setGeometry(300, 300, 300, 200)
        self.show()

    def login(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        # 在这里执行登录验证的逻辑，获取令牌（token）
        # 假设登录验证成功，获取到了令牌
        token = "your_token"

        # 将令牌缓存到本地
        with open("token.json", "w") as file:
            json.dump({"token": token}, file)

        # 关闭登录窗口
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    sys.exit(app.exec_())
