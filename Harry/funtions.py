'''def greet(name):
    print("Good morning, "+ name)
greet("RAJ")

def sum(val1,val2):
    print("Sum is ", val1+val2)
sum(5,10)'''

'''def add(n):
    for i in range(0,n-1):
        return n*(n+1)/2
n=int(input("Enter a number:"))
print("The sum is: ",add(n))'''

n=int(input("Enter a number:"))
def table(n):
    for i in range(0,10):
        return n*i
for i in range(0,10):
    print(n, 'x', i, '=', table(n))
