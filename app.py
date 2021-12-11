# comment 
#hell = "Hello World"
#print(hell)
#a = 22
#b = 2



a = input("Enter a =")
b = input("Enter b =")
o = '-'
if o == '+' :
    c =  int(a) + int(b)
elif o == '-':
    c =  int(a) - int(b)
elif o == '*':
    c =  int(a) * int(b)
else : 
    print ("error")
print()
print("a " + o + " b = " , c)
