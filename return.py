#cách dùng lênh return trong hàm để trả về giá trị từ hàm
def add(a,b):
    return a + b        #trả về giá trị tổng của a và b
                        #khác vs việc gọi sum và in ra giá trị sum
                        #thì return sẽ trả về giá trị để có thể sử dụng nó ở nơi khác
                        # khác vs return của java hay là C/C++ là return trong python có thể trả về nhiều giá trị cùng lúc dưới dạng tuple
                        #nếu như k có return thì hàm sẽ trả về giá trị None

print(add(5, 10))       #gọi hàm add với tham số 5 và 10, in ra kết quả trả về (a+b) là 15
print("--------------------------------------------------------------------------------------------------------------------------------")

#có thể gán giá trị vs hàm có return
result = add(20, 30)    #gán giá trị trả về của hàm add(20,30) cho biến result
print(result)           #in ra giá trị của biến result (50)
print("--------------------------------------------------------------------------------------------------------------------------------")

#đặc biệt những câu lệnh sau return trong hàm sẽ k được thực thi. hàm sẽ kết thúc khi gặp lệnh return
def multiply(a, b):
    return a * b                                #trả về giá trị tích của a và b
    print("This line will not be executed")     #dòng này sẽ không được thực thi vì nó nằm sau lệnh return

print(multiply(5, 4))                           #gọi hàm multiply với tham số 5 và 4, in ra kết quả trả về (a*b) là 20
print("--------------------------------------------------------------------------------------------------------------------------------")