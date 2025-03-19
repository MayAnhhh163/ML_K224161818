from PyQt6.QtWidgets import QApplication, QMainWindow

from ML_K224161818.Midterm.UI.LoginWindowExt import LoginWindowExt

app=QApplication([])
qmainWindow = QMainWindow()
myui = LoginWindowExt()
myui.showWindow()
app.exec()