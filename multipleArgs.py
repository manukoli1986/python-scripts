#When we know how many arguments we need to pass
def add(x,y):
    return x+y


# print(add(4,6))


#If we do not know how many arguments we gonna have
def addition(*args):
    count=0
    for each in args:
        count += each
    return count

print(addition(3,4,5,6,7))


# **Kwargs deals with dictionary