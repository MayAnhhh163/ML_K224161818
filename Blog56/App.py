from PyQt6.QtWidgets import QApplication, QMainWindow

from K224161818_ML.Blog56.UI.MainWindowEx import MainWindowEx

qApp=QApplication([])
qmainWindow=QMainWindow()
window=MainWindowEx()
window.setupUi(qmainWindow)
window.show()
qApp.exec()