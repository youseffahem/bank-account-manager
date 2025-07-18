class Std:
    def __init__(self,name,age):
        self.name=name
        self.age=age

x= str(input("ENter name: "))
y=int(input("Enter age: "))
std=Std(x,y)
print(f"the student {std.name} his age = {std.age}")