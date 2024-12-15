'''file = open('sample.txt', 'r') #doesn't matters whether we write 'r' in case of read only, by default it is read only.
data = file.read()
print(data)
file.close()'''

'''file = open('sample.txt', 'r')
data = file.read(5) #Reads the first 5 words of the content present in the file.
print(data)
file.close()'''

'''file = open('sample.txt', 'r')
data = file.readline() #Reads the 1st line of the content in the file
print(data)
data = file.readline() #Reads the 2nd line of the content in the file
print(data)
data = file.readline() #Reads the 3rd line of the content in the file
print(data)
data = file.readline() #Reads the 4th line of the content in the file
print(data)
file.close()'''

'''file = open('sample.txt', 'r')
data = file.readlines() #Reads all the lines together
print(data)
file.close()'''

'''with open("sample.txt","r") as file: #Both the read and write operartion ca be performed by the with statement and using with statment in this syntax helps to close the file automatically hence there is no need to close the file manually
    print(file.read()) #file.read or file.write function can also be written within the print function directly without storing it in a variable'''