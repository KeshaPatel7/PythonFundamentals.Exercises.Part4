# The program prints each number from 1 to 100 to a new line.
def num():
    n=1
    while n <= 100:
        print(n)
        n=n+1

# if the number is a multiple of 3, print "Fizz" instead of the number.
def num1():

    for i in range(1, 100):
        if i % 3 == 0:
            print(str(i))
        elif i % 5 == 0:
            print(str(i))
        else:
            i % 3 == 0 and i % 5 == 0
            print(str(i)+"FizzBuzz")
num1()












num()


