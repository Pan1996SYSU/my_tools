import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtGui import QPolygon
from PyQt5.QtWidgets import QApplication, QMainWindow

from input_visualization_parameter import keyboard_parameter, keyboard_mapping, mouse_parameter


class VirtualInput(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1150, 340)
        self.setWindowTitle('输入测试')
        self.show()

    def draw_mouse(self):
        painter = QPainter(self)
        pen = QtGui.QPen(QColor(120, 120, 122), 3, QtCore.Qt.SolidLine)

        for key in mouse_parameter.keys():
            if key in self.pressed_keys:
                painter.setBrush(QColor(176, 226, 255))
            else:
                painter.setBrush(QColor(255, 255, 255))

            points = mouse_parameter[key]
            polygon = QPolygon([QPoint(*point) for point in points])
            painter.setPen(pen)
            painter.drawPolygon(polygon)

    def paintEvent(self, event):
        self.draw_mouse()
        qp = QPainter()
        qp.begin(self)
        for key in keyboard_parameter.keys():
            x, y, w, h = keyboard_parameter[key]
            self.drawKey(qp, key, x, y, w, h)
            if key == 'Shift':
                x, y, w, h = keyboard_parameter['shift']
                self.drawKey(qp, 'shift', x, y, w, h)
            elif key == 'Ctrl':
                x, y, w, h = keyboard_parameter['ctrl']
                self.drawKey(qp, 'crl', x, y, w, h)
            elif key == 'Alt':
                x, y, w, h = keyboard_parameter['alt']
                self.drawKey(qp, 'alt', x, y, w, h)
        qp.end()

    def drawKey(self, qp, text, x, y, w, h):
        pen = QtGui.QPen(QColor(120, 120, 122), 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        if text in self.pressed_keys:
            qp.setBrush(QColor(176, 226, 255))
        else:
            qp.setBrush(QColor(255, 255, 255))

        qp.drawRect(x, y, w, h)

        qp.setFont(QFont('Decorative', 10))
        n = len(text)
        qp.drawText(x - 4 * n + w // 2 + 2, y + 30, text)

    def keyPressEvent(self, event):
        key = event.key()
        try:
            k = keyboard_mapping[key]
        except:
            return
        self.pressed_keys.add(k)
        if k == 'Shift':
            self.pressed_keys.add('shift')
        elif k == 'Ctrl':
            self.pressed_keys.add('ctrl')
        elif k == 'Alt':
            self.pressed_keys.add('alt')
        self.update()

    def keyReleaseEvent(self, event):
        key = event.key()
        try:
            k = keyboard_mapping[key]
        except:
            return
        self.pressed_keys.remove(k)
        if k == 'Shift':
            self.pressed_keys.remove('shift')
        elif k == 'Ctrl':
            self.pressed_keys.remove('ctrl')
        elif k == 'Alt':
            self.pressed_keys.remove('alt')
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pressed_keys.add('left')
        elif event.button() == Qt.RightButton:
            self.pressed_keys.add('right')
        elif event.button() == Qt.MiddleButton:
            self.pressed_keys.add('mid')
        elif event.button() == Qt.BackButton:
            self.pressed_keys.add('down')
        elif event.button() == Qt.ForwardButton:
            self.pressed_keys.add('up')
        self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.pressed_keys.remove('left')
        elif event.button() == Qt.RightButton:
            self.pressed_keys.remove('right')
        elif event.button() == Qt.MiddleButton:
            self.pressed_keys.remove('mid')
        elif event.button() == Qt.BackButton:
            self.pressed_keys.remove('down')
        elif event.button() == Qt.ForwardButton:
            self.pressed_keys.remove('up')
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VirtualInput()
    ex.pressed_keys = set()
    sys.exit(app.exec_())
