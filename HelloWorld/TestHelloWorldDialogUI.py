from PyQt6.QtWidgets import QApplication, QDialog
from HelloWorldDialog import Ui_Minhe_HelloWorld

app=QApplication([])
dialog=QDialog()
window = Ui_Minhe_HelloWorld()
window.setupUi(dialog)
dialog.show()
app.exec()