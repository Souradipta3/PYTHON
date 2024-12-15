num=int(input("Enter a number:"))
count=0
for n in range(2,int(num/2)+1):
    if num%n==0:
        count+=1
if count>=2:
    print("Composite number")
else:
    print("Prime number")  
