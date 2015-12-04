def love_meet(alice, bob):
    a = set(alice)
    b = set(bob)
    d = a & b
    return(d)

def affair_meet(bob, alice, silvester):
    a = set(alice)
    b = set(bob)
    c = set(silvester)
    d = a & b
    e = a & c
    for i in e:
        if i not in d:
            f = i
    return(f)
