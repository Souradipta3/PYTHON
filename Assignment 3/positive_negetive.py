count=0
sum=0
while(1):
    num=int(input("Enter a number:"))
    if num==-1:
        break
    else:
        sum+=num
        count+=1
avg=sum/count
print("Sum is",sum)
print("Average is",avg)
