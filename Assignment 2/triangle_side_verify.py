side1=int(input("Enter the 1st side length:"))
side2=int(input("Enter the 2nd side length:"))
side3=int(input("Enter the 3rd side length:"))
sum1=side1+side2
sum2=side2+side3
sum3=side3+side1
if(sum1>side3 and sum2>side1 and sum3>side2):
    print("Triangle can be formed.")
else:
    print("Triangle cannot be formed.")
