#cách tạo hàm tính lũy thừa trong python
def power(base, exponent):          #hàm power nhận hai tham số: base (cơ số) và exponent (số mũ)
    #sử dụng vòng lặp for để tính lũy thừa
    result =1
    for i in range(exponent):       #lặp từ 0 đến exponent-1
        result *= base              #nhân result với base trong mỗi lần lặp
        #ví dụ: nếu base=2 và exponent=3 thì vòng lặp sẽ chạy 3 lần
        #lần 1: result = 1 * 2 = 2
        #lần 2: result = 2 * 2 = 4
        #lần 3: result = 4 * 2 = 8
        #chạy 3 lần vì chạy từ 0 đến 2 (tổng cộng 3 số: 0,1,2)
    return result                   #trả về kết quả lũy thừa

a = int(input("nhập cơ số (base): "))          #nhập cơ số từ người dùng và chuyển sang kiểu int
b = int(input("nhập số mũ (exponent): "))      #nhập số mũ từ người dùng và chuyển sang kiểu int
print(power(a,b))                              #gọi hàm power với base là a và exponent là

print(power(2,3))                              #gọi hàm power với base là 2 và exponent là 3, in ra kết quả (2^3 = 8)
