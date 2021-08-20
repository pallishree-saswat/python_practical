# list data types
""" 
it stores ordered data
its mutable
it can be accessed using index
heterogenous in nature 

 """

 



a = [1,2,3,4,5]
print(a)
print(a[1])

b = ['jatin',1,2,3,print]
print(b)
print(b[0])

print(len(a))

print(a + a)

# a[-2] second last

print(a[-2])

# taking member in list
print(1 in a)

# slice
c = [1,2,3,4,5]
# c[1:4] = [2,3,4]
print(c[1:4])

# start from 0 to 5 with jump of 2
print(c[0:5:2]) 

# reversing list in python 
print(c[::-1])

# given str is palindrome or not 

print(c == c[::-1])

# updating list 
# insert and append

k = [1,2,3,4,5]
k.insert(1, 'lucky') 
# insert lucky at index 1 
print(k)
j = [ 1,2,3,4,5]
j.append("shiv")
print(j)

# delete from list 
p = [1,2,3,4,5]
p.pop()
# remove from last
p.pop(2)
# remove by index

d = ["lucky","siv","lipa"]
d.remove("lipa")
print(d)
# remove lipa - it will remove first occurence of object

del p[0]

print(p)

# sorting list
 
 
x = [1,5,3,8,6]
sorted(x)
print(x)

y = [3,4,5,6,6,8,1]
y.sort()
print(y)

# reverse()
for i in reversed(x):
    print(i)
# reversed()

y.reverse()

print(y)


