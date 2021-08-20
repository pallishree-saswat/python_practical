def func(a,b,*args,**kwargs):
  print(args)
  print(a)
  print(b)
  print(kwargs)


func(1,4,3,4,5,6, name="john",fruit=",mango")


a = 'lipa'
b= 'lucky'

print('{firstname}+{lastname}'.format(firstname = a, lastname=b))



print(a.split(' '))

x = input()
print(x)


z= "aabbcdssaa"
print(z.count('aa'))
print(z.count('a'))


k = "abcdabcd"
print(k.replace('a','l'))

j = "yes   "
print(j.strip() == "yes")
print(j == "yes")

