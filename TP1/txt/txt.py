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
    print(db_unprefixed)
