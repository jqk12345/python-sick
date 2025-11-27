# DICTIONARY - TỪ ĐIỂN
#   KEY      | VALUE
#------------|--------------|
#|  HELLO    | "Xin chào"   |
#------------|--------------|
#|  GOODBYE  | "Tạm biệt"   |
#------------|--------------|
#|  MORNING  | "buổi sáng"  |
#------------|--------------|
#|  BREAD    | "bánh mì"    |
#------------|--------------|
#|  COFFEE   | "cà phê"     |
#------------|--------------|

#tạo một dictionary có tên english_to_vietnamese với các cặp key-value như trên
#cách tạo 1 dictionary trong python là dùng dấu ngoặc nhọn {}
english_to_vietnamese = {
    "hello": "xin chào",                #chú ý: mỗi 1 key phải là duy nhất trong dictionary k thể có 2 key giống nhau nhưng value khác nhau
    "goodbye": "tạm biệt",              #nếu có 2 key giống nhau thì key sau sẽ ghi đè lên key trước
    "morning": "buổi sáng",             #ví dụ: "hello": "hi" sẽ ghi đè lên "hello": "xin chào"
    "bread": "bánh mì",                 #key và value trong dictionary có thể là bất kỳ kiểu dữ liệu nào: số, chuỗi, list, tuple, thậm chí là dictionary khác
    "coffee": "cà phê"                  #ở đây key là chuỗi và value cũng là chuỗi và giá trị cuối k có dấu phẩy    
}

#truy cập giá trị trong dictionary thông qua key
print(english_to_vietnamese["hello"])       #in ra giá trị của key "hello" trong dictionary english_to_vietnamese
                                            #kết quả: xin chào
print("--------------------------------------------------------------------------------------------------------------------------------")

#thay thì dùng [] để truy cập giá trị trong dictionary thì có thể dùng phương thức get()
print(english_to_vietnamese.get("goodbye")) #in ra giá trị của key "goodbye" trong dictionary english_to_vietnamese
                                            #kết quả: tạm biệt
print("--------------------------------------------------------------------------------------------------------------------------------")

#1 điều hay ở get() là nếu key không tồn tại trong dictionary thì sẽ trả về giá trị None thay vì báo lỗi như khi dùng [] và t có thể yêu cầu trả về giá trị mặc định nếu key không tồn tại
print(english_to_vietnamese.get("afternoon", "Không tìm thấy từ này"))  #in ra giá trị của key "afternoon" trong dictionary english_to_vietnamese
                                                                        #vì key "afternoon" không tồn tại nên sẽ trả về giá trị mặc định "Không tìm thấy từ này"

#chú ý: +các key trong dictionary là phân biệt chữ hoa và chữ thường
#       +các key k nhất thiết phải là chuỗi mà có thể là bất kỳ kiểu dữ liệu nào miễn là nó là immutable(ko thể thay đổi) như số, tuple, v.v.
#       +dictionary là không có thứ tự nên k thể truy cập giá trị thông qua chỉ số vị trí như list hay tuple