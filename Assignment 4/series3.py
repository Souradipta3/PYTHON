import math
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum+=1/math.factorial(i+1)
print("The sum of the series is:",sum)
