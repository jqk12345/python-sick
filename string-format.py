#trong number.py và string.py có sử dụng f-string để định dạng chuỗi
num=290
text = "{}cm độ dài con c t"
print(text.format(num))  # in ra "290 độ dài con c t" bằng cách dùng phương thức format() của chuỗi
                         #đây là 1 cách định dạng chuỗi trong python nhưng có thể dùng như f-string trong number.py và string.py cho tiện và dễ nhớ

#Ưu điểm của format() so với f-string là có thể tái sử dụng chuỗi định dạng nhiều lần với các giá trị khác nhau
#ex:
text1 = "{}cm độ dài con c t, {}cm là dộ dài con c ngựa"
cact = 290
cacng = 50
print(text1.format(cact,cacng))  #in ra "290cm độ dài con c t, 50cm là độ dài con c ngựa"

#hoặc có thể dùng chỉ số vị trí trong format()
text2 = "{1}cm độ dài con c ngựa, {0}cm là độ dài con c t"
print(text2.format(cact,cacng))  #in ra "50cm độ dài con c ngựa, 290cm là độ dài con c t" mặc dù format(cact,cacng) nhưng do chỉ số vị trí nên vẫn in đúng giá trị mong muốn
