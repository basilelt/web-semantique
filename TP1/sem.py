# -*- coding: utf-8 -*-
# TP1/sem.py
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
    csv = []
    for line in content.split("\n"):
        csv.append(line.split(","))
    return csv


##########
## JOIN ##
##########
def join(csv):
    txt = "\n".join([",".join(triplet) for triplet in csv])
    return txt


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


if __name__ == "__main__":
    # Load
    content = load("data.csv")
    print(content)

    # Split
    csv = split(content)
    print(csv)

    # Join
    txt = join(csv)
    print(txt)

    # Write
    write("data_copy.csv", txt)
    print(load("data_copy.csv"))

    # Contains
    print(contains(csv, "ensisa"))  # True
    print(contains(csv, "uha"))  # False


    # Intersection
    print(intersection(range(1, 10), range(5, 15)))
    
    # Difference
    print(difference(range(1, 10), range(5, 15)))
    
    # Union
    print(union(range(1, 10), range(5, 15)))
    
    