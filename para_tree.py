import sys

import pyqtgraph as pg
import pyqtgraph.parametertree.parameterTypes as pTypes


class MyListParameterItem(pTypes.ListParameterItem):

    def valueChanged(self, param, value, force=False):
        super().valueChanged(param, value, force)
        for i in range(self.childCount()):
            if i == self.widget.currentIndex():
                self.child(i).setHidden(False)
                self.child(i).param.opts['visible'] = True
            else:
                self.child(i).setHidden(True)
                self.child(i).param.opts['visible'] = False

    def addChild(self, child):
        super().addChild(child)
        if self.childCount() == len(self.param.childs):
            for i in range(self.childCount()):
                if i == self.widget.currentIndex():
                    self.child(i).setHidden(False)
                    self.child(i).param.opts['visible'] = True
                else:
                    self.child(i).setHidden(True)
                    self.child(i).param.opts['visible'] = False


class MyListParameter(pTypes.ListParameter):
    itemClass = MyListParameterItem

    def setLimits(self, limits):
        limits.clear()
        for child in self.childs:
            limits.append(child.name())
        super().setLimits(limits)


pTypes.registerParameterType('new_list', MyListParameter, override=True)
if __name__ == '__main__':
    # Test the new list parameter
    newlist = [
        {
            'name': 'List',
            'type': 'new_list',
            'children': [
                {
                    'name': 'str',
                    'type': 'str',
                    'value': 'default value'
                }, {
                    'name': 'int',
                    'type': 'int',
                    'value': 0
                }, {
                    'name': 'float',
                    'type': 'float',
                    'value': 1.0
                }, {
                    'name': 'str2',
                    'type': 'str',
                    'value': 'fuck'
                }
            ],
            'children2': [
                {
                    'name': 'str',
                    'type': 'str',
                    'value': 'default value'
                }, {
                    'name': 'int',
                    'type': 'int',
                    'value': 0
                }
            ],
        }
    ]

    # Create parameters manually
    params = pTypes.SimpleParameter(
        name='Parameters', type='group', children=newlist)

    # Create a ParameterTree and add the parameters
    app = pg.mkQApp()
    param_tree = pg.parametertree.ParameterTree()
    param_tree.setParameters(params, showTop=False)

    # Show the ParameterTree
    param_tree.show()

    # Start the Qt event loop
    sys.exit(app.exec_())
