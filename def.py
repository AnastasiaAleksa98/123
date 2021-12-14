import math

#def foo():
  #  print("Hello function")
    # return True
 #   return 123

#foo()
#print(foo())

#def bar(a = 100, b = 100):
 #   return a + b

#print(bar(55, 88))
#print(bar(55))
#print(bar())

#print (2**100000000)

x = 0
y = 0
o = "+"
TITLE = "ghkl"

def plus(x, y):
    return x + y 

def minus(x, y):
    return x - y

def div(x, y):
    return x /y
def sin(x):
    return math.sin(x)

#x = int(input('Enter x = '))
#y = int(input('Enter y = '))
#o = input('Enter operation = ')

#if o == '+':
 #   print(plus (x, y))
#elif o == '-':
   # print(minus (x, y))
#elif o == '/':
 #   print(div(x, y))
#else:
  #  print('Bed operation')


# x = int(input('Enter x = '))
#y = int(input('Enter y = '))
#o = input('Enter operation = ')

def menu():
    print("Operation:")
    print("Add: +")
    print("Subtr: -")
    print("Div: /")
    print()
    print('Exit: q')
    return input ('your choice (+ | - | / | q):')

while True:
    o = menu()
    if o == 'q':
        print('Thank you for using ' + TITLE + '!')
        break
    x = int(input('Enter x = '))
    if o != 's':
        y = int(input('Enter y = '))

    match o :
        case'+': 
            print(plus (x, y))
        case  '-':
            print(minus (x, y))
        case '/':
            print(div(x, y))
        case 's':
            print(sin (x))
        case _: 
            print('Bed operation')