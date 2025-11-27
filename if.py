#cách sử dụng if, elif và else trong python
#cú pháp if
a=50
b=100
if a < b:                       #nếu a nhỏ hơn b thì thực hiện khối lệnh bên dưới
    print(f"{a} nhỏ hơn {b}")   #in ra "50 nhỏ hơn 100" vì khi này a=50 và b=100

#nhưng nếu a không nhỏ hơn b thì khối lệnh bên dưới sẽ không được thực thi
a=150
if a < b:                       #nếu a nhỏ hơn b thì thực hiện khối lệnh bên dưới
    print(f"{a} nhỏ hơn {b}")   #không in gì cả vì a=150 không nhỏ hơn b=100

#vậy nên muốn kiểm tra nhiều điều kiện hơn thì dùng elif và else
elif a>b:
    print(f"{a} lớn hơn {b}")   #in ra "150 lớn hơn 100" vì a=150 lớn hơn b=100
                                #khối lệnh elif chỉ được kiểm tra nếu khối if phía trên không đúng
                                #nếu khối if đúng thì khối elif sẽ không được kiểm tra

#trong trường hợp có nhiều điều kiện để kiểm tra thì có thể dùng nhiều khối elif
#và nếu cả if và elif đều không đúng thì dùng else để thực thi khối lệnh cuối cùng
else:
    print(f"{a} bằng {b}")      #else sẽ được thực thi nếu tất cả các khối if và elif phía trên đều không đúng
                                #ở đây else sẽ không được thực thi vì khối elif đã đúng
print("--------------------------------------------------------------------------------------------------------------------------------")

#toán tử khác trong if
# and, or, not
x=200
y=50
z=100

#toán tử and
if(x>y)and(x>z):                            #toán tử and: chỉ khi hai điều kiện đều đúng thì khối lệnh if bên dưới mới được thực thi
                                            #nếu một trong hai điều kiện sai thì khối lệnh sẽ không được thực thi
    print(f"{x} là số lớn nhất")            #in ra "200 là số lớn nhất" vì x=200 lớn hơn cả y=50 và z=100

#toán tử or
if(x>y)or(z>y):                             #toán tử or: chỉ cần một trong hai điều kiện đúng thì khối lệnh if bên dưới sẽ được thực thi
                                            #chỉ khi cả hai điều kiện sai thì khối lệnh sẽ không được thực thi
    print(f"{x} hoặc {z} lớn hơn {y}")      #in ra "200 hoặc 100 lớn hơn 50" vì cả x=200 và z=100 đều lớn hơn y=50

#toán tử not
e=True                                      #gán giá trị True cho biến e
print(not e)                                #toán tử not: đảo ngược giá trị của biến e
                                            #vì e=True nên not e sẽ là False
if not(x<y):                                #toán tử not: đảo ngược điều kiện x<y
                                            #vì x=200 không nhỏ hơn y=50 nên x<y là False
                                            #nên not(x<y) sẽ là True và khối lệnh if bên dưới sẽ được thực thi
    print(f"{x} không nhỏ hơn {y}")         #in ra "200 không nhỏ hơn 50"
print("--------------------------------------------------------------------------------------------------------------------------------")