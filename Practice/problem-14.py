#swap two numbers;

x=float(input("Enter first number:"))
y=float(input("Enter second number:"))
print("Given numbers are:",x,y)

x,y=y,x #without using third variable
print("Swap numbers are:",x,y)