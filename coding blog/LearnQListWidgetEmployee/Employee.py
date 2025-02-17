
class Employee:
    def __init__(self,name,email,gender):
        self.name=name
        self.email=email
        self.gender=gender

###hiển thị thông tin dữ liệu của đối tượng lên giao diện
    def __str__(self):
        if self.gender==True:
            return self.name+" - "+self.email +"(Woman)"
        else:
            return self.name + " - " + self.email + "(Man)"