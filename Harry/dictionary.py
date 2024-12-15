mydict = {
    "Generator":"Bramha",
    "Operator":"Bhisnu",
    "Destroyer":"Maheswar",
    "GOD":["Bramha","Bhisnu","Maheswar"],
    "Main God":[1,2,3],
    "Similar God":{"Thakur":"Ma"},
}

'''print(mydict["Generator"])
print(mydict["Operator"])
print(mydict["Destroyer"])
print(mydict["GOD"])
print(mydict["Main God"])
print(mydict["Similar God"])
print(mydict["Similar God"]["Thakur"])'''

'''print(mydict.keys())
print(mydict.values())
print(mydict.items())'''

'''print(mydict)
updatedict = {
    "Lord of Universe":"Jagannath Dev",
    "Symbol of Love":"Chaitannya Dev",
    "Great Leader":"Swamiji",
    "Similar God":{"Thakur":"Swamiji"},
}
mydict.update(updatedict)
print(mydict)'''

'''print(mydict.get("GOD"))
print(mydict["GOD"])
# In above case the output is same for both the functions(Similarity).
print(mydict.get("God"))
print(mydict["God"])
# In the above case since there is no key as God so get() function is returning None/Null as output while normal mydict[] fucntion throwing an error(Difference).'''
