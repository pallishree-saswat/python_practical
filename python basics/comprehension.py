""" 
comprehension is a method to create data structure in python
in single line

 """

#  list of squares till 10

a = []
for i in range(10):
    a.append(i**2)

print(a)    

# list comprehension

b = [i**2 for i in range(10)]
print(b)

# square of all even num
c = [ i**2 for i in range(10) if i % 2 == 0]
print(c)

# dict comprehension

d = { i:i**2 for i in range(10) if i % 2 == 0}
print(d)

# set comprehension

e = {i**2 for i in range(10) if i % 2== 0}

print(e)