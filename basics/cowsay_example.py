#list of packages and documentation at pypi.org
# pypi.org/project/cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello " + sys.argv[1]) 
    cowsay.trex("Hai " + sys.argv[1])