a = 6
print(a)

str1 = "hello world"
print(str1)

if(a > 1):
    print("positive")
elif a == 0:
    print("zero")
else:
    print("negative")


while a > 1:
    print(a)
    a -= 1

for i in "python":
    print(i)

# range(5)
# [0,4)

for i in range(5):
    print(i)

for j in range(1, 10):
    print(j)

for k in range(1, 10, 2):
    print(k)


print("a" > "b")
print("a" != "b")
print("a" == "b")
print(54 == 10)
print(5 <= 45)
print(5 != 5)


print(2 * 5)
print(2 ** 5)
print(5 / 2)
print(12 % 5)
print(22 // 5)
print(2 + 5)
print(20 - 5)


x = 25
x += 10
print(x)

# function


def sum(num1, num2):
    print(num1 + num2)


sum(10, 20)


def display(x, times):
    for i in range(times):
        print(x)


display(5, 3)


def sum2(num1, num2):
    return(num1 + num2)


add = sum2(20, 30)
print(add)

def div(a,b):
    try:
       return a/b
    except:
        print('error')
    finally:
        print("done")

div(10,0)            
div(10,2)
p = div(20,4)
print(p)            


q = 10

def show():
    global q
    q += 10
    print(q)

show()   


def outer():
    z = 10
    print(z)
    def inner():
        nonlocal z
        z += 5
        print(z)
    inner()


outer()    

# lamda function

def add2 (a,b):
    return a+b

v = lambda a,b:a+b

d = v(1,2)
e= add2(1,2)
print(d)
print(e)