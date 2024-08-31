#program to calculate and print the sums of even and odd integers of the first n natural numbers:

n=int(input("up to which natural number?"))
ctr=1
sum_even=sum_odd=0
while ctr<=n:
    if ctr%2==0:
        sum_even+=ctr
    else:
        sum_odd+=ctr
    ctr+=1
print("The sum of even integers is",sum_even)
print("The sum of odd integers is",sum_odd)