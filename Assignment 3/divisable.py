lr=int(input("Enter the lower range:"))
ur=int(input("Enter the upper range:"))
for num in range(lr,ur+1):
    if num%6==0:
        print("Number dvisible by 6 is:",num)
