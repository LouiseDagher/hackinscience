import sys
a = enumerate(sys.argv)
for i, e in a :
    i = str(i)
    print(i + " " + e)
