#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import pyphen
import os
import math

dic = pyphen.Pyphen(lang='de_DE')
ColumnsRowsAmount, shellRowsAmount = os.popen('stty size', 'r').read().split()

def primfak(n):

    """ zerlegt eine Zahl in ihre Primfaktoren

    >>> primfaktoren(24)
    [2, 2, 2, 3]

    """

    faktoren = []
    z = n
    while z > 1:
        # bestimme den kleinsten Primfaktor p von z
        i = 2
        gefunden = False
        while i*i <= n and not gefunden:
            if z % i == 0:
                gefunden = True
                p = i
            else:
                i = i + 1
        if not gefunden:
            p = z
        # füge p in die Liste der Faktoren ein
        faktoren = faktoren + [p]
        z = z // p
    return faktoren
#print(str(primfak(7)))

def wrapping(text,length):
    if len(text) > length:
        isItNone = dic.wrap(text, length)
    else:
        isItNone = None
    return isItNone

def colorize(text,num, row, rest=False):
    #\033[0;34mblaues Huhn\033[0m.
    num = int(num)
    if rest:
        if num == 0:
            return '\033[41m'+'\033[30m'+'\033[1m'+text+'\033[0m'
        elif num % 2 == 0:
            return '\033[47m'+'\033[30m'+text+'\033[0m'+'\033[0m'
        else:
            return '\033[40m'+'\033[37m'+text+'\033[0m'+'\033[0m'
    elif moonNumber(num)[1] != []:
        #00;33
        return '\033[46m'+'\033[30m'+text+'\033[0m'+'\033[0m'
    elif len(primfak(num)) == 1:
        return '\033[43m'+'\033[30m'+text+'\033[0m'+'\033[0m'
    elif num % 2 == 0:
        if num == 0:
            return '\033[41m'+'\033[30m'+'\033[1m'+text+'\033[0m'
        else:
            return '\033[47m'+'\033[30m'+text+'\033[0m'+'\033[0m'
    else:
        return '\033[40m'+'\033[37m'+text+'\033[0m'+'\033[0m'

def moonNumber(num):
    results=[]
    exponent=[]
    for i in range(2,num):
        oneResult = math.pow(num, 1/i)
        if math.floor(oneResult) == oneResult:
            results += [oneResult]
            exponent += [i-2]
    return results, exponent

#for i in range(100):
#    print(str(i)+'. '+str(moonNumber(i)))

if True:
    textwidth = 21
    with open('religion.csv', mode='r') as csv_file:
        relitable = []
        for row in list(csv.reader(csv_file, delimiter=';')):
            relitable += [row]
    headingsAmount = len(relitable[0])
    newRows = []
    for u, line in enumerate(relitable):
        new2Lines = []
        for t, cell in enumerate(line):
            newLines = [[]]*headingsAmount
            isItNone = wrapping(cell, textwidth)
            cell2 = tuple()
            rest = cell
            while not isItNone is None:
                cell2 += isItNone
                isItNone = wrapping(cell2[-1], textwidth)
                rest = cell2[-1]
                cell2 = cell2[:-1]
            else:
                cell2 += (rest,)
                for k,cellInCells in enumerate(cell2):
                    if k < len(newLines):
                        newLines[k] += [cellInCells]
                    else:
                        pass
            new2Lines += [newLines[t]]
        newRows += [new2Lines]
    # c nächste silbe
    # b nächste Spalte
    # a nächste Zeile
    #exit()
    #originalLinesRange = range(len(newRows))
    originalLinesRange = range(120)
    #realLinesRange = range(len(newRows[0]))
    realLinesRange = range(50)
    #rowsRange = range(len(newRows[0][0]))
    rowsRange = range(50)

    #print(newRows[0][1][0])
    #exit()
    maxPartLineLen = 0
    for k in originalLinesRange: # n Linien einer Zelle, d.h. 1 EL = n Zellen
        actualPartLineLen = 0
        for m in rowsRange: # eine Zeile immer
            actualPartLineLen += 1
            line=''
            linesEmpty = 0
            for i in realLinesRange: # Teil-Linien nebeneinander als Teil-Spalten
                maxRowsPossible = math.floor( int(shellRowsAmount) / int(textwidth+1))
                if i < maxRowsPossible and k < 6:
                    try:
                        line += colorize(newRows[k][i][m].ljust(textwidth), k, i)+' ' # neben-Einander
                    except:
                        linesEmpty += 1
                        line += colorize(''.ljust(textwidth), k,i ,True)+' ' # neben-Einander
            if k < 6 and linesEmpty != maxRowsPossible: #and m < actualPartLineLen:
                print(line)
                #print(colorize(str(linesEmpty)+' '+str(maxRowsPossible), k))
        if actualPartLineLen > maxPartLineLen:
            maxPartLineLen = actualPartLineLen






