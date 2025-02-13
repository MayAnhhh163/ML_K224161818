from Salesmanagement.libs.connector import MySQLConnector
from Salesmanagement.models.sanpham import SanPham


class SanPhamConnector(MySQLConnector):
    def LaySanPhamTheoMaDanhMuc(self,iddm):
        cursor = self.conn.cursor()
        sql = "select * from sanpham where iddanhmuc=%s"
        val=(iddm,)
        cursor.execute(sql,val)
        dataset = cursor.fetchall()
        dssp = []
        for item in dataset:
            id = item[0]
            masanpham= item[1]
            tensanpham= item[2]
            soluong= item[3]
            dongia= item[4]
            iddanhmuc= item[5]
            dssp.append(SanPham(id,masanpham,tensanpham,soluong,dongia,iddanhmuc))
        cursor.close()
        return dssp

    def Lay_ChiTiet(self, id):
        cursor=self.conn.cursor()
        sql="select * from sanpham where id = %s"
        val=(id,)
        cursor.execute(sql,val)
        dataset = cursor.fetchone() #lấy 1 dòng
        sp=None
        if dataset != None:
            id,ma,ten,sl,gia,iddm = dataset
            sp=SanPham(id,ma,ten,sl,gia,iddm)
        cursor.close()
        return sp

    def Xoa_SanPham(self,id):
        cursor = self.conn.cursor()
        sql = "delete from sanpham where id=%s"
        val = (id,)
        cursor.execute(sql, val)
        self.conn.commit()
        #số dòng dữ liệu bị ảnh hưởng:
        result=cursor.rowcount
        cursor.close()
        return result
