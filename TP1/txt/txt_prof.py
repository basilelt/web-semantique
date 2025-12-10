# Chargement des données
load = lambda name: open(name).read()


def intersect(s1, s2):
    r = []
    for e in s1:
        if e in s2:
            r += [e]
    return r


def difference(s1, s2):
    r = []
    for e in s1:
        if e not in s2:
            r += [e]
    return r


def union(s1, s2):
    return difference(s1, s2) + s2


txt = map(lambda x: x.split(" "), load("data.txt").replace("\n", "").strip().split("."))
sup = ["is", "at", "the"]

db = []
for phrase in txt:
    if phrase == [] or phrase == [""]:
        continue
    db += [difference(phrase, sup)]

print(db)

def map(f, set):
    r = []
    for e in set:
        r += [f(e)]
    return r


db_prefixed = []
for e in db:
    prefixe = map(lambda x: "http://sem.org#" + x, e)
    db_prefixed += [prefixe]
print(db_prefixed)