#sử dụng vòng lặp while để đoán số hoặc chuỗi
#người dùng sẽ nhập vào một giá trị và vòng lặp while sẽ tiếp tục yêu cầu người dùng nhập lại cho đến khi giá trị đúng được nhập
secret_value = "minhdzai"                       #giá trị bí mật cần đoán
hint = "tên anh và vẻ ngoài của anh"            #gợi ý cho người dùng
guess = ""                                      #biến lưu giá trị người dùng nhập vào, ban đầu là chuỗi rỗng vì user chưa nhập gì
guess_count = 0                                 #biến đếm số lần đoán

while guess != secret_value:                    #miễn là giá trị người dùng nhập vào khác với giá trị bí mật thì vòng lặp tiếp tục
    guess = input(f"Đoán giá trị bí mật: ")     #yêu cầu người dùng nhập giá trị đoán
    guess_count += 1                            #tăng biến đếm số lần đoán lên 1
    if guess != secret_value:                   #nếu giá trị người dùng nhập vào vẫn chưa đúng
        print("Đoán sai, thử lại!")             #in ra thông báo đoán sai
        print("-------------------------")      #in ra dòng phân cách
    if guess == secret_value:                   #nếu giá trị người dùng nhập vào đúng với giá trị bí mật
        break                                   #thoát khỏi vòng lặp while
    if guess_count >=5:                         #nếu người dùng đã đoán 4
        print("Bạn đã đoán sai nhiều lần rồi đó!")  #in ra thông báo nhắc nhở người dùng
        break                                   #thoát khỏi vòng lặp while
                                                #ở đây để >=5 rồi ,ới để >=3 là để tránh trg hợp in lần thứ 5 vẫn in gợi ý
    if guess_count >= 3:                        #nếu người dùng đã đoán 3
        print(f"Gợi ý: {hint}")                 #in ra gợi ý để giúp người dùng đoán đúng
    
if guess == secret_value:                       #nếu giá trị người dùng nhập vào đúng với giá trị bí mật
    print("giỏi lm con trai của t")             #in ra thông báo chúc mừng
else:
    print(f"Giá trị bí mật là: {secret_value}") #in ra giá trị bí mật nếu người dùng đoán sai quá nhiều lần