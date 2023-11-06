import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("Left button released")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
