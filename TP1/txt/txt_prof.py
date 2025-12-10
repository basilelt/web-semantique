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


# Compréhensions
def map(f, s):
    r = []
    for e in s:
        r += [f(e)]
    return r


prefix = map(lambda e: map(lambda x: "http://sem.org#" + x, e), db)

unprefix = map(lambda e: map(lambda x: x.replace("http://sem.org#", ""), e), prefix)
print(unprefix)
