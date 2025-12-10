load = lambda x: open(x, "r").read()

intersect = lambda s1, s2: list(filter(lambda x: x in s2, s1))
difference = lambda s1, s2: list(filter(lambda x: x not in s2, s1))
union = lambda s1, s2: difference(s1, s2) + s2

txt = map(lambda x: x.split(" "), load("data.txt").replace("\n", "").strip().split("."))
sup = ["is", "at", "the"]

db = []
for phrase in txt:
    if phrase == [] or phrase == [""]:
        continue
    db += [difference(phrase, sup)]


db += [[x[0], "rdf:type", "Person"] for x in db if x[1] == "studies"]

print(db)
