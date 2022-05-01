#các kiến thức về chuỗi:
a = "I'm Misu"
#nói chung chuỗi đơn giản là đoạn ký tự nằm trong cặp nháy đơn '' hoặc nháy kép "" thôi.

#Escape Sequence \
#Có nhiều kiểu sử dụng:
"\a" #phát ra 1 tiếng beep
"\b" #đưa con trỏ về lại 1 khoảng trắng
"\n" #đưa con trỏ xuống dòng
"\t" #thêm 1 khoảng tab
"\'" #in ra ký tự '
"\"" #in ra ký tự "
"\\" #in ra ký tự \

#củng cố:
# 'nasdfiuqwnerp', #đúng
# "234a'adadf", #đúng
# """asd34'asdfjoaisdfadf""", #đúng
# "\", #sai
# """\""", #sai
# '' #đúng

#sự khác nhau của 
b = 69
c = '69'
#b là số int còn c là chuỗi str

str1 = '35\53ni34' 
str2 = '\\n'
str3 = "\/\/\/\\/\/"

#Chuỗi trần: để tránh \ ng ta thêm r+ chuỗi để loại ỏ tác dụng của \
print(r"hello\world")
#tác dụng chính chủ yếu để viết đường dẫn thư mục các thứ

#toán tử sử dụng được vs chuỗi trong python
Str_a = "Im Misu"
Str_b = "Come With Me"
#toán tử +
print(Str_a + Str_b)
#toán tử x
print(Str_a * 10)
#toán tử in
print("M" in Str_a)

#Indexing và cắt chuỗi
print(Str_a[3])
#kết quả trả về ký tự của vị trí thứ 4 của chuỗi là M (tính từ 0)

#cắt chuỗi chuỗi[x:y:z]
print(Str_a[3:7])
# x:y là cắt từ x đến y với bước nhảy cắt z. để trống thì mặc định là None. X = none = 0
# y = none = vị trí cuối. z = none = 1. Có thể sử dụng số âm 1 cách thông minh (tính ngược).

#ép kiểu dữ liệu:
var_a = '710'
int(var_a) #biến chuỗi var_a từ str về int. K thể chuyển nếu số dạng float
float(var_a) # biến chuỗi var_a dạng float về số float

#thay thế chữ trong chuỗi là k thể, chúng ta phải thực hiện các phương pháp cắt ghép để tạo chuỗi mới

