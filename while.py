#vòng lặp while trong python
#while dùng để lặp lại một khối lệnh miễn là điều kiện còn đúng thì vòng lặp sẽ tiếp tục thực hiện
i=1                         #khởi tạo biến i với giá trị ban đầu là 1
while i<10:                 #miễn là i còn nhỏ hơn 10 thì vòng lặp while còn chạy
    print("đm mày")         #in ra "đm mày"
    i += 1                  #tăng giá trị của i lên 1 sau mỗi lần lặp
                            #nếu k có dòng i += 1 thì vòng lặp while sẽ chạy mãi mãi vì i luôn bằng 1 và điều kiện i<10 luôn đúng
print("vòng lặp kết thúc")  #in ra "vòng lặp kết thúc" khi vòng lặp while kết thúc (i không còn nhỏ hơn 10 nữa)
print("--------------------------------------------------------------------------------------------------------------------------------")