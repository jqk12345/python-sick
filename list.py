#Khá khó và quan trọng
list = ["Minh", "Buổi", "To", 290, "cm", True]  #tạo 1 list có tên là list gồm các phần tử là chuỗi và số nguyên
                                                #ở python trong 1 list có thể có nhiều kiểu dữ liệu khác nhau như chuỗi, số nguyên, số thực, boolean, v.v...
print(list)                                     #in ra toàn bộ list
print(list[2])                                  #truy cập phần tử đầu tiên của list (chỉ số bắt đầu từ 0)
                                                #out put sẽ là "Minh" thay vì M

#Muốn in ra 1 phần tử trong list thì chỉ cần gọi tên list + [chỉ số phần tử cần truy cập]
#Ex: muốn in ra Buổi thì chỉ cần gọi list[1]
print(list[1])                                  #out put sẽ là "Buổi"
print(list[-2])                                 #truy cập phần tử thứ 2 từ cuối list (chỉ số âm bắt đầu từ -1)
                                                #output sẽ là "cm"
                                                #"Minh", "Buổi", "To", 290, "cm", True
                                                #  0       1      2     3     4     5
                                                #  0      -5     -4    -3    -2    -1

print(list[1:4])                                #truy cập các phần tử từ chỉ số 1 đến chỉ số 3 (chỉ số 4 không được tính)
                                                #output sẽ là ['Buổi', 'To', 290]
                                                #cú pháp: list[số lấy:số dừng + 1]
                                                #nếu list[a:] thì sẽ lấy từ chỉ số a đến cuối list

#cách thay đổi giá trị phần tử trong list
list[1] = "Cặc"                                 #thay đổi giá trị phần tử đầu tiên của list từ "Buổi" thành "Cặc
print(list)                                     #in ra toàn bộ list sau khi thay đổi