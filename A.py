from PyQt5.Qt import *


class A(QObject):
    sendmsg = pyqtSignal(str, int)

    def send_msg(self):
        self.sendmsg.emit('hello', 2)
