#hàm def
def say_hello():
    print("lô con c")

print("bắt đầu")
say_hello()                     #gọi hàm say_hello để in ra "lô con c"
print("kết thúc")
print("--------------------------------------------------------------------------------------------------------------------------------")

#hàm với tham số
def hello(name):
    print(f"lô con c {name}")  #in ra "lô con c " kèm theo tên được truyền vào hàm
                                #nó có cấu trúc giống f-string trong string.py và number.py

print("bắt đầu")
hello("Minh")                   #gọi hàm hello với tham số "Minh"
hello("nòn")                    #gọi hàm hello với tham số "nòn"
print("kết thúc")
print("--------------------------------------------------------------------------------------------------------------------------------")

#đặc biệt hàm có thể chứ nhiều tham số
def infor(name, age):
    print(f"Tên tôi là {name}")  #in ra "Tên tôi là {name}" với name
    print(f"Tôi {age} tuổi")     #in ra "Tôi {age} tuổi" với age

print("bắt đầu")
infor("Minh", 20)               #gọi hàm infor với tham số "Minh" và 20
infor("nòn", 18)                #gọi hàm infor với tham số "nòn" và 18
print("kết thúc")
print("--------------------------------------------------------------------------------------------------------------------------------")