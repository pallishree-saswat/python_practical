""" 
Sets are unordered collection  of objects(data)
no key value pair
all values in sets should be unique
if we give multiple same number it will store only unique values
 """


a = { 1,2,3,4,5}
print(type(a))

print(a)

b = {3,4,5,6}

# common elements
c = a.intersection(b)
# all elements of both
d = a.union(b)
# all in anot in b
e = a - b

print(c)
print(d)
print(e)


x = {1,2,2,3,3,4,2,1,3}
print(x)

# how to deduplicate a list

y = [1,2,3,4,2,2,2,1,1,3] 

print(list(set(y)))