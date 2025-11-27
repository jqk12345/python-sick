#chú ý: về input.py
num1 = input("nhập cho a xin 1 số: ")
num2 = input("nhập cho a xin 1 số nữa: ")

sum =num1 + num2
print(f"kết quả của {num1} + {num2} = {sum}")
#kết quả sẽ là nối chuỗi chứ k phải phép cộng số học
#vd: nhập 1 vs 2 thì output sẽ là 12 chứ k phải 3

#để thực hiện phép cộng số học thì phải chuyển kiểu dữ liệu từ string sang int
num1 = int(input("nhập cho a xin 1 số: "))
num2 = int(input("nhập cho a xin 1 số nữa: "))
sum =num1 + num2
print(f"kết quả của {num1} + {num2} = {sum}")
#hoăc
sum = int(num1) + int(num2)
print(f"kết quả của {num1} + {num2} = {sum}")

#!!!!! có thể thay int bằng float để chuyển sang số thực k cần quan tâm nó có .0 hay k vì python tự xử lý chuyện đó
#vd: nhập 1.5 vs 2.3 thì output sẽ là 3.8 còn nhập 1 vs 2 thì output sẽ là 3
sum = float(num1) + float(num2)
print(f"kết quả của {num1} + {num2} = {sum}")