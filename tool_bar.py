from PyQt5 import QtWidgets, QtCore


class ToolBar(QtWidgets.QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        lay = self.findChild(QtWidgets.QLayout)
        if lay is not None:
            lay.setExpanded(True)
        QtCore.QTimer.singleShot(0, self.on_timeout)

    @QtCore.pyqtSlot()
    def on_timeout(self):
        button = self.findChild(QtWidgets.QToolButton, "qt_toolbar_ext_button")
        if button is not None:
            button.setFixedSize(0, 0)

    def event(self, e):
        if e.type() == QtCore.QEvent.Leave:
            return True
        return super().event(e)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    toolbar = ToolBar()
    for i in range(20):
        toolbar.addAction("action{}".format(i))
    w.addToolBar(QtCore.Qt.TopToolBarArea, toolbar)

    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())