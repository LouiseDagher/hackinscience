import sys
import operator
a = len(sys.argv)
if a == 3:
    sys.argv[1] = int(sys.argv[1])
    sys.argv[2] = int(sys.argv[2])
    d = operator.add(sys.argv[1], sys.argv[2])
    print(d)
else:
    print("usage: python3 solution.py OP1 OP2")
