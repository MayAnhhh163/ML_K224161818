from ML_K224161818.Salesmanagement.libs.danhmucconnector import DanhMucConnector

dmc=DanhMucConnector()
dmc.connect()
dsdm=dmc.LayToanBoDanhMuc()
print("Danh mục sản phẩm của hệ thống:")
for dm in dsdm:
    print(dm)
