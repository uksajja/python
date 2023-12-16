import csv


#Read file using csv reader
with open("students1.csv", "r") as file: 
    reader = csv.reader(file) 
    for row in reader:
        print(f"{row[0]} : {row[1]}")


students = []#List of dictionaries
with open("students1.csv", "r") as file:
    file_reader = csv.reader(file)
    for name, house in file_reader:
        students.append({"name":name, "house":house}) #Read each line and create a dictionary
#Sorting list of dictionaries based on keys (Please check sort.py)
for student in sorted(students, key = lambda student: student['name'], reverse = True):
    print(f"{student['name']} is in {student['house']}")
    
names = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
with open("students.csv", "a") as file:
    writer = csv.writer(file)
    for i in range (len(names)):
        writer.writerow([names[i], houses[i]])




