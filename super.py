import sys

import pyqtgraph as pg
import pyqtgraph.parametertree.parameterTypes as pTypes


class MyListParameterItem(pTypes.ListParameterItem):

    def valueChanged(self, param, value, force=False, *args):
        super().valueChanged(param, value, force, *args)
        for i in range(self.childCount()):
            if i == self.widget.currentIndex():
                self.child(i).setHidden(False)
            else:
                self.child(i).setHidden(True)


class MyListParameter(pTypes.ListParameter):
    itemClass = MyListParameterItem

    def setLimits(self, limits):
        limits.clear()
        for child in self.childs:
            limits.append(child.name())
        super().setLimits(limits)


pTypes.registerParameterType('mylist', MyListParameter, override=True)
if __name__ == '__main__':
    # Test the new list parameter
    newlist = [
        {
            'name': 'List',
            'type': 'mylist',
            'children': [
                {
                    'name': 'Item 1',
                    'type': 'str',
                    'value': 'default value'
                }, {
                    'name': 'Item 2',
                    'type': 'int',
                    'value': 0
                }, {
                    'name': 'Item 3',
                    'type': 'float',
                    'value': 1.0
                }
            ]
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
