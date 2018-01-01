# -*- coding:utf-8 -*-
names = ['test0','test1','test2']

for name in names:
    print(name)

rangetest = list(range(5))
for i in rangetest:
    print(i)

sum = 0
for i in range(101):
    sum = sum + i
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

n = 1
while n < 100:
    if n > 10:
        break
    print(n)
    n = n + 1

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
