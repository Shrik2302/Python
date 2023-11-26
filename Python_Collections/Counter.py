from collections import Counter

# With sequence of items
print(Counter(["A","B","C","A","B","C","A","B","C"]))
print(type(Counter(["A","B","C","A","B","C","A","B","C"])))

# With sequence of items
print(Counter({'A':3,'B':5,'C':4}))

# with keyword arguments
print(Counter(A=3,B=4,C=5))

# updating
count=Counter()
count.update([1,2,3,4,1,2,3])
print(count)

count.update([5,4,6])
print("new count",count)

# The element() Function
print("elements",list(count.elements()))

# The most_common() Function
print("most_common",count.most_common())
print("most_common_type",type(count.most_common()))

# The subtract() Function
deduct = {1:1, 2:2}
count.subtract(deduct)
print(count)
