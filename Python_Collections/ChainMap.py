from collections import ChainMap

d1={'a':1,'b':2}
d2={'c':3,'d':4}
l=[]
l.append(d1)
l.append(d2)
print(l)

dict1={'a':1,'b':2}
dict2={'c':3,'d':4}
dict3={'e':5,'f':6}
c1=ChainMap(dict1,dict2,dict3)
print("c1:",c1)


# Accessing Keys and Values from ChainMap
print("values: ",list(c1.values()))
print("keys: ",list(c1.keys()))
print("maps: ",c1.maps)

# Adding new dictionary
print("before update c1: ",c1)
dict4={'f':7,'g':8}
chain1=c1.new_child(dict4)
print("updated chain1: ",chain1)
print(c1)

# reversed() :
dict1={'a':1,'b':2}
dict2= {'b':3,'c':4}
chain1=ChainMap(dict1,dict2)
print("chain1: ",chain1)
print("chain1[b]: ",chain1['b'])
chain1.maps=reversed(chain1.maps)
print("chain1[b]",chain1['b'])
