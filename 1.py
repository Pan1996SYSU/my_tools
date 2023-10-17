from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        self.tab1 = QWidget(self)
        self.tab2 = QWidget(self)

        self.tab_widget.addTab(self.tab1, "Tab 1")
        self.tab_widget.addTab(self.tab2, "Tab 2")

        self.tab1_layout = QVBoxLayout(self.tab1)
        self.tab1_label = QLabel("This is Tab 1", self.tab1)
        self.tab1_layout.addWidget(self.tab1_label)

        self.tab2_layout = QVBoxLayout(self.tab2)
        self.tab2_label = QLabel("This is Tab 2", self.tab2)
        self.tab2_layout.addWidget(self.tab2_label)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
