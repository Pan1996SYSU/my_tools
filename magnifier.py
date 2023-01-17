import sys

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFrame


class AreaMagnification(QMainWindow):

    def __init__(self):
        super().__init__()

        self.pixmap = QPixmap("image.png")

        self.image_label = QLabel(self)
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setMouseTracking(True)
        self.image_label.mouseMoveEvent = self.show_color
        self.setCentralWidget(self.image_label)

        self.color_label = QLabel(self)
        self.color_label.setFixedSize(100, 100)
        self.color_label.setStyleSheet(
            "QLabel { border: 1px solid blue;  \
                                                background-color: white; position: absolute; left: 0px; top: 0px;}"
        )

        self.horizontal_line = QFrame(self.color_label)
        self.horizontal_line.setGeometry(QRect(0, 50, 100, 1))
        self.horizontal_line.setFrameShape(QFrame.HLine)
        self.horizontal_line.setFrameShadow(QFrame.Sunken)
        self.horizontal_line.setLineWidth(1)
        self.horizontal_line.setStyleSheet('background-color:blue;')

        self.vertical_line = QFrame(self.color_label)
        self.vertical_line.setGeometry(QRect(50, 0, 1, 100))
        self.vertical_line.setFrameShape(QFrame.VLine)
        self.vertical_line.setFrameShadow(QFrame.Sunken)
        self.vertical_line.setLineWidth(1)
        self.vertical_line.setStyleSheet('background-color:blue;')

    def show_color(self, event):
        x, y = event.pos().x(), event.pos().y()
        color_area = self.pixmap.copy(x - 15, y - 15, 30, 30)
        color_area = color_area.scaled(100, 100)
        self.color_label.setPixmap(color_area)

        pos_x = x + 30
        pos_y = y + 30
        if pos_x + 100 > self.pixmap.width():
            pos_x -= 160
        if pos_y + 100 > self.pixmap.height():
            pos_y -= 160
        self.color_label.move(pos_x, pos_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    am = AreaMagnification()
    am.show()
    am.color_label.show()
    sys.exit(app.exec_())
