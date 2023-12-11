import sys 
print(sys.path)
from basics.hello_example import hello
#import basics.hello_example as h

def main():
    test_default()

def test_default():
    hello()
    assert hello() == "Hello, World"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"Hello, {name}"
        
        
if __name__== "__main__":
    main()

