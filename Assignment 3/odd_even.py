m=int(input("Enter the lower range:"))
n=int(input("Enter the upper range:"))
for i in range(m,n+1):
    if i%2==0:
        print(i,"is a even number.")
    else:
        print(i,"is a odd number.")
