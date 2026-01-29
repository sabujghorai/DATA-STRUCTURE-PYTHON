from array import * # from array import all 
val = array('i',[1,2,3,4,5,6,7,8,9,10])  # 'i' --> integer (usually 2 bytes)

for i in range(0,len(val)): # better syntax
    print(val[i],end=" ")

print("\n")
for x in val: # enhance for loop to print the array
    print(x,end=" , ")



from array import * # from array import all 
val = array('i',[1,2,3,4,5,6,7,8,9,10])  # 'i' --> integer (usually 2 bytes)

print("\n")
print(val.typecode) # prints i ---> typecode is integer

val.reverse() # reverse the array
for i in range(0,len(val)):
    print(val[i],end=" ")
print("\n")


from array import * # from array import all 
val = array('i',[1,2,3,4,5,6,7,8,9,10])  # 'i' --> integer (usually 2 bytes)


val.insert(0,50) # 0 is the index and 50 is the new adding element
for i in range(0,len(val)):
    print(val[i],end=" ")
print("\n")

from array import * # from array import all 
val = array('i',[1,2,3,4,5,6,7,8,9,10])  # 'i' --> integer (usually 2 bytes)


val.append(50) # at the element at the end
val[2] = 100 # replace the second element with 100
for i in range(0,len(val)):
    print(val[i],end=" ")
print("\n")