#method Get
alphabet = {
    1:"a",
    2:"b",
    3:"c",
}
result = alphabet.get(1)
print(result)

result_1 =alphabet.get(2)
print(result_1)

#keys
result_2 = alphabet.keys()
print(result_2)

#values
result_3 = alphabet.values()
print(result_3)

#item
result_4 = alphabet.items()
print(result_4)

if 1 in alphabet:   #In default case seraching works for keys
    print("ok")

if 1 in alphabet.keys():
    print("ok")

if "a" in alphabet.values():
    print("ok")    

#update - has 2 operations update and append, if the key does`nt exists then appending new item with key
manufactured = {
    "brand": "BMW",
    "modal": "Z4",
    "color": "blue",
}
manufactured.update({"color":"yellow"})
print(manufactured)

manufactured.update({"year":"2021"})
print(manufactured)

#pop
manufactured.pop("brand")
print(manufactured)

#popitem    - remove last item
manufactured.popitem()
print(manufactured)

#cleare
manufactured.clear()
print(manufactured)

"""
#delete - 
del manufactured
print(manufactured)
"""

models = {
    "bmw": "Z4",
    "mercedes": "W223",
    "audi": "a4",
    "toyota": "RAV4"
}

for x,y in models.items():
    print(x, end=" ")
    print(y)

#copy-create duplicate
thisdict = {
  "brand": "BMW",
  "model": "X5M",
  "year": 2019,
  "color": "Black",
  "engine":  4.4,
}
mydict = thisdict.copy()
print(mydict)
