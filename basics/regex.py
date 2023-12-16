import re
#re.search(pattern, string, flag =0)
"""
.     represents any charater
*     0 or more repetitions
+     1 or more repetitions
?     0 or 1 repetitions
{m}   m repetitions
{m,n} m-n repetitions

^     matches the start of the string
$     matches the end of the string
[]    match any set of characters inside[]
[^]   complementing the set - cannot match any of the characters inside[]

\w    word character - alphanumeric character as well as underscore
\W    not a word character
\d    decimal digit
\D    not a decimal digit
\s    whitespace character

A|B     either A or B
(...)   a group
(?:..)  non capturing version

.*@.*                    0 or more chars followed by @ followed by 0 or more chars
.+@.+                    1 or more chars followed by @ followed by 1 or more chars
..*@..*                  - same as above
.+@.+\.edu               1 or more chars followed by @ followed by 1 or more chars followed by .edu
                        (\. matches only with . character where as just . matches any character)
r".+@.+\.edu"            raw string to tell \ is used in a usual way as an escape character
r"^.+@.+\.edu$"          strictly searches for email address only but not a complete sentences involving email address
r"^[^@]+@[^@]+\.edu$"    strictly allows only one @ in email  -- This has replaced . with [^@] to match any character except @

"""

def main():
    email = input("What is your email? ").strip()
    print(is_valid(email))

    
def is_valid(email): #allows '.' in domain name or subdomain name
    if re.search(r"^(\w+\.)*\w+@(\w+\.)?\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE):
        return("Valid")
    else:
        return("Invalid")
    
def is_valid4(email): #allows '.' in domain name or subdomain name
    if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|gov|net|org)$", email):
        return("Valid")
    else:
        return("Invalid")
    
def is_valid3(email):
    if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email):
        return("Valid")
    else:
        return("Invalid")
    
def is_valid2(email):
    if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
        return("Valid")
    else:
        return("Invalid")
    
def is_valid1(email):
    if re.search(r"^[^@]+@[^@]+\.edu$", email):
        return("Valid")
    else:
        return("Invalid")
    
if __name__== "__main__":
    main()
    