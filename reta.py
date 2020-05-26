#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import pyphen
import os
import math
import sys

dic = pyphen.Pyphen(lang='de_DE')
ColumnsRowsAmount, shellRowsAmount = os.popen('stty size', 'r').read().split()
paramLines = set()
paramRows = set()
toYesDisplayLines = set()
toYesdisplayRows = set()
toNotDisplayLines = set()
toNotDisplayRows = set()
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

zaehlungen = [0,{},{},{}]


def parameters(argv):
    global paramLines, paramRows
    bigParamaeter=[]
    for arg in argv[1:]:
        if len(arg) > 0 and  arg[0] == '-':
            if len(arg) > 1 and arg[1] == '-' and len(bigParamaeter) > 0 and bigParamaeter[-1] == 'zeilen': # unteres Kommando
                if arg[2:7]=='zeit=':
                    for subpara in arg[7:]:
                        if '=' in subpara:
                            paramLines.add('=')
                        elif '<' in subpara:
                            paramLines.add('<')
                        elif '>' in subpara:
                            paramLines.add('>')
                elif arg[2:11]=='zaehlung=':
                    for maybedigit in arg[11:].split(','):
                        if maybedigit.isdecimal() and int(maybedigit) != 0:
                            paramLines.add(maybedigit+'z')
                elif arg[2:6]=='typ=':
                    for word in arg[6:].split(','):
                        if word == 'sonne':
                            paramLines.add('sonne')
                        elif word == 'schwarzesonne':
                            paramLines.add('schwarzesonne')
                        elif word == 'planet':
                            paramLines.add('planet')
                        elif word == 'mond':
                            paramLines.add('mond')
                elif arg[2:20]=='primzahlvielfache=':
                    for word in arg[20:].split(','):
                        if word.isdecimal():
                            paramLines.add(word+'p')
                elif arg[2:22]=='vorhervonausschnitt=':
                    maybeAmounts=arg[22:].split('-')
                    if len(maybeAmounts) == 1 and maybeAmounts[0] != '0':
                        if maybeAmounts[0].isdecimal():
                            paramLines.add('1-a-'+str(int(maybeAmounts[0])))
                    elif len(maybeAmounts) == 2 and maybeAmounts[1] != '0' and maybeAmounts[0] != '0':
                        if maybeAmounts[0].isdecimal() and maybeAmounts[1].isdecimal():
                            paramLines.add(maybeAmounts[0]+'-a-'+maybeAmounts[1])
                elif arg[2:21]=='nachtraeglichdavon=':
                    maybeAmounts=arg[21:].split('-')
                    if len(maybeAmounts) == 1 and maybeAmounts[0] != '0':
                        if maybeAmounts[0].isdecimal():
                            paramLines.add('1-z-'+maybeAmounts[0])
                    elif len(maybeAmounts) == 2 and maybeAmounts[1] != '0' and maybeAmounts[0] != '0':
                        if maybeAmounts[0].isdecimal() and maybeAmounts[1].isdecimal():
                            paramLines.add(maybeAmounts[0]+'-z-'+maybeAmounts[1])
            else: # oberes Kommando
                if arg[1:]=='zeilen':
                    bigParamaeter += ['zeilen']
                elif arg[1:]=='spalten':
                    bigParamaeter += ['spalten']

def fromUntil(a):
    if a[0].isdecimal():
        a[0] = int(a[0])
        if len(a) == 2 and a[1].isdecimal():
            a[1] = int(a[1])
        elif len(a) == 1:
            swap = a[0]
            a[0] = 1
            a += [swap]
            a[0] = 1
        else:
            return (1,1)
        return a
    else:
        return (1,1)


def FilterOriginalLines(numRange : set): # ich wollte je pro extra num, nun nicht mehr nur sondern modular ein mal alles und dann pro nummer in 2 funktionen geteilt
    global toYesDisplayLines, toYesdisplayRows, zaehlungen, paramLines, paramRows, toNotDisplayLines
    def bereinigen(wether, a : set, b : set):
        if wether:
            a.difference(b)
