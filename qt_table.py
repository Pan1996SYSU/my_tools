import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QComboBox

app = QApplication(sys.argv)

# 创建表格
table = QTableWidget(4, 2)

# 将下拉框放入表格中的第一列
for i in range(4):
    combo = QComboBox()
    combo.addItem("Option {}-1".format(i))
    combo.addItem("Option {}-2".format(i))
    combo.addItem("Option {}-3".format(i))
    table.setCellWidget(i, 0, combo)

table.show()

sys.exit(app.exec_())
