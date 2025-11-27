#mảng trong mảng 2D (2 chiều) hay còn gọi là ma trận
matrix = [
    [1,2,3],    #hàng 0    [1,2,3] 
    [4,5,6],    #hàng 1    [4,5,6]
    [7,8,9]     #hàng 2    [7,8,9]
                #       cột 0 1 2  
]

#print ma trận
#vd muốn in số 5
print(matrix[1][1])  #cấu trúc matrix[hàng][cột]  => in ra 5 vì hàng 1 cột 1 là số 5
print(matrix[2][1])  #in ra 8 vì hàng 2 cột 1 là số 8
print("--------------------------------------------------------------------------------------------------------------------------------")

#in toàn bộ ma trận
#sử dung jvongf lặp for
for row in matrix:        #duyệt từng hàng trong ma trận
    print(row)            #in ra từng hàng
print("--------------------------------------------------------------------------------------------------------------------------------")

#in từng phần tử trong ma trận
for row in matrix:             #duyệt từng hàng trong ma trận
    for column in row:         #duyệt từng cột trong hàng hiện tại
        print(column)          #in ra từng cột