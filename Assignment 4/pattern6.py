n=int(input("Enter no. of lines:"))
for i in range(0,n):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")

for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
