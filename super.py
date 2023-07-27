import sys

import pyqtgraph as pg
import pyqtgraph.parametertree.parameterTypes as pTypes


class MyListParameterItem(pTypes.ListParameterItem):
    def value(self):
        """
        Get the current value of the list parameter.
        """
        return self.param.value()

    def setValue(self, value):
        """
        Set the value of the list parameter based on the name of the child.
        """
        self.param.setValue(value)

class MyListParameter(pTypes.ListParameter):
    itemClass = MyListParameterItem

pTypes.registerParameterType('mylist', MyListParameter, override=True)

if __name__ == '__main__':
    # Register the new parameter type
    pTypes.registerParameterType('mylist', MyListParameter, override=True)

    # Test the new list parameter
    newlist = [
        {
            'name': 'List',
            'type': 'mylist',
            'limits': [
                'Item 1',
                'Item 2',
                'Item 3',
            ],
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
