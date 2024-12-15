import math
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum+=math.pow(i,2)/i
print("The sum of the series is:",sum)
