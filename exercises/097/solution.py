def love_meet(alice, bob):
    a = set(alice)
    b = set(bob)
    d = a & b
    return(d)


def affair_meet(bob, alice, silvester):
    a = set(alice)
    b = set(bob)
    c = set(silvester)
    e = a & c
    y = e - b
    r = set(y)
    return(r)
