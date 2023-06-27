import sys

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFrame

FixedSize = 100
LineWidth = 1
AreaSize = 30


class AreaMagnification(QMainWindow):

    def __init__(self):
        super().__init__()

        self.pixmap = QPixmap(r"D:\桌面\sth\Cam_3-01-05 14_33_39_970_NG.bmp")

        self.image_label = QLabel(self)
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setMouseTracking(True)
        self.image_label.mouseMoveEvent = self.show_color
        self.setCentralWidget(self.image_label)

        self.color_label = QLabel(self)
        self.color_label.setFixedSize(FixedSize, FixedSize)
        self.color_label.setStyleSheet(
            "QLabel { border: 1px solid blue;  \
                                                background-color: white; position: absolute; left: 0px; top: 0px;}"
        )

        self.horizontal_line = QFrame(self.color_label)
        self.horizontal_line.setGeometry(QRect(0, int(FixedSize/2), FixedSize, LineWidth))
        self.horizontal_line.setFrameShape(QFrame.HLine)
        self.horizontal_line.setFrameShadow(QFrame.Sunken)
        self.horizontal_line.setLineWidth(LineWidth)
        self.horizontal_line.setStyleSheet('background-color:blue;')

        self.vertical_line = QFrame(self.color_label)
        self.vertical_line.setGeometry(QRect(int(FixedSize/2), 0, LineWidth, FixedSize))
        self.vertical_line.setFrameShape(QFrame.VLine)
        self.vertical_line.setFrameShadow(QFrame.Sunken)
        self.vertical_line.setLineWidth(LineWidth)
        self.vertical_line.setStyleSheet('background-color:blue;')

    def show_color(self, event):
        x, y = event.pos().x(), event.pos().y()
        color_area = self.pixmap.copy(int(x - AreaSize/2), int(y - AreaSize/2), AreaSize, AreaSize)
        color_area = color_area.scaled(FixedSize, FixedSize)
        self.color_label.setPixmap(color_area)

        pos_x = x + AreaSize
        pos_y = y + AreaSize
        if pos_x + FixedSize > self.pixmap.width():
            pos_x -= (FixedSize + 2 * AreaSize)
        if pos_y + FixedSize > self.pixmap.height():
            pos_y -= (FixedSize + 2 * AreaSize)
        self.color_label.move(pos_x, pos_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    am = AreaMagnification()
    am.show()
    am.color_label.show()
    sys.exit(app.exec_())
