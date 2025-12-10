# -*- coding: utf-8 -*-
# TP1/txt.py
"""
Created on Wed Dec 10 08:00:00 2025
@author: BLETHIEC
"""


##########
## LOAD ##
##########
def load(file):
    file = open(file, "r")
    content = file.read()
    file.close()
    return content


###########
## SPLIT ##
###########
def split(content):
    triplets = []
    content = content.replace("\n", "").strip()
    for line in content.split("."):
        triplets.append(line.split(" "))
    return triplets


###########
## WRITE ##
###########
def write(file, txt):
    file = open(file, "w")
    file.write(txt)
    file.close()


##############
## CONTAINS ##
##############
def contains(s, e):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] == e:
                return True
    return False


##################
## INTERSECTION ##
##################
def intersection(s1, s2):
    inter = []
    for i in s1:
        if i in s2:
            inter.append(i)
    return inter


################
## DIFFERENCE ##
################
def difference(s1, s2):
    diff = []
    for i in s1:
        if not i in s2:
            diff.append(i)
    return diff


###########
## UNION ##
###########
def union(s1, s2):
    uni = list(s1)
    for i in s2:
        if not i in uni:
            uni.append(i)
    return uni


###############
## NETTOYAGE ##
###############
def nettoyage(s):
    to_remove = ["at", "is", "a", "the", "in", "on", "and", "of", "to"]
    r = []
    for e in s:
        if e not in to_remove:
            r.append(e.lower())
    return r


#########
## MAP ##
#########
def map(f, s):
    r = []
    for e in s:
        r += [f(e)]
    return r


################
## CONCATENER ##
################
def concatener(s):
    r = []
    for e in s:
        r += e
    return r


############
## FILTER ##
############
def filter(p, t):
    r = []
    for e in t:
        if p(e):
            r += [e]
    return r


if __name__ == "__main__":
    content = load("data.txt")
    triplets = split(content)

    db = []
    for triplet in triplets:
        if triplet == [""]:  # Skip empty triplets
            continue
        db.append(nettoyage(triplet))

    db_prefixed = []
    for e in db:
        prefixe = map(lambda x: "http://sem.org#" + x, e)
        db_prefixed += [prefixe]

    db_unprefixed = []
    for e in db_prefixed:
        unprefixe = map(lambda x: x.replace("http://sem.org#", ""), e)
        db_unprefixed += [unprefixe]

    filtered = filter(lambda x: x[0] == "bob", db)
    filtered = [x for x in db if x[0] == "bob"]

    # [?x, rdf:type, ?y] => [?y, rdf:type, owl:Class] [?x, ?r, ?y]
    db += [[x[0], "rdf:type", "Person"] for x in db if x[1] == "studies"]
    db += [[x[0], "rdf:type", "University"] for x in db if x[1] == "located"]
    db += [[x[2], "rdf:type", "City"] for x in db if x[1] == "located"]
    
    # Class
    db += [[x[2], "rdf:type", "owl:Class"] for x in db if x[1] == "rdf:type"]
    
    # ObjectProperty
    db += [[x[1], "rdf:type", "owl:ObjectProperty"] for x in db if (x[1] != "rdf:type")]
    
    # NamedIndividual
    db += [[x[0], "rdf:type", "owl:NamedIndividual"] for x in db if x[1] == "rdf:type" and x[2] != "owl:Class"]

    # [?x, rdf:type, ?c] => [?r, rdf:domain, ?c]
    db += [[x[0], "rdf:domain", "Person"] for x in db if x[2] == "owl:ObjectProperty" and x[0] == "studies"]
    db += [[x[0], "rdf:range", "University"] for x in db if x[2] == "owl:ObjectProperty" and x[0] == "studies"]
        
    db += [[x[0], "rdf:domain", "University"] for x in db if x[2] == "owl:ObjectProperty" and x[0] == "located"]
    db += [[x[0], "rdf:range", "City"] for x in db if x[2] == "owl:ObjectProperty" and x[0] == "located"]


    for e in db:
        print(e)