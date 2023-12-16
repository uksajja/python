import sys

#command-line arguments
try:
    print("hello ", sys.argv[1])
except IndexError:
    print("Enter your name as an argument")
print(sys.argv)

if len(sys.argv)<2:
    print("Twoo few arguments")
#elif len(sys.argv)>2:
#    print("Twoo many arguments")
else:
    print("Hello ", sys.argv[1])
    
if len(sys.argv)<2:
    sys.exit("Two few arguments")
for arg in sys.argv[1:]:  #print arguments except the first argument
    print("Hello ", arg, sep = " ", end = "")
    
for arg in sys.argv[1:-1]: #print arguments except the first and the last arguments
    print("Hello", arg)