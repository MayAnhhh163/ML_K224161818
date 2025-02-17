from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowExt import MainWindowEx

app=QApplication([])
myWindow=MainWindowEx()
myWindow.setupUi(QMainWindow())
myWindow.show()
app.exec()