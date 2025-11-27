#cách nhập dữ liệu từ bàn phím của python
name= input("Xin cái tên: ")
age = input("Xin cái tuổi: ")
if(age.isdigit() == False):
    print("Vui lòng nhập số hợp lệ cho tuổi.")
    exit()
print(f"xin chào {name}, bạn {age} tuổi")
#!!!! chú ý: input() luôn là giá trị String dù nhập số hay chữ