#            for n in a.copy():
#                if not n in b:
#                    a.remove(n)

    for condition in paramLines:
        if '-a-' in condition:
            a = fromUntil(condition.split('-a-'))
            print('ä '+str(a))
            for n in numRange.copy():
                if a[0] > n or a[1] < n:
                    numRange.remove(n)
                    toNotDisplayLines.add(n)
    print('ö '+str(numRange))

    numRangeYesZ = set()
    ifZeitAtAll = False

    for condition in paramLines:
        if '=' == condition:
            ifZeitAtAll = True
            numRangeYesZ.add(9)
        elif '<' == condition:
            ifZeitAtAll = True
            for n in numRange.copy():
                if n < 9:
                    numRangeYesZ.add(n)
        elif '>' == condition:
            ifZeitAtAll = True
            for n in numRange.copy():
                if n > 9:
                    numRangeYesZ.add(n)

    bereinigen(ifZeitAtAll, numRange, numRangeYesZ)
    print('ö2 '+str(numRange))

    numRangeYesZ = set()
    ifZaehlungenAtAll = False
    for condition in paramLines:
        if len(condition) > 2 and condition[-1] == 'z' and condition[0:-1].isdecimal(): # ist eine von mehreren Zählungen
            if not ifZaehlungenAtAll:
                setZaehlungen(originalLinesRange[-1])
                ifZaehlungenAtAll = True
            zaehlungGesucht = int(condition[0:-1]) # eine zählung = eine zahl, beginnend minimal ab 1
            for n in numRange: # nur die nummern, die noch infrage kommen
                #zaehlungen = [0,{},{},{}]
                wouldBeZwahlungNum = zaehlungen[3][n]
                if wouldBeZwahlungNum.isdecimal() and wouldBeZwahlungNum == zaehlungGesucht: # nummer der zählung
                    numRangeYesZ.add(n)

    bereinigen(ifZaehlungenAtAll, numRange, numRangeYesZ)

    for condition in paramLines:
        if '-z-' in condition:
            z = fromUntil(condition.split('-z-'))
    return numRange


def primfak(n : int):

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

def wrapping(text,length : int):
    if len(text) > length:
        isItNone = dic.wrap(text, length)
    else:
        isItNone = None
    return isItNone

def colorize(text,num : int, row, rest=False):
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

def moonNumber(num : int):
    results=[]
    exponent=[]
    for i in range(2,num):
        oneResult = math.pow(num, 1/i)
        if math.floor(oneResult) == oneResult:
            results += [oneResult]
            exponent += [i-2]
    return results, exponent


def setZaehlungen(num : int): # mehrere Zählungen finden festlegen zum später auslesen
    global zaehlungen
    wasMoon = True
    if zaehlungen[0] == 0:
        wasMoon = True
    else:
        ifIsMoon = moonNumber(zaehlungen[0])
        if ifIsMoon[1] != []:
            wasMoon = False
        else:
            wasMoon = True

    for i in range(zaehlungen[0]+1, num+1):
        ifIsMoon = moonNumber(i)
        if ifIsMoon[1] != []:
            if wasMoon:
                wasMoon = False
                zaehlungen[1][len(zaehlungen[1]) + 1 ] = i
                zaehlungen[2][i] = len(zaehlungen[2]) + 1
        else:
            if not wasMoon:
                wasMoon = True
        zaehlungen[3][i] = len(zaehlungen[2])

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

    parameters(sys.argv)
    toYesDisplayLines = FilterOriginalLines(set(originalLinesRange))
    maxPartLineLen = 0
    print('0 '+str(toYesDisplayLines))
    print('1 '+str(set(originalLinesRange)))
    print('2 '+str(toYesDisplayLines))

    for k in toYesDisplayLines: # n Linien einer Zelle, d.h. 1 EL = n Zellen
        actualPartLineLen = 0
        for m in rowsRange: # eine Zeile immer
            actualPartLineLen += 1
            line=''
            linesEmpty = 0
            for i in realLinesRange: # Teil-Linien nebeneinander als Teil-Spalten
                maxRowsPossible = math.floor( int(shellRowsAmount) / int(textwidth+1))
                #if i < maxRowsPossible and k < 6:
                if i < maxRowsPossible:
                    try:
                        line += colorize(newRows[k][i][m].ljust(textwidth), k, i)+' ' # neben-Einander
                    except:
                        linesEmpty += 1
                        line += colorize(''.ljust(textwidth), k,i ,True)+' ' # neben-Einander
            #if k < 6 and linesEmpty != maxRowsPossible: #and m < actualPartLineLen:
            if linesEmpty != maxRowsPossible: #and m < actualPartLineLen:
                print(line)
                #print(colorize(str(linesEmpty)+' '+str(maxRowsPossible), k))
        if actualPartLineLen > maxPartLineLen:
            maxPartLineLen = actualPartLineLen

