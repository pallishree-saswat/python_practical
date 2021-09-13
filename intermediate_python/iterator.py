
# make your own iterable class
class yrange:
    # n is the number upto I want
    def __init__(self, n):
        self.i = 0
        self.n = n
# this method makes our class iterable

    def __iter__(self):
        return self
# this is for iterator

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


for x in yrange(5):
    print(x)


# inbuilt iter() -- iterator in python

x = [1, 2, 3, 4, 5]
x_iter = iter(x)
print(x_iter)

print(next(x_iter))
print(next(x_iter))


# Other iterators na diterable objects in python
# list
a = [1, 2, 3, [4, 5], 6, 7, 8]
for x in a:
    print(x)

# dictonary
b = {"name": "jatin", "last_name": "gatiyal", "marks": 90}
for x in b:
    print(x)
# on dict we will get keys, on which we can iterate


# iterate over a file
for line in open("./word.txt", "r"):
    print(line)

# ".".join() function joins the strings with "."
c = ".".join(["a", "b", "c", "d"])
print(c)

k = list("jatin")
print(k)
# return each character

l = [1, 2, 3, 4]
n = sum(l)
print(n)
# iterate over the list and return the sum
