names = []
for _ in range(4):
    names.append(input("Enter a name:"))

print(names)
#a = names.sort()
b = sorted(names)
print(names)
print(b)


# printing names in alphabetical order
for name in sorted(names):
    print(f"Hello {name}")


# printing names in reverse alphabetical order#Mission2023-2

# sorted(iterable, /, *, key=None, reverse=False)
for name in sorted(names, reverse=True):
    print(f"Hello {name}")

studentList = [
    ["Hermione", "Gryffindor"],
    ["Harry", "Gryffindor"],
    ["Ron", "Gryffindor"],
    ["Draco", "Slytherin"],
]
studentDictList = []
for s in studentList:
    studentDictList.append({"name"  : s[0], "house" : s[1]})
print(studentDictList)

studentTuples = [
    ("Hermione", "Gryffindor"),
    ("Harry", "Gryffindor"),
    ("Ron", "Gryffindor"),
    ("Draco", "Slytherin"),
]
sDictList = []
for s in studentTuples:
    sDictList.append({"name"  : s[0], "house" : s[1]})
print(sDictList)
