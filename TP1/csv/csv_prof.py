# Chargement des données
load = lambda name: open(name).read()
csv = map(lambda x: x.split(","), (load("data.csv")).split("\n"))
txt2 = "\n".join(map(lambda x: ",".join(x), csv))


# Ensembles
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


print(intersect(range(1, 10), range(5, 15)))
print(difference(range(1, 10), range(5, 15)))
print(union(list(range(1, 10)), list(range(5, 15))))
