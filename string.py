name = "Minh Buổi To Dài 290cm"
print(name.upper().isupper())   #name.upper() chuyển tất cả ký tự thành chữ hoa; 
                                #name.isupper() kiểm tra xem tất cả ký tự có phải là chữ hoa không;
                                #name.upper().isupper() trả về True

print(name.lower().islower())   #name.lower() chuyển tất cả ký tự thành chữ thường;
                                #name.islower() kiểm tra xem tất cả ký tự có phải là chữ thường không
                                #name.lower().islower() trả về True

print(len(name))                #len() trả về độ dài của chuỗi(số ký tự trong chuỗi)

print(name[5])                  #truy cập ký tự đầu tiên của chuỗi "M i n h . |B| u ổ i . T  o  .  D  à  i  .  2  9  0  c  m"
                                                                   #0 1 2 3 4 |5| 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 22

print(name.index("u"))          #trả về kí tự đầu tiên của từ "Buổi" trong chuỗi name(nếu k có kí tự thì sẽ báo lỗi ex: z hoặc là chữ d)

print(name.replace("Buổi","Cặc"))#thay thế từ "Buổi" thành từ "Cặc" trong chuỗi name