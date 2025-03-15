from PyQt6.QtWidgets import QApplication, QMainWindow

from ML_K224161818.Salesmanagement.ui.LoginMainWindowExt import LoginMainWindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=LoginMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()