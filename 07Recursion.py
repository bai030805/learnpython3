# -*- coding:utf-8 -*-

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(1))

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(10))

def mov(n,a,b,c):
    if n == 1:
        print(a ,'-->', c)



mov(1,'A','B','C')



