#-*- coding:utf-8 -*-

age = 12
if age > 18:
    print('your age is',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')

age = 3
if age > 6:
    print('teenager')
elif age > 18:
    print('adult')
else:
    print('kid')

birthyear = int(input('birth year:'))

if birthyear < 2000:
    print('00前')
else:
    print('00后')

height = 1.75
weight = 80.5
bmi = weight/(height*height)

if bmi < 18.5:
    print('too light')
elif bmi > 18.5 and bmi < 25:
    print('normal')
elif bmi > 25 and bmi < 28:
    print('too heavy')
elif bmi > 28 and bmi < 32:
    print('fat')
else:
    print('too fat')

