names = []
for _ in range(4):
    names.append(input("Enter a name:"))

#printing names in alphabetical order 
for name in sorted(names):
    print(f"Hello {name}")

#printing names in reverse alphabetical order#Mission2023-2

# sorted(iterable, /, *, key=None, reverse=False)   
for name in sorted(names, reverse=True):
    print(f"Hello {name}")
    
studentList = [["Hermoine","Griffindor"], ["Harry","Griffindor"], ["Ron","Griffindor"],["Draco","Slytherine"]]
studentDictList = []
for s in studentList:
    studentDictList.append({"name"  : s[0], "house" : s[1]})
print(studentDictList)

studentTouples = [("Hermoine","Griffindor"), ("Harry","Griffindor"), ("Ron","Griffindor"),("Draco","Slytherine")]
sDictList = []
for s in studentTouples:
    sDictList.append({"name"  : s[0], "house" : s[1]})
print(sDictList)