import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor


class WidgetOne(QWidget):
    def __init__(self):
        super().__init__()
        self.setAutoFillBackground(True)
        self.setMouseTracking(True)
        self.setFixedSize(100, 100)
        self.white_palette = QPalette()
        self.white_palette.setColor(QPalette.Background, QColor(Qt.white))
        self.gray_palette = QPalette()
        self.gray_palette.setColor(QPalette.Background, QColor(Qt.gray))

    def enterEvent(self, event):
        self.setPalette(self.gray_palette)

    def leaveEvent(self, event):
        self.setPalette(self.white_palette)


class WidgetTwo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        for _ in range(3):
            widget_one = WidgetOne()
            layout.addWidget(widget_one)

        self.setLayout(layout)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        widget_two = WidgetTwo()
        main_layout = QVBoxLayout()
        main_layout.addWidget(widget_two)
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
