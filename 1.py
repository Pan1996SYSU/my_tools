from PyQt5.QtWidgets import QApplication
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QMouseEvent
from PyQt5.QtCore import Qt


class CustomChartView(QChartView):
    def __init__(self, series, parent=None):
        super(CustomChartView, self).__init__(parent)
        self.series = series

    def mouseMoveEvent(self, event: QMouseEvent):
        super(CustomChartView, self).mouseMoveEvent(event)
        for slice in self.series.slices():
            if slice.contains(self.chart().mapToValue(event.pos())):
                slice.setToolTip(f"{slice.label()} : {slice.value()}")
            else:
                slice.setToolTip("")


if __name__ == "__main__":
    app = QApplication([])

    series = QPieSeries()
    series.append("Slice 1", 10)
    series.append("Slice 2", 20)
    series.append("Slice 3", 30)

    chart = QChart()
    chart.addSeries(series)
    chart.createDefaultAxes()
    chart.setAnimationOptions(QChart.SeriesAnimations)

    chart_view = CustomChartView(series)
    chart_view.setRenderHint(QPainter.Antialiasing)
    chart_view.setChart(chart)
    chart_view.show()

    app.exec_()
