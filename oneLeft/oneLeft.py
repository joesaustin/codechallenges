def oneLeft(s):
    a = [['q','w','e','r','t','y','u','i','o','p'],['a','s','d','f','g','h','j','k','l'],['z','x','c','v','b','n','m']]
    d = {}

    for g in a:
        for i in g:
            if g.index(i) == 0:
                d[i] = g[-1]
            else:
                d[i] = g[g.index(i)-1]
    return "".join(map(lambda n: d[n], s))
