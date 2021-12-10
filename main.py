import random
pepple=random.choice(["красивоя","ужасноя"])
peppleludoed=random.choice(["голодный","не голодный"])
wether=random.choice(["плохая","ясноя"])
print("погода была",wether ,"и принцесса была",pepple ,"и людоед был ",peppleludoed)
if (wether=="ясноя" and pepple=="красивоя") or (wether=="ясноя" and pepple=="ужасноя") or (wether=="плохая" and pepple=="красивоя"):
    print("принцесса пошла гулять")
    if (peppleludoed == "голодный" and pepple=="красивоя") or (peppleludoed=="не голодный" and pepple=="красивоя") or (peppleludoed=="голодный" and pepple=="ужасноя"):
        print("принцессу съел людоед")
    else:
        print("принцессу не съел людоед")
else:
    print("принцесса не пошла гулять")
