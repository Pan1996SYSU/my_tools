import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 初始化计数器和窗口标题
        self.counter = 0
        self.setWindowTitle(f"Time elapsed: {self.counter} seconds")

        # 创建 QTimer 对象
        self.timer = QTimer()

        # 将 QTimer.timeout 信号连接到自定义的槽函数
        self.timer.timeout.connect(self.update_title)

        # 设置计时器间隔（毫秒）并启动计时器
        self.timer.start(1000)

    def update_title(self):
        # 槽函数：更新窗口标题
        self.counter += 1
        self.setWindowTitle(f"Time elapsed: {self.counter} seconds")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
