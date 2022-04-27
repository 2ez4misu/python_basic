#các kiểu dữ liệu số:

#Số nguyên: 
a = 10
print(type(a))

#Số thực:
b = 10.7
print(type(b))
# số chữ số đằng sau dấu phẩy mặc định là 15 số.
c = 10/3
print(c) 

#phân số:
from fractions import Fraction
Fraction(10,7)
print(Fraction(10,7))
print(type(Fraction(10,7)))

#số phức:
d = complex(3,1)
print(d)
print(type(d))
