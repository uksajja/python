names = ["Hermoine", "Harry", "Ron", "Draco"]
#1. List method sort()
names.sort() #original list changes to contain the sorted items
print(names)

#2. sorted()
languages = ["c", "python", "c++", "fortan"]
s_languages  = sorted(languages)
print(languages)   #languages is not sorted, still contain the original order
print(s_languages) #sorted list

#3. Reverse sorting
r_languages = sorted(languages, reverse = True)
print(r_languages) #reverse sorting

#4. sorted() can be applied on any iterable
print(sorted({1: 'D',  3: 'B', 2: 'B', 5: 'A', 4: 'E'}))

#5. sorted() - sorting a dictionary based on keys
def get_name(student):
    return student["name"]
def get_house(student):
    return student["house"]
students = [{'name': 'Hermoine', 'house': 'Gryffindor'}, {'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Ron', 'house': 'Gryffindor'}, {'name': 'Draco', 'house': 'Slytherin'}]
s_students_name = sorted(students, key = get_name)
print(s_students_name)

s_students_house = sorted(students, key = get_house)
print(s_students_house)










