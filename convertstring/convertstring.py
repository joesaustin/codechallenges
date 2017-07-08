def convertString(s, t):
    e=[]
    j=0

    for i in t:
        try:
            if s.index(i,j) >= j:
                e.append(i)
                j = s.index(i)
        except ValueError:
            return False

    if "".join(e) == t:
        return True
    else:
        return False
