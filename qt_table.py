import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QComboBox

app = QApplication(sys.argv)

# 创建表格
table = QTableWidget(3, 2)

# 将下拉框放入表格中的第一列
for i in range(3):
    combo = QComboBox()
    combo.addItem("1")
    combo.addItem("2")
    combo.addItem("3")
    table.setCellWidget(i, 0, combo)

# 设置每一行下拉框的内容
table.cellWidget(0, 0).setCurrentIndex(0)
table.cellWidget(1, 0).setCurrentIndex(1)
table.cellWidget(2, 0).setCurrentIndex(2)

table.show()

sys.exit(app.exec_())
