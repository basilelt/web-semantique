# Chargement des données
load = lambda name: open(name).read()
csv = map(lambda x: x.split(","), (load("data.csv")).split("\n"))
txt2 = "\n".join(map(lambda x: ",".join(x), csv))

# Ensembles
print(txt2)
