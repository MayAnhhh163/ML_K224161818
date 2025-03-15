from ML_K224161818.Salesmanagement.libs.connector import MySQLConnector
from ML_K224161818.Salesmanagement.models.nhanvien import NhanVien


class NhanVienConnector(MySQLConnector):
    def dang_nhap(self,username,password):
        cursor=self.conn.cursor()
        sql=('select * from nhanvien where username = %s and password=%s')
        val=(username,password)
        cursor.execute(sql, val)
        dataset = cursor.fetchone()
        nv=None #giả sử kh tìm thấy nhân viên đúng theo username và password
        if dataset != None:
            id, manhanvien, tennhanvien, username, password, isdeleted = dataset
            #vào đc đây tức là có nvien
            nv=NhanVien(id,manhanvien, tennhanvien, username, password, isdeleted)
        cursor.close()
        return nv #Null: đăng nhập thất bại