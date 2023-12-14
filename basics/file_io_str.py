
names = ["Harry", "Hermione", "Ron", "Draco"]
languages = ["c", "python", "c++", "fortran"]

#Write 1 (open and close)
file = open("names.txt", "w")
for name in sorted(names):
    file.write(f"{name}\n")
file.close()

#Write 2 (with) (Preferred - no explict closing required)
with open ("languages.txt", "w") as file:
    for lan in languages:
        file.write(f"{lan}\n")

#Read 1 (reading line by line)
with open("names.txt", "r") as file:
    for line in file:
        print(f"{line.rstrip()}")

#Read 2 (readlines)
with open("languages.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(f"{line.rstrip()}")

#Read 3 (copy lines to a list)
strs = []
with open("names.txt", "r")as file:
    for line in file:
        strs.append(line.rstrip())
for name in sorted(strs, reverse=True):
    print(f"Hello {name}")