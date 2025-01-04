class Product:
    def __init__(self, id=None, name=None,price=None): #tạo thuộc tính trong lớp
        self.id=id
        self.name=name
        self.price=price

    def __str__(self): #chọn hiển thị những cột (thuộc tính) cần thiết
        infor=f"{self.id}\t{self.name}\t{self.price}"
        return infor
