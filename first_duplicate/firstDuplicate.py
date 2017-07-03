def firstDuplicate(a):
    occurence = {}
    first_dup = None

    for i in a:
        if a.count(i) > 1 and str(i) not in occurence.keys():
            indices = [j for j, x in enumerate(a) if x == i]
            if len(indices) > 1:
                occurence[str(i)]=indices

    for key, value in occurence.iteritems():
        current = value[1]
        if current < first_dup or first_dup is None:first_dup=current

    if first_dup is None:
        return -1
    else:
        return a[first_dup]