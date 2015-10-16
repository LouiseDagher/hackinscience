import sys
a = len(sys.argv)
if a>=2:
    print(sys.argv[1])
else:
    print("usage: python3 solution.py PARAM")
