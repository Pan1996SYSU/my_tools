import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from pyqtgraph.parametertree import Parameter, ParameterTree
from pyqtgraph.parametertree.parameterTypes import GroupParameter, ListParameter

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个参数树
        self.parameter_tree = ParameterTree()
        self.setCentralWidget(self.parameter_tree)

        # 创建一个参数组，并添加到参数树中
        self.group_param = GroupParameter(name='Parameters')
        self.parameter_tree.setParameters(self.group_param, showTop=False)

        # 创建一个新的参数类型 "new_list"，并添加到参数组中
        self.new_list_param = ListParameter(name='new_list', values=[1, 2, 3, 4], value=1)
        self.group_param.addChild(self.new_list_param)

        # 为新的参数类型添加子参数
        self.button_params = []
        for i in range(1, 5):
            button_param = Parameter(name=f'Button {i}', type='bool', value=False)
            self.new_list_param.addChild(button_param)
            self.button_params.append(button_param)

        # 监听参数值的变化，根据新的值显示或隐藏对应的子参数
        self.new_list_param.sigValueChanged.connect(self.update_button_params)

    def update_button_params(self, param, value):
        # 隐藏所有的按钮子参数
        for button_param in self.button_params:
            button_param.hide()

        # 显示对应值的按钮子参数
        index = value - 1
        if index >= 0 and index < len(self.button_params):
            self.button_params[index].show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
