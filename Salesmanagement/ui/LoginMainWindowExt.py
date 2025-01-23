from PyQt6.QtWidgets import QMessageBox, QMainWindow

from Salesmanagement.models.nhanvienconnector import NhanVienConnector
from Salesmanagement.ui.LoginMainWindow import Ui_MainWindow
from Salesmanagement.ui.MainProgramMainWindowExt import MainProgramMainWindowExt


class LoginMainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.nvconnector=NhanVienConnector()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_dangnhap.clicked.connect(self.xuly_dangnhap)

    def xuly_dangnhap(self):
        username=self.lineEdit_username.text()
        password=self.lineEdit_password.text()
        #giả lập đăng nhập (hôm sau truy vấn thật trong CSDL)
        #Goij kết nối đăng nhập trong MySQL
        self.nvconnector.connect()
        self.nvlogin=self.nvconnector.dang_nhap(username,password)
        if self.nvlogin!=None:
            self.MainWindow.hide()
            self.mainwindow = QMainWindow()
            self.myui = MainProgramMainWindowExt()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        else:
            self.msg=QMessageBox()
            self.msg.setWindowTitle("Login thất bại")
            self.msg.setText("Bạn đăng nhập thất bại.\nKiểm tra lại thông tin đăng nhập")
            self.msg.setIcon(QMessageBox.Icon.Critical)
            self.msg.show()