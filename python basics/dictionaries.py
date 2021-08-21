""" 
a data stucture which store data in key value pairs
not ordered
can access a data value by its keys
culy braces {}

 key is a string
 value can be any data types

 """

a= {
    "name":"Siv",
    "marks":100,
    "subjects":["eng","math"],
    "friends":{
        "ram":"android"
    }
} 

print(a["friends"])
print(a)

# when we iterate a dictionary bydefault we get all keys available in dict

for key in a:
    print(key)


# operations on dictonary
# items() will create a touple of each key value pair
for item in a.items():
    print(item)
    
    
# now touple is iterable we can destructure key value from it

for key,value in a.items():
    print(key ," =>",value) 


#keys()
for key in a.keys():
    print(key)


# values -- show error if key has no value
for value in a.values():
    print(value)

#get()
# return none if key has no value 

print(a.get("name"))
# clear()

# a.clear()

""" challenge  a program to store student  """
students = []

n = int(input())

for _ in range(n):
    roll = int(input())
    name = input()
    branch = input()
    students.append({
        "roll-no":roll,
        "name":name,
        "branch":branch
    })

    
print(students)


""" 
Keys in the dictonary can be any immutable
Data structure
 as tuple is immutable we can take a tuple as keys in dict

 """

q = {
    (1,2) : "Lucky"
}

print(q)