names = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
studentsList = [["Hermione","Gryffindor"], ["Harry","Gryffindor"], ["Ron", "Gryffindor"], ["Draco","Slytherin"]]
studentsTouple = [("Hermione","Gryffindor"), ("Harry","Gryffindor"), ("Ron", "Gryffindor"), ("Draco","Slytherin")]
with open("students1.csv", "w") as file:
    for student in studentsTouple:
        file.write(f"{student[0]}, {student[1]}\n")
with open("students2.csv", "w") as file:
    for i in range(len(names)):
        file.write(f"{houses[i]}, {names[i]}\n")
        

#Read file and print the file line by line
with open("students1.csv", "r") as file:  
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} : {row[1]}")
print("_________________________") 
lines = [] # List of lines. Store each line in a list as a sentence
with open("students1.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        lines.append(f"{name} is in {house}") # creating the list of sentences
for line in sorted(lines): #sorting the sentences (NOT based on the keys)
    print(line)
print("_________________________")            
students = []#List of dictionaries
with open("students1.csv", "r") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name":name, "house":house}) #Read each line and create a dictionary
#Sorting list of dictionaries based on keys (Please check sort.py)
for student in sorted(students, key = lambda student: student['name'], reverse = True):
    print(f"{student['name']} is in {student['house']}")
