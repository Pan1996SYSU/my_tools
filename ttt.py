import sys
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget


class Example(QWidget):

    def __init__(self):
        super().__init__()

        # 创建一个QStackedWidget
        self.stack = QStackedWidget(self)
        self.stack.setGeometry(0, 0, 200, 200)

        # 创建两个子QWidget
        self.widget1 = QWidget(self)
        self.widget2 = QWidget(self)
        self.widget1.setStyleSheet("background-color: blue;")  # 设置widget1的背景颜色
        self.widget2.setStyleSheet("background-color: red;")  # 设置widget2的背景颜色

        # 将两个子QWidget添加到QStackedWidget中
        self.stack.addWidget(self.widget1)
        self.stack.addWidget(self.widget2)

        # 设置widget2的透明度为50%
        self.widget2.setStyleSheet("background-color: rgba(255, 0, 0, 128);")

        # 设置当前显示的QWidget
        self.stack.setCurrentIndex(1)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
