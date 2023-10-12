import sys

from PyQt5.QtChart import QPieSeries, QChart, QChartView
from PyQt5.QtCore import Qt, QSizeF
from PyQt5.QtGui import QFontMetrics, QPainter
from PyQt5.QtWidgets import QGraphicsWidget, QGraphicsLinearLayout, QApplication, QSizePolicy


class CustomLegendItem(QGraphicsWidget):

    def __init__(self, label, color, parent=None):
        super().__init__(parent)
        self.m_label = label
        self.m_color = color
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.setMinimumHeight(20)

    def sizeHint(self, hint, size=QSizeF()):
        if hint == Qt.PreferredSize:
            fm = QFontMetrics(self.font())
            textSize = fm.size(Qt.TextSingleLine, self.m_label)
            return QSizeF(textSize.width() + 30, 20)
        return super().sizeHint(hint, size)

    def paint(self, painter, option, widget=None):
        rect = self.boundingRect()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.m_color)
        painter.drawRect(rect.topLeft().x() + 15,
                         rect.topLeft().y() + 5, 15, 15)

        painter.setPen(Qt.white)
        painter.setFont(self.font())
        painter.drawText(
            rect.adjusted(45, 0, 0, 0), Qt.AlignVCenter, self.m_label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    series = QPieSeries()
    series.append("online devices", 1)
    series.append("offline devices", 10)

    chart = QChart()
    layout = QGraphicsLinearLayout(Qt.Vertical)

    # Add custom legend items
    for slice in series.slices():
        label = slice.label()
        color = slice.color()
        item = CustomLegendItem(label, color)
        layout.addItem(item)

    chart.addSeries(series)
    chart.legend().setAlignment(Qt.AlignBottom)
    chart.legend().setLayout(layout)

    chartView = QChartView(chart)
    chartView.setRenderHint(QPainter.Antialiasing)
    chartView.show()
    sys.exit(app.exec_())
