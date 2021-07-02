import array as arr
  
# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print(a)
print(type(a))


for i in range (0, 3):
    print (a[i], end =" ")
print()
