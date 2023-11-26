# Syntax:
# class collections.deque(list)
from collections import deque

deque1 = deque([1, 2, 3, 4])
print(deque1)
print(type(deque1))


# Inserting Elements
deque1.append(5)
print(deque1)

# using appendleft() to insert element at left end
deque1.appendleft(6)
print(deque1)

# using appendright() to insert element at right end
deque1.append(7)
print(deque1)


# Removing Elements

# using pop() to delete element from right end
deque1.pop()
print(deque1)

# using popleft() to delete element from right end
deque1.popleft()
print(deque1)


# Inserting Elements

# using index() to print the first occurrence of 4
print(deque1.index(4, 0, len(deque1)))

# insert(i, a) :- This function inserts the value -
# - mentioned in arguments(a) at index(i) specified in arguments.
deque1.insert(2, 10)
print(deque1)

# remove() :- This function removes the-
# -first occurrence of value mentioned in arguments
deque1.remove(10)
print(deque1)

# count() :- This function counts the -
# - number of occurrences of value mentioned in arguments.
print(deque1.count(3))

# extend(iterable) :- This function is used to add multiple -
# -values at the right end of deque. The argument passed is an iterable.
deque1.extend([7, 8, 9])
print(deque1)

# extendleft(iterable) :- This function is used to add multiple values at the left-
# -end of deque.The argument passed is an iterable. Order is reversed as a result of left appends.
deque1.extendleft([10, 11, 12])
print(deque1)

# reverse() :- This function is used to reverse order of deque elements.
deque1.reverse()
print(deque1)

# rotate() :- This function rotates the deque by the number specified in arguments.
# If the number specified is negative, rotation occurs to left.
# Else rotation is to right. filter_none
deque1.rotate(3)
print(deque1)
deque1.rotate(-3)
print(deque1)
print(deque1.__mul__(2))
