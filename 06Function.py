# -*- coding:utf-8 -*-
print(help(abs))
print(abs(-100))
print(max(1,2,4,5,-100,200))
print(type(int('123')))
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x
print(type(my_abs))
print(my_abs(-100))
def nop():
    pass
print(nop)
def power(x):
    return x*x
print(power(5))
def power(x,n=3):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5,4))
print(power(5))

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc(1,2,3))