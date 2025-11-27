#nâng cao trong cal vs toán tử học trong python
num1= float(input("nhập số thứ nhất: "))    #chuyển input sang float để có thể nhập số thực
operator = input("nhập phép toán (+, -, *, /): ")
num2= float(input("nhập số thứ hai: "))      #chuyển input sang float để có thể nhập số thực

#sử dụng if để kiểm tra phép toán và thực hiện phép tính tương ứng
if (operator == "+"):
    print(num1+num2)
elif (operator == "-"):
    print(num1-num2)
elif (operator == "*"):
    print(num1*num2)
elif (operator == "/"):
    print(num1/num2)
else:
    print("phép toán không hợp lệ")