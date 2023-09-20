import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QColor, QPalette


class ColorWidget(QWidget):
    def __init__(self, color, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class ColorChangeApp(QWidget):
    def __init__(self):
        super().__init__()

        self.blue_widget = ColorWidget("blue", self)
        self.green_widget = ColorWidget("green", self)
        self.current_widget = self.blue_widget

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Change App')

        self.button = QPushButton('Change Color', self)
        self.button.clicked.connect(self.toggleColor)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.blue_widget)
        self.layout.addWidget(self.green_widget)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def toggleColor(self):
        if self.current_widget == self.blue_widget:
            self.blue_widget.hide()
            self.green_widget.show()
            self.current_widget = self.green_widget
        else:
            self.green_widget.hide()
            self.blue_widget.show()
            self.current_widget = self.blue_widget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorChangeApp()
    window.show()
    sys.exit(app.exec_())
