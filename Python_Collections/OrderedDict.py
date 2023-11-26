from collections import OrderedDict

print("this is dict")
d= {}
d['a']=1
d['b']=2
d['c']=3
d['d']=4
print("d=",d)
print(type(d))

print("\n")
print("this ordinaryDict")
od=OrderedDict()
od['a']=1
od['b']=2
od['c']=3
od['d']=4
print(od)

for key, value in od.items():
    print(key, value)


# deleting and re-inserting the same key
# deleting element
od.pop('a')
print(od)
# inderting element
od['a']=1
print(od)

print(d)
d.pop('a')
print(d)
d['a']=1
print(d)


# Key value Change
od['c']=5
print(od)



