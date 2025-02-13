from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem

from Salesmanagement.libs.danhmucconnector import DanhMucConnector
from Salesmanagement.ui.ProductMainWindow import Ui_MainWindow


class ProductMainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.dmc=DanhMucConnector()
        self.dsdm=[]
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.truyvan_danhmucsanpham()
        self.hienthi_danhmucsanpham()

    def showWindow(self):
        self.MainWindow.show()

    def truyvan_danhmucsanpham(self):
        self.dmc.connect()
        self.dsdm=self.dmc.LayToanBoDanhMuc()

    def hienthi_danhmucsanpham(self):
        #xóa toàn bộ dữ liệu cũ trên giao diện:
        self.listWidgetDanhMuc.clear()
        for dm in self.dsdm:
            item=QListWidgetItem()
            #ghi dữ liệu vao bộ nhớ
            item.setData(Qt.ItemDataRole.UserRole,dm)
            #hiển thị dữ liệu trên giao diện
            item.setText(dm.tendanhmuc)
            self.listWidgetDanhMuc.addItem(item)