from collections import namedtuple
Student = namedtuple('Student',['name','age','DOB'])
S=Student('shrikant','21','2302199')
print(id(Student))
print(S)
print(type(S))
print(S[1])
print(S.name)


# Conversion Operations
S1=["Amar","22","10101999"]
S2=Student._make(S1)
print(Student._make(S1))
print(id(Student))
print(id(S2))
print(S2.name)
## using _asdict() to return an OrderedDict()
print (S._asdict())


# Let’s see various Operations on namedtuple() :
# Access Operations
# Access using index
print(S2[1])

## Access using name
print(S2.name)

# Access using getattr()
print(getattr(S2,'DOB'))

# using ** operator to return namedtuple from dictionary
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' }
print(Student(**di))


# Additional Operations
# fields :- This function is used to return all the keynames of the namespace declared.
print("Fields: ",S2._fields)

#_replace() :- This function is used to change the values mapped with the passed keyname.
print(S2._replace(name= "Aniket"))
print(id(S2._replace(name= "Aniket")))
print(S2)
print(id(S2))

S3=S2._replace(name= "Aniket")
print(S3)

