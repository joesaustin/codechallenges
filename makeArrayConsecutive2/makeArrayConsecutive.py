def makeArrayConsecutive2(statues):
    statues.sort()
    r = range(statues[0], (statues[-1]+1))
    return len([i for i in r if i not in statues])