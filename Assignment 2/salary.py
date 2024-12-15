BS=int(input("Enter the basic salary:"))
if(BS>=5000):
    DA=(11/100)*BS
    HRA=(20/100)*BS
    CV=500
    GS=BS+DA+HRA+CV
elif(BS>=3000 and BS<5000):
    DA=(10/100)*BS
    HRA=(15/100)*BS
    CV=400
    GS=BS+DA+HRA+CV
elif(BS<3000):
    DA=(9/100)*BS
    HRA=(10/100)*BS
    CV=300
    GS=BS+DA+HRA+CV
print("The Gross Salary is",GS)
