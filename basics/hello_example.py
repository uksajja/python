def main():
    titlecase()
    capitalize()
    print(hello())

def titlecase():
    name = input(" Name?").strip().title()
    #Remove whitespace from str and make it title case

    print(f"Name: {name}")
    
def capitalize():
    # capitalize only capitalizes only the first letter of the string
    sentence = input ("sentence:?").capitalize()
    print(f"Capsentence: {sentence}")

    
def splitExample():
    txt= "hello, this Python course is very interesting, easy to learn, and useful"
    w1, w2, w3, w4 =  txt.split(",")
    print(w1, w2)    
    
def splitName():
    fullname = input(" FullName?")
    first, last = fullname.split(" ")
    print(f"Firstname: {first} : Lastname: {last}")

def hello(to = "World"):
    print("HelloWorld")
    return f"Hello, {to}"

if __name__ == "__main__":
    main()
