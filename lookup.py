#!/usr/bin/env python
import csv
import math
import sys



def importer():
    if len(sys.argv) < 2:
        print("That was unpog")
        exit()

    contents = []
    with open(sys.argv[1]) as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        for row in csv_read:
            contents.append(row)
    return contents

def greatFilter():
    filter = importer()
    newList = []
    for row in filter:
        #print(row)
        row[2] = float(row[2])
        row[4] = float(row[4])
        if distance(row[2], row[4]) > 6000:
            #print("")
            #print(row[1], row[2])
            #print(row[0], distance(row[1], row[2]))
            newList.append(row)
    return newList

def distance(x, z):
    d = math.sqrt(x**2+z**2)
    return d

def trained():
    kk = greatFilter()
    #print(kk)
    for player in kk:
        print("|||" + player[0] + "|||" + "," + str(player[2]) + "," + str(player[4]) + ",")
        for player2 in kk:
            if player2 != player:
                if distance(player[2]-player2[2], player[4]-player2[4]) < 500:
                    print(player2[0] + "," + str(player2[2]) + "," + str(player2[4]) + "," + str(distance(player[2]-player2[2], player[4]-player2[4])))
                    print("")
trained()
