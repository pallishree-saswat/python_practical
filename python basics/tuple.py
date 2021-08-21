""" 
iterable
unmutable

 """

a = (1,2,3,4,5)
print(a[0])

""" this is useful because args are given by user and we dont want to modify it """

def func(*args):
    print(args)

func(1,2,3,4,5,6)

b = 5
c= 6
# swap b with c

temp = b
b = c
c = temp
print(b,c)

# or 
# comma separated value reffers a tuple
x = 2,3,4,5

# cool method in python to swap

y = 10
z = 20

# left assign to change the order for assigning value
# (z,y) = (y,z)
z,y = y,z
print(y,z)

# convert a tuple to list

d = (1,2,3,4,5)
d = list(d)
print(d)

e = list("lucky")
print(e)

l = list(range(15))

print(l)


def addSubtract(a,b):
    return a+b, a-b

sum , diff = addSubtract(10,5)    
print(sum, diff)
