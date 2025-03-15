from ML_K224161818.Salesmanagement.libs.connector import MySQLConnector
from ML_K224161818.Salesmanagement.models.danhmuc import DanhMuc


class DanhMucConnector(MySQLConnector):
    def LayToanBoDanhMuc(self):
        cursor = self.conn.cursor()
        sql = "select * from danhmuc"
        cursor.execute(sql)
        dataset = cursor.fetchall()
        dsdm=[]
        for item in dataset:
            id=item[0]
            ma=item[1]
            ten=item[2]
            dsdm.append(DanhMuc(id,ma,ten))
        cursor.close()
        return dsdm