#check prime number

num=int(input("Enter the number:"))

if num==1:
  print("It is bot a prime number")
if num>1:
 for i in range(2,num):
     if num%i==0:        
        print(num,"is not a prime number")
        break
 else:
        print(num,"is a prime number")
