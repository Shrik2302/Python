from _collections import defaultdict
# defaultdict never raises a KeyError

def def_value():
    return "Not present"

value = None
d=defaultdict(def_value)
d['a'] = 1
d['b'] = 2
print(d['c'])

# Inner Working of defaultdict
d = defaultdict(lambda : "Not present new")
print(d['c'])


# __missing__():
# Defining the dict
d = defaultdict(lambda: "Not Present missing")
d["a"] = 5
d["b"] = 6
print(d)
# Provides the default value
# for the key
print(d.__missing__('a'))
print(d.__missing__('d'))
print(d)


# Using List as default_factory
d = defaultdict(list)
for val in range(5):
    d[val].append(val)
print(d)


# Using int as default_factory
d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]
for val in L:
    d[val] += 1
print(d)


