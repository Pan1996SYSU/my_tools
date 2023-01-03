from PyQt5.Qt import *


class A(QObject):
    sig = pyqtSignal(str, int)

    def send_msg(self):
        self.sig.emit('hello', 2)
