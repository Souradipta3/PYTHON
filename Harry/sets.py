'''a={1,2,3,4,5}
print(type(a))
print(a)

b={3,1,1,3} #data cannot be repeated in case of sets
print(b)

c={} # it denotes empty dictionary not sets
print(type(c)) 

d=set()
print(type(d))'''

e=set()
e.add(0)
e.add(9)
e.add(1) 
e.add(1) #Adding same value repeatedly does not change the set
e.add(7)
e.add(2)
#e.add([1,3,9]) List cannot be added in sets
#e.add({2,4,8}) Dictionary cannot be added in sets

'''e.remove(7)
print(e)'''

'''print(len(e)) #Prints the length of the set
print(e.pop()) #Removes any random value/data from the set
print(e.clear()) #Clears the set fully and makes it empty'''

'''print(e.union({3,4}))
print(e.intersection({1,2}))'''
