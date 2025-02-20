from PyQt6.QtWidgets import QApplication, QMainWindow
from HousingPricePrediction.conding_pyqt6.HousingPricePredictonMainWindowExt import HousingPricePredictionMainWindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=HousingPricePredictionMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()