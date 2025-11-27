coordinates = (10,20)   #tạo một tuple có tên coordinates với hai phần tử 10 và 20 (x,y)
                        #tương tự list thì tuple cũng có thể truy cập các phần tử thông qua chỉ số vị trí
                        #(10,20)
                        # 0  1
                        #đặc biệt tuple là không thể thay đổi được (immutable) tức là không thể thêm, xóa hoặc thay đổi các phần tử trong tuple sau khi nó đã được tạo
                        #vs coordinates[1] = 30  #sẽ báo lỗi TypeError: 'tuple' object does not support item assignment
                        #tuple thường được sử dụng để lưu trữ các tập hợp dữ liệu không thay đổi, như tọa độ, màu sắc, v.v.

print(coordinates[0])   #truy cập phần tử đầu tiên của tuple coordinates (10)
