try:
    x = int(input("What is X? "))
except ValueError:
    print("x is not an integer")
else:  #if the exception is not resulted
    print(f"X value is {x}")
    
def main():
    x = get_an_integer()
    print(f" x is {x}")    
    y = get_int("What's y?")
    print(f"y is {y}")
    
def get_an_integer():
    while True:
        try:
            return int(input("What's X? ")) # return x when it is integer otherwise loop till x is integer
        except ValueError:
            print("x is not an integer")    # use pass to avoid the print msg
            
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
if __name__ == "__main__":
    main()            