from Salesmanagement.libs.sanphamconnector import SanPhamConnector

spc=SanPhamConnector()
spc.connect()
dssp=spc.LaySanPhamTheoMaDanhMuc(1)
print("Danh sách sản phẩm có mã danh mục = 1:")
for p in dssp:
    print(p)