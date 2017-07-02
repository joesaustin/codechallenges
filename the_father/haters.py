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

haters=["Willia_Faircloth Jenee_Platero",
 "Jenee_Platero Dennis_Lukes",
 "Vanessa_Alward Colby_Leeds",
 "Retta_Hedberg Dirk_Spires",
 "Inell_Izzard Fernanda_Chappel",
 "Colby_Leeds Berta_Wittig",
 "Fernanda_Chappel Berta_Wittig",
 "Sidney_Whitlock Saundra_Cozad",
 "Lavonda_Frederickson Retta_Hedberg",
 "Jenee_Platero Christal_Pippin",
 "Dirk_Spires Retta_Hedberg",
 "Lilly_Hamp Johnathon_Arpin",
 "Saundra_Cozad Fern_Grunwald",
 "Lesa_Barnhouse Fern_Grunwald"]

print thefather(haters)