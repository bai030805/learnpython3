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