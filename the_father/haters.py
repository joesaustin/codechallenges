def thefather(haters):
    group1 = []
    group2 = []
    names={}
    num=1

    for i in haters:
        status = True
        d = i.index(" ")
        names["name{0}".format(num)] = [i[:d], i[d + 1:]]
        num += 1

    any_in = lambda group1, group2: any(i in group2 for i in group1)
    for key, value in names.iteritems():
        if value[0] not in group1 and value[0] not in group2:
            group1.append(value[0])
            if value[1] not in group2:
                group2.append(value[1])
        if any_in(group1, group2):
            status = False
            break

    return status
