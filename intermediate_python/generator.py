# generators
# Simple functions or expressions used to create iterator.
# there is a method   or key for generators - yield


# generator for fibonacci

def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev+curr


gen = fib()
(print(next(gen)))
(print(next(gen)))
(print(next(gen)))
(print(next(gen)))
(print(next(gen)))
(print(next(gen)))
(print(next(gen)))


# generator expressions
# let us find the sum of squares  of first 10 numbers

generator = (x**2 for x in range(1, 11))

# this expression act like genrator we dont need to call this
# we can directly apply next method

print(type(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
