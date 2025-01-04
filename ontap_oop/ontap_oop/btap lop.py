from K22416C.ontap_oop.FileFactory import FileFactory
from K22416C.ontap_oop.product import Product
ff = FileFactory()
dataset = ff.readData("mydataset.json", Product)

#Viết hàm lọc ra các sản phẩm có giá từ a tới b
def filter_products_by_price(dataset, a, b):
    filtered_products = []
    for product in dataset:
        if a <= product.price <= b:
            filtered_products.append(product)
    return filtered_products

a = float(input("Nhập giá tối thiểu: "))
b = float(input("Nhập giá tối đa: "))
filtered_products = filter_products_by_price(dataset, a, b)

print(f"Danh sách sản phẩm có giá từ {a} tới {b}:")
for product in filtered_products:
    print(product)

#Xoá tất cả các sản phẩm có giá nhỏ hơn x
def remove_products_below_price(dataset, x):
    filtered_products = []
    for product in dataset:
        if product.price >= x:
            filtered_products.append(product)
    return filtered_products

x = float(input("Nhập giá tối thiểu để giữ lại sản phẩm: "))
dataset = remove_products_below_price(dataset, x)

print(f"Danh sách sản phẩm sau khi xóa các sản phẩm có giá nhỏ hơn {x}:")
for product in dataset:
    print(product)