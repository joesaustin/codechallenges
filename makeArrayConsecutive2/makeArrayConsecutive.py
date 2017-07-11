def makeArrayConsecutive2(statues):
    statues.sort()
    r = range(statues[0], (statues[-1]+1))
    l = [i for i in r if i not in statues]
    return len(l)
