from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen
from PyQt5.QtCore import Qt

class DrawingLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(500, 500)
        self.pixmap = QPixmap(500, 500)
        self.pixmap.fill(Qt.white)
        self.setPixmap(self.pixmap)
        self.last_x, self.last_y = None, None

    def mousePressEvent(self, event):
        self.last_x, self.last_y = event.x(), event.y()
        self.update()

    def mouseMoveEvent(self, event):
        painter = QPainter(self.pixmap)
        pen = QPen(Qt.black, 5, Qt.SolidLine)
        painter.setPen(pen)
        if self.last_x is not None and self.last_y is not None:
            painter.drawLine(self.last_x, self.last_y, event.x(), event.y())
            self.update()
        self.last_x, self.last_y = event.x(), event.y()
        self.update()

if __name__ == '__main__':
    app = QApplication([])
    label = DrawingLabel()
    label.show()
    app.exec_()
