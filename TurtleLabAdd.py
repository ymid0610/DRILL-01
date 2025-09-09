def add(a,b):
    sum = a+b
    return sum

result = add(100,10)
print(result)

result = add('Hong','Gildong')
print(result)

a = 'AAA'
b = 'BBB'
a, b = b, a
x,y,z = 1,2,3
x,y,z = y,z,x
print (x,y,z)