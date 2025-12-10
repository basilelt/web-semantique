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
            r.append(e)
    return r


if __name__ == "__main__":
    # Load
    content = load("data.txt")
    print(content)

    # Split
    triplets = split(content)
    print(triplets)

    t_clean = []
    for triplet in triplets:
        if triplet == [""]:  # Skip empty triplets
            continue
        t_clean.append(nettoyage(triplet))

    print(t_clean)
