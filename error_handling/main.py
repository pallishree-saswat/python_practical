# try and except

try:
    # a = int("sivay")
    print(10/0)
except ZeroDivisionError:
    print("You are trying to divide by zero")
except ValueError:
    print("value error occured")


try:
    print(10/0)
except Exception as e:
    print(type(e))
    print(str(e))

try:
    print(10/0)
except:
    print("error in your code")


# raise error means throw errors

try:
    raise Exception("my custom error")
except Exception as e:
    print(e)


# custom error class
# We have to give argument as baseExpection arg to accept args
class MyException(Exception):
    # initialize when error occur, we can give message at that time and store that msg in self
    def __init__(self, message):
        self.message = message

    def __str__(self):           # while stringify the message we can just stringify the message and return that message as custom error
        return self.message


try:
    raise MyException("some erroe")
except Exception as e:
    print(e.message)


# try,except,else,finally
# finally block will be always execute
# else block will only execute when try block is not returning anything
# finnaly blcok is written for cleanup
def func():
    try:
        return 1
    except:
        return 2
    finally:
        return 4


a = func()
print(a)


try:
    print("hello")
except:
    print("hey")
else:
    print("hii")
finally:
    print("hola")


# with statement is used when we have predefined cleanup action
# try to open a file

try:
    file = open("file.txt", "r")
    print(file.read())
except Exception as e:
    print(e)
finally:
    file.close()    


with open("file.txt","r") as file:
    print(file.read())

