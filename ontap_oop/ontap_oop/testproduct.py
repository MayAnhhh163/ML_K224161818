from K22416C.ontap_oop.FileFactory import FileFactory
from K22416C.ontap_oop.product import Product
p1=Product(1,"Coca",100)
print(p1)
dataset=[]
dataset.append(p1)
dataset.append(Product(2,"Pepsi",30))
dataset.append(Product(3,"Sting",40))
dataset.append(Product(4,"Aquq",50))
dataset.append(Product(5,"RedBull",60))
print("Danh sách sản phẩm:")
for product in dataset:
    print(product)

#Lưu mới
while True:
    id=int(input("Nhập mã:"))
    name=input("Nhập tên:")
    price=float(input("Nhập giá:"))
    p=Product(id,name,price)
    dataset.append(p)
    ask=input("Nhập tiếp không? (c/k):")
    if ask=='k':
        break
print("Danh sách sản phẩm sau khi nhập:")
for product in dataset:
    print(product)

#Gọi chức năng chụp ảnh đối tượng xuống ổ cứng
#Chụp thành đinh dạng Json
ff=FileFactory()
ff.writeData("mydataset.json",dataset)
