import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class CenterPointWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # 设置窗口属性
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 设置窗口大小和位置
        screen_geometry = QApplication.desktop().availableGeometry()
        window_width, window_height = 7, 7
        window_x = screen_geometry.width() // 2 - window_width // 2
        window_y = screen_geometry.height() // 2 - window_height // 2
        self.setGeometry(window_x, window_y, window_width, window_height)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制一个白色的点
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 255, 255))
        painter.drawEllipse(self.rect())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CenterPointWindow()
    window.show()
    sys.exit(app.exec_())
