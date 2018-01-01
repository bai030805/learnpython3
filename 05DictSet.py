dict = {1:'test1', 2:'test2', 3:'test3'}
print(dict)
print(dict[1])
dict[1] = 'test1_1'
print(dict[1])

print(4 in dict)

print(dict.get(5, -100))
dict.pop(1)
print(dict)

s = set([1,2,2,3,4])
s.add(100)
print(s)