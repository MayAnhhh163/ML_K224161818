from Salesmanagement.libs.sanphamconnector import SanPhamConnector

spc=SanPhamConnector()
spc.connect()
dssp=spc.LaySanPhamTheoMaDanhMuc(1)
print("Danh sách sản phẩm có mã danh mục = 1:")
for p in dssp:
    print(p)

#test chi tiết sp
id=2
spc.connect()
sp=spc.Lay_ChiTiet(id)
if sp!=None:
    print("*"*20)
    print(sp)

id_remove=14
spc.connect()
result=spc.Xoa_SanPham(id_remove)
if result>0:
    print("Xóa sp thành công")
else:
    print("Xóa sp thất bại")