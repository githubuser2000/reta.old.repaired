#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import pyphen
import os
import math

dic = pyphen.Pyphen(lang='de_DE')
ColumnsRowsAmount, shellRowsAmount = os.popen('stty size', 'r').read().split()

def wrapping(text,length):
    if len(text) > length:
        isItNone = dic.wrap(text, length)
    else:
        isItNone = None
    return isItNone

def colorize(text,num):
    #\033[0;34mblaues Huhn\033[0m.
    if moonNumber(num)[1] != []:
        #00;33
        return '\033[43m'+'\033[30m'+text+'\033[0m'+'\033[0m'
    if num % 2 == 0:
        if num == 0:
            return '\033[46m'+'\033[30m'+'\033[1m'+text+'\033[0m'
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
                maxRowsPossible = math.floor( int(shellRowsAmount) / int(textwidth))
                if i < maxRowsPossible and k < 6:
                    try:
                        line += newRows[k][i][m].ljust(textwidth)+' ' # neben-Einander
                    except:
                        linesEmpty += 1
                        line += ''.ljust(textwidth)+' ' # neben-Einander
            if k < 6 and linesEmpty != maxRowsPossible: #and m < actualPartLineLen:
                print(colorize(line, k))
                #print(colorize(str(linesEmpty)+' '+str(maxRowsPossible), k))
        if actualPartLineLen > maxPartLineLen:
            maxPartLineLen = actualPartLineLen






