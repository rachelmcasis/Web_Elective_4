#calculator exercise

#functions


def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

print()
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print()
z = input("what's your choice?: ")
print()
x = int(input("Enter the first value: "))
y = int(input("Enter the second value: "))
print()

if z=='1':
    print (x,"+",y, "=", add(x,y))
elif z=='2':
    print(x,"-",y, "=", subtract(x,y))
elif z=='3':
    print(x,"*",y, "=", multiply(x,y))
elif z=='4':
    print(x,"/",y, "=", divide(x,y))
else:   print("Your choice is not here")

print()
print("Would you like to calculate again? ")
a = input("Yes or No: ")

