#gần giống vs vòng lặp while nhưng for dùng để lặp qua một tập hợp các phần tử như list, tuple, string, hoặc range
#cú pháp for
name = "Minh Buổi To Dài 290cm"
for char in name:               #lặp qua từng ký tự trong chuỗi name
    print(char)                 #in ra từng ký tự một
print("--------------------------------------------------------------------------------------------------------------------------------")

#sử dụng for để lặp qua một list
teams = ["Real Madrid", "Barcelona", "Manchester United", "Bayern Munich"]
for team in teams:              #lặp qua từng phần tử trong list teams
    print(team)                 #in ra từng phần tử một

    print(team[1])              #truy cập ký tự thứ hai của từng phần tử trong list teams
print("--------------------------------------------------------------------------------------------------------------------------------")

#sử dụng for với hàm range()
for index in range(10):         
    print(index)                #in ra các số từ 0 đến 9 (không bao gồm 10)
print("--------------------------------------------------------------------------------------------------------------------------------")

#trg hợp nếu muốn in từ 1 đến 10 thì có thể dùng range(1,11)
# range(start, stop, step)
for i in range(1,11,2):
    print(i)                #in ra các số từ 1 đến 10 (bao gồm 1 nhưng không bao gồm 11)    
print("--------------------------------------------------------------------------------------------------------------------------------")                

#có thể sử dụng đc nhiều dạng vs for như lồng for trong for hoặc if trong for
for i in range(1,6):            #lặp từ 1 đến 5
    if i == 1:
        print(f"{i} là số đầu tiên và là phần tử {i} trong mảng")       #nếu i bằng 1 thì in ra "1 là số đầu tiên"
    else:
        print(f"{i} là phần tử thứ {i} trong mảng")                     #nếu i khác 1 thì in ra "i là phần tử thứ i trong mảng"
print("--------------------------------------------------------------------------------------------------------------------------------")