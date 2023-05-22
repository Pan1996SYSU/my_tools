import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QShortcut

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个QWidget作为主窗口的中央窗口
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建多个控件
        self.text_edit = QTextEdit()
        self.button = QPushButton("Click me")
        self.line_edit = QLineEdit()

        # 将控件添加到布局中
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.line_edit)

        # 将布局应用到中央窗口
        central_widget.setLayout(layout)

        # 创建一个QShortcut，设置快捷键为Ctrl+K，并将其快捷键事件与槽函数连接
        self.shortcut = QShortcut(QKeySequence("Ctrl+K"), self)
        self.shortcut.activated.connect(self.on_shortcut_activated)

    def on_shortcut_activated(self):
        print("Ctrl+K pressed")

app = QApplication(sys.argv)
main_win = MainWindow()
main_win.show()
sys.exit(app.exec_())
