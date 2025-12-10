# -*- coding: utf-8 -*-
# TP1/sem.py
"""
Created on Wed Dec 10 08:00:00 2025
@author: BLETHIEC
"""


##########
## LOAD ##
##########
def load(filename):
    file = open(filename, "r")
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
def write(filename, txt):
    file = open(filename, "w")
    file.write(txt)
    file.close()


##############
## CONTAINS ##
##############
def contains(ensemble, element):
    for i in range(len(ensemble)):
        for j in range(len(ensemble[i])):
            if ensemble[i][j] == element:
                return True
    return False


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
