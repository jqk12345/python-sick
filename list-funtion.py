list_name = ["Minh", "Cặc", "To","Vãi"]
Lenght = [10,9,8,7]

list_name.append("Dài")         #thêm phần tử "Dài" vào cuối list list_name
print(list_name)
print("--------------------------------------------------------------------------------------------------------------------------------")

list_name.extend(Lenght)        #thêm các phần tử của list Lenght vào cuối list list_name
print(list_name)
print("--------------------------------------------------------------------------------------------------------------------------------")

list_name.insert(1,"Đzai")      #chèn phần tử "Đéo" vào vị trí chỉ số 1 của list list_name(ở đấy là giữa "Minh" và "Cặc")
print(list_name)
print("--------------------------------------------------------------------------------------------------------------------------------")

list_name.remove("Cặc")         #xóa phần tử "Cặc" khỏi list list_name
print(list_name)
print("--------------------------------------------------------------------------------------------------------------------------------")

list_name.pop()                  #xóa phần tử cuối cùng khỏi list list_name
print(list_name)
print("--------------------------------------------------------------------------------------------------------------------------------")

list_name.index("Minh")           #trả về chỉ số của phần tử "Cặc" trong list list_name
                                 #khác vs tronglist.py là tìm kết quả tại vị trí 1(là "Cặc") thì ở đây ngược lại ct sẽ trả về chỉ số của phần tử "Cặc" là 1
print(list_name.index("Minh"))   #nếu k có phần tử thì sẽ báo lỗi và hiện thông báo là ValueError: 'phần tử' is not in list    
print("--------------------------------------------------------------------------------------------------------------------------------")

print(list_name.count("Minh"))   #đếm số lần xuất hiện của phần tử "Minh" trong list list_name. Nếu phần tử không có trong list thì trả về 0
print("--------------------------------------------------------------------------------------------------------------------------------")

Lenght.sort()                    #sắp xếp các phần tử trong list list_name theo thứ tự tăng dần (theo bảng chữ cái đối với chuỗi và theo giá trị số đối với số)
print(Lenght)
print("--------------------------------------------------------------------------------------------------------------------------------")

list_name.reverse()             #đảo ngược thứ tự các phần tử trong list list_name
print(list_name)
print("--------------------------------------------------------------------------------------------------------------------------------")

list_name2=list_name.copy()          #tạo một bản sao của list list_name và gán nó cho list list_name2
print(list_name2)
print("--------------------------------------------------------------------------------------------------------------------------------")

list_name.clear()               #xóa tất cả phần tử khỏi list list_name
print(list_name)                #in ra list_name sau khi đã xóa tất cả phần tử
print("--------------------------------------------------------------------------------------------------------------------------------")