from PyQt6.QtWidgets import QApplication, QMainWindow

from ML_K224161818.Blog56.UI.MainWindowEx import MainWindowEx

qApp=QApplication([])
qmainWindow=QMainWindow()
window=MainWindowEx()
window.setupUi(qmainWindow)
window.show()
qApp.exec()