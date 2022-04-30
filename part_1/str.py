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

