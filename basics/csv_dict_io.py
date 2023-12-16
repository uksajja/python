import csv

students = []   
with open("student_dict.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #students.append({"name": row["name"], "house": row["house"]})
        students.append(row)
for student in sorted(students, key = lambda st: st['name']):
    print(student)

names = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
with open("student.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames = ["house", "name"])
    for i in range(len(names)):
        writer.writerow({"house": houses[i], "name": names[i]})
        #writer.writerow([houses[i], names[i]])

