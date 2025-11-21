print(2*5-11)                           # in ra 2*5=10; 10-11=-1

print(-1.3444)                          # in ra -1.3444 (khác vs C/C++ or java thì python ko phân biệt số thực và số nguyên)

num = 290
print(num)                              # in ra 290
print(str(num)+"cm là độ dài con c t")  # chuyển số thành chuỗi và nối với "cm" in ra "290cm"
#hoặc dùng f-string
print(f"{num}cm là độ dài con c t")     # cũng in ra "290cm là độ dài con c t"  
                                        #!!! chú ý k thể cộng 1 số vs 1 chuỗi trực tiếp được như java mà phải chuyển số thành chuỗi trước bằng str() hoặc dùng f-string như trên
print(abs(num))                         # in ra giá trị tuyệt đối của num là 290
print(pow(num,2))                       # in ra 290 mũ 2 = 9
print(max(num,1000))                    # in ra số lớn hơn trong 2 số num và 1000 là 1000
print(min(num,1000))                    # in ra số nhỏ hơn trong 2 số num và 1000 là 290

print(round(3.4444))                    # in ra số làm tròn gần nhất của 3.4444 là 3
print(round(3.5))                    # in ra số làm tròn gần nhất của 3.5444 là 4

#cách thêm thư viện vào python
import math                             #thêm thư viện math
print(math.floor(3.9999))               #in ra số nguyên nhỏ hơn hoặc bằng 3.9999 là 3
                                        #khác vs round() là floor mặc định tròn xuống
print(math.ceil(3.0001))                #in ra số nguyên lớn hơn hoặc bằng 3.0001 là 4
                                        #khác vs round() là ceil mặc định tròn lên
print(math.sqrt(36))                    #in ra căn bậc 2 của 36 là 6.0