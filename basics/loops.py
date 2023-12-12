

def get_a_positive_number():
    while True:
        n = int(input("Enter  a number:"))
        if n>0:
            return n

def main():

    sum = 0
    n = get_a_positive_number() 
    for i in range(n+1):
        sum += i
    print(f"Sum of first {n} natural numbers is : {sum}")

    i = 0
    while i<3:
        print("Hello")
        i += 1

    for _ in range(3):
        print("Hai!")

    for i in [0, 4, 2]:
        print(i , "Hello")

    for i in range(3):
        print(i , "Hello")

    strs = ["Hello", "Hai", "Hola!"]
    for i in range(len(strs)):
        print(strs[i])
        
    for name in strs:
        print(f"Hello {name}!")
        
    print("HelloHaiHola! "*3, end="\n")

if __name__ == "__main__":
    main()