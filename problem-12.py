#python program to find square root of a number

#method----->01
num1=int(input("Enter a number:"))
sr=num1**(1/2)
print("The square root of a the given number is:",sr)




print("--------------------------------------------------------")
#method---->02(using math module)
import math
num=int(input("Enter a number:"))
sqrt=math.sqrt(num)
print("The square root of a the given number is:",sqrt)