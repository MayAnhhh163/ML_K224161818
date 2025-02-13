from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem, QTableWidgetItem, QMessageBox

from Salesmanagement.libs.danhmucconnector import DanhMucConnector
from Salesmanagement.libs.sanphamconnector import SanPhamConnector
from Salesmanagement.ui.ProductMainWindow import Ui_MainWindow


class ProductMainWindowExt(Ui_MainWindow):
    def __init__(self):
        self.dmc=DanhMucConnector()
        self.dsdm=[]
        self.spc=SanPhamConnector()
        self.dssp=[]
        self.current_selected_danhmuc=None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.truyvan_danhmucsanpham()
        self.hienthi_danhmucsanpham()
        self.setupSignalAndSlot()

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

    def setupSignalAndSlot(self):
        self.listWidgetDanhMuc.itemSelectionChanged.connect(self.tai_danhsach_sanpham)
        self.tableWidgetSanPham.itemSelectionChanged.connect(self.xem_chitiet_sanpham)
        self.pushButtonXoa.clicked.connect(self.xuly_xoa)

    def tai_danhsach_sanpham(self):
        selected_index=self.listWidgetDanhMuc.currentRow()
        if selected_index<0:#chưa chọn gì
            return
        item=self.listWidgetDanhMuc.item(selected_index)
        dm=item.data(Qt.ItemDataRole.UserRole)
        self.spc.connect()
        self.dssp=self.spc.LaySanPhamTheoMaDanhMuc(dm.id)
        for p in self.dssp:
            print(p)
        self.hienthi_dssp_len_qtable()
        self.current_selected_danhmuc=dm

    def hienthi_dssp_len_qtable(self):
        #xóa dữ liệu cũ trên QTableWidget
        self.tableWidgetSanPham.setRowCount(0)
        for p in self.dssp:
            #Lấy vị trí của dòng cuối cùng +1 (tức là dòng mới)
            row_index=self.tableWidgetSanPham.rowCount()
            #thực hiện chèn mới 1 dòng vào cuối bảng
            self.tableWidgetSanPham.insertRow(row_index)
            #vì mỗi dòng có 6 cột. Ta hiển thị giá trị cho từng cột:
            cot_id=QTableWidgetItem(str(p.id))
            cot_ma=QTableWidgetItem(p.masanpham)
            cot_ten = QTableWidgetItem(p.tensanpham)
            cot_sl = QTableWidgetItem(str(p.soluong))
            cot_gia = QTableWidgetItem(str(p.dongia))
            cot_iddm = QTableWidgetItem(str(p.iddanhmuc))
            self.tableWidgetSanPham.setItem(row_index,0,cot_id)
            self.tableWidgetSanPham.setItem(row_index,1,cot_ma)
            self.tableWidgetSanPham.setItem(row_index,2,cot_ten)
            self.tableWidgetSanPham.setItem(row_index,3,cot_sl)
            self.tableWidgetSanPham.setItem(row_index,4,cot_gia)
            self.tableWidgetSanPham.setItem(row_index,5,cot_iddm)
            #setItem(row, column, item): Gán giá trị vào từng cột của dòng mới.
            if p.soluong<=20:
                cot_sl.setBackground(Qt.GlobalColor.yellow)
                cot_sl.setForeground(Qt.GlobalColor.red)

    def xem_chitiet_sanpham(self):
        selected_index=self.tableWidgetSanPham.currentRow()
        if selected_index==-1:
            return
        id=self.tableWidgetSanPham.item(selected_index,0).text()
        self.spc.connect()
        sp=self.spc.Lay_ChiTiet(id)
        if sp!=None:
            self.lineEditId.setText(str(sp.id))
            self.lineEditMa.setText(sp.masanpham)
            self.lineEditTen.setText(sp.tensanpham)
            self.lineEditSoLuong.setText(str(sp.soluong))
            self.lineEditDonGia.setText(str(sp.dongia))
            self.lineEditIdDM.setText(str(sp.iddanhmuc))

    def xuly_xoa(self):
        msg=self.lineEditId.text()+"-"+self.lineEditTen.text()
        dlg=QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác thực xóa")
        dlg.setText("Ê, muốn xóa sản phẩm ["+msg +"]hả?")
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons=QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        result=dlg.exec()
        if result==QMessageBox.StandardButton.No:
            return
        self.spc.connect()
        result=self.spc.Xoa_SanPham(self.lineEditId.text())
        if result>0:
            self.spc.connect()
            self.dssp = self.spc.LaySanPhamTheoMaDanhMuc(self.current_selected_danhmuc.id)
            self.hienthi_dssp_len_qtable()