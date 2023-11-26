# UserList
# Syntax:
# collections.UserDict([initialdata])

from collections import UserList
# creating list where deleting is not allowed
class Mylist(UserList):
    def remove(self, s=None):
        raise RuntimeError("Deleting is not allowed")
    def pop( self, s= None):
        raise RuntimeError("Deleting is not allowed")

l=Mylist([1,2,3,4])
print("orignal: ",l)
l.append(5)
print("appended list:",l)
l.remove(2)
