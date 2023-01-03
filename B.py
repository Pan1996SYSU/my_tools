from PyQt5.Qt import *

from A import A


class B(QObject):

    def get_msg(self, string, aa):
        print('你好' + string)
        print(aa)


b = B()
a = A()

a.sig.connect(b.get_msg)
a.send_msg()
