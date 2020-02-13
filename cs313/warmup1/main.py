from __future__ import print_function
import numpy as np
import math


def prettyPrint(ary):
    for i in range(len(ary[0])):
        for j in range(len(ary)):
            print (ary[j][i], end='')
    print()
  
def encrypt(row,ary):
    leng = len(ary)
    col = int(math.ceil(float(leng) / row))
    ary2 = [[] for _ in range(row)]
    count = 0

    for i in range(row):
        for j in range(col):
            if count < leng:
                ary2[i].append(ary[count])      
            else:
                ary2[i].append('Z')
            count = count + 1

    return ary2
          
def decrypt(col,ary):
    leng = len(ary)
    row = leng / col
    ary2 = [[] for _ in range(col)]
    count = 0



    for i in range(row):
        for j in range(col):
            


lst = []
count = 0
with open("cryptoFile.txt",'r') as cFile:
    for line in cFile:
        lst.append(line.strip())
        if lst[count][0] == 'E':
            #print lst[count][2:-1]
            prettyPrint(encrypt(int(lst[count][1]),lst[count][2:-1]))
        else:
            decrypt(int(lst[count][1]),lst[count][2:-1])
    
        count = count + 1