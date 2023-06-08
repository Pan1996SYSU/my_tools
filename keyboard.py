import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Drawing text')

        self.show()

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawKey(qp, 'A', 20, 20)
        self.drawKey(qp, 'B', 70, 20)
        self.drawKey(qp, 'C', 120, 20)
        self.drawKey(qp, 'D', 170, 20)
        qp.end()

    def drawKey(self, qp, text, x, y):

        qp.setPen(Qt.black)
        qp.drawRect(x, y, 50, 50)

        if text in self.pressed_keys:
            qp.setBrush(QColor(255, 0, 0))
        else:
            qp.setBrush(QColor(255, 255, 255))

        qp.drawRect(x + 5, y + 5, 40, 40)

        qp.setFont(QFont('Decorative', 10))
        qp.drawText(x + 20, y + 30, text)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_A:
            self.pressed_keys.add('A')
        elif key == Qt.Key_B:
            self.pressed_keys.add('B')
        elif key == Qt.Key_C:
            self.pressed_keys.add('C')
        elif key == Qt.Key_D:
            self.pressed_keys.add('D')
        self.update()

    def keyReleaseEvent(self, event):
        key = event.key()
        if key == Qt.Key_A:
            self.pressed_keys.remove('A')
        elif key == Qt.Key_B:
            self.pressed_keys.remove('B')
        elif key == Qt.Key_C:
            self.pressed_keys.remove('C')
        elif key == Qt.Key_D:
            self.pressed_keys.remove('D')
        self.update()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ex.pressed_keys = set()
    sys.exit(app.exec_())
