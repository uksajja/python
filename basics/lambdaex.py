names = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Grifindor", "Grifindor", "Grifindor", "Slytherine"]
students = []
for i in range (len(names)):
    student = { "name": names[i], "house": houses[i]}
    students.append(student)
    
#Sort list of dictionaries using lamda function
for s in sorted(students, key = lambda st: st["name"], reverse=False):
    print(s)