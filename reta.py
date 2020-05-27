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

zaehlungen = [0,{},{},{},{}]
textwidth = 21
textheight = 0
numerierung = True
spalten =  set()
#spalten.add(1)

def parameters(argv):
    global paramLines, paramRows, textwidth, textheight, numerierung, spalten
    bigParamaeter=[]
    for arg in argv[1:]:
        if len(arg) > 0 and  arg[0] == '-':
            if len(arg) > 1 and arg[1] == '-' and len(bigParamaeter) > 0 and bigParamaeter[-1] == 'spalten': # unteres Kommando
                if arg[2:9]=='breite=':
                    if arg[9:].isdecimal():
                        textwidth = abs(int(arg[9:]))
                elif arg[2:20]=='keinenummerierung':
                    numerierung = False
                elif arg[2:13]=='religionen=':
                    for religion in arg[13:].split(','):
                        if religion == 'sternpolygon':
                            spalten.add(0)
                            spalten.add(6)
                        elif religion in ['babylon','dertierkreiszeichen']:
                            spalten.add(0)
                        elif religion in ['gleichfoermigespolygon','nichtsternpolygon','polygon']:
                            spalten.add(16)
                elif arg[2:11]=='galaxien=' or arg[2:16]=='alteschriften=' or arg[2:9]=='kreise=':
                    for thing in arg[(arg.find('=')+1):].split(','):
                        if thing in ['babylon','tierkreiszeichen']:
                            spalten.add(1)
                            spalten.add(2)
                        elif thing in ['thomas','thomasevangelium']:
                            spalten.add(3)
                elif arg[2:] in ['groessenordnung','strukturgroesse','groesse','stufe']:
                    spalten.add(4)
                elif arg[2:] in ['universum','transzendentalien','strukturalien']:
                    spalten.add(5)


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
                elif arg[2:15]=='hoehemaximal=':
                    if arg[15:].isdecimal():
                        textheight = abs(int(arg[15:]))
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
                elif arg[2:21]=='vielfachevonzahlen=':
                    for word in arg[21:].split(','):
                        if word.isdecimal():
                            paramLines.add(word+'v')
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


def FilterOriginalLines(numRange : set) -> set: # ich wollte je pro extra num, nun nicht mehr nur sondern modular ein mal alles und dann pro nummer in 2 funktionen geteilt
    global toYesDisplayLines, toYesdisplayRows, zaehlungen, paramLines, paramRows, toNotDisplayLines
    def diffset(wether, a : set, b : set) -> set:
        if wether:
            result = a.difference(b)
            if result is None:
                return set()
            else:
                return result
        return a
    numRange.remove(0)
    def cutset(wether, a : set, b : set) -> set:
        if wether:
            result = a.intersection(b)
            #print("x "+str(result))
            if result is None:
                return set()
            else:
                return result
        return a

    for condition in paramLines:
        if '-a-' in condition:
            a = fromUntil(condition.split('-a-'))
            for n in numRange.copy():
                if a[0] > n or a[1] < n:
                    numRange.remove(n)
                    toNotDisplayLines.add(n)

    numRangeYesZ = set()
    ifZeitAtAll = False

    for condition in paramLines:
        if '=' == condition:
            ifZeitAtAll = True
            numRangeYesZ.add(10)
        elif '<' == condition:
            ifZeitAtAll = True
            for n in numRange:
                if n < 10:
                    numRangeYesZ.add(n)
        elif '>' == condition:
            ifZeitAtAll = True
            for n in numRange:
                if n > 10:
                    numRangeYesZ.add(n)

    numRange = cutset(ifZeitAtAll, numRange, numRangeYesZ)

    #print("x0 "+str(numRange))
    #print("y0 "+str(paramLines))
    numRangeYesZ = set()
    ifZaehlungenAtAll = False
    for condition in paramLines:
        if len(condition) > 1 and condition[-1] == 'z' and condition[0:-1].isdecimal(): # ist eine von mehreren Zählungen
            if not ifZaehlungenAtAll:
                setZaehlungen(originalLinesRange[-1])
                ifZaehlungenAtAll = True
            zaehlungGesucht = int(condition[0:-1]) # eine zählung = eine zahl, beginnend minimal ab 1
            for n in numRange: # nur die nummern, die noch infrage kommen
                #zaehlungen = [0,{},{},{}]
                if zaehlungen[3][n] == int(zaehlungGesucht): # 1-4:1,5-9:2 == jetzt ?
                    numRangeYesZ.add(n)
                    #numRange.remove(n)
    #print("xi "+str(numRangeYesZ))
    #print("xt "+str(numRange))
    numRange = cutset(ifZaehlungenAtAll, numRange, numRangeYesZ)
   # set().add
    #exit()
    ifTypAtAll = False
    numRangeYesZ = set()
    def moonsun(MoonNotSun : bool, numRangeYesZ : set):
        if not ifZaehlungenAtAll:
            setZaehlungen(originalLinesRange[-1])
        for n in numRange:
            if ( zaehlungen[4][n][0] != [] ) == MoonNotSun:
                numRangeYesZ.add(n)
        return numRangeYesZ

    for condition in paramLines:
        if 'mond' in condition:
            numRangeYesZ, ifTypAtAll = moonsun(True, numRangeYesZ), True
        elif 'sonne' in condition:
            numRangeYesZ, ifTypAtAll = moonsun(False, numRangeYesZ), True
        elif 'planet' in condition:
            ifTypAtAll = True
            for n in numRange:
                if n % 2 == 0:
                    numRangeYesZ.add(n)

    #print("x2 "+str(numRangeYesZ))
    numRange = cutset(ifTypAtAll, numRange, numRangeYesZ)
    #print("x3 "+str(numRange))

    primMultiples = []
    ifPrimAtAll = False
    for condition in paramLines:
        if len(condition) > 1 and condition[-1] == 'p' and condition[:-1].isdecimal():
            ifPrimAtAll = True
            primMultiples += [int(condition[:-1])]

    #print("x3 "+str(numRange))
    if ifPrimAtAll:
        numRangeYesZ = set()
        for n in numRange:
            if isPrimMultiple(n, primMultiples):
                numRangeYesZ.add(n)
        numRange = cutset(ifTypAtAll, numRange, numRangeYesZ)
    #print("x4 "+str(numRangeYesZ))
    #print("x5 "+str(numRange))


    ifMultiplesFromAnyAtAll = False
    anyMultiples = []
    for condition in paramLines:
        if len(condition) > 1 and condition[-1] == 'v' and condition[:-1].isdecimal():
            ifMultiplesFromAnyAtAll = True
            anyMultiples += [int(condition[:-1])]

    if ifMultiplesFromAnyAtAll:
        numRangeYesZ = set()
        for n in numRange:
            #print(str(n))
            for divisor in anyMultiples:
                if n % divisor == 0:
                    numRangeYesZ.add(n)
        numRange = cutset(ifMultiplesFromAnyAtAll, numRange, numRangeYesZ)


    ifNachtraeglichAtAll = False
    for condition in paramLines:
        if '-z-' in condition:
            if not ifNachtraeglichAtAll:
                numRange = list(numRange)
                numRange.sort()
                ifNachtraeglichAtAll = True
            a = fromUntil(condition.split('-z-'))
            for i, n in enumerate(numRange.copy()):
                if a[0] - 1 > i or a[1] - 1 < i:
                    numRange.remove(n)
    if ifNachtraeglichAtAll:
        numRange = set(numRange)
    return numRange

def primFak(n : int):
    faktoren = []
    z = n
    while z > 1:
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
        faktoren += [p]
        z = z // p
    return faktoren

def primRepeat(n):
    n.reverse()
    c = 1
    b = None
    d = []
    for a in n:
        if b == a:
            c += 1
        else:
            c = 1
        d += [[a,c]]
        b = a
    d.reverse()
    b = None
    f = []
    for e,g in d:
        if b != e:
            if g == 1:
                f += [(e,1)]
            else:
                f += [(e,g)]
        b = e
    return f
def primMultiple(n : int) -> list:
    multiples = [(1,n)]
    for prim in primRepeat(primFak(n)):
        multiples += [(prim[0],round(n / prim[0]))]
    return multiples

def isPrimMultiple(isIt : int, multiples1 : list, dontReturnList = True):
    areThey = []
    multiples2 = primMultiple(isIt)
    for multiple1 in multiples1:
        for multiple2 in multiples2:
            areThey += [True if multiple1 == multiple2[1] else False]
            if dontReturnList and areThey[-1]:
                return True
    if dontReturnList:
        return False
    return areThey

#for e in range(1,11):
#    print("w "+str(isPrimMultiple(e, [2])))

def wrapping(text : str, length : int):
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
    elif len(primFak(num)) == 1:
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
    global zaehlungen # [bis zu welcher zahl, {zaehlung:zahl},{zahl:zaehlung},{jede zahl,zugehoerigeZaehlung}]
    wasMoon = True
    if zaehlungen[0] == 0:
        isMoon = True
    else:
        isMoon = moonNumber(zaehlungen[0])[0] != []

    for i in range(zaehlungen[0]+1, num+1):
        wasMoon = isMoon
        moonType = moonNumber(i)
        isMoon = moonType[0] != []
        if wasMoon and not isMoon:
            isMoon = False
            zaehlungen[1][len(zaehlungen[1]) + 1 ] = i
            zaehlungen[2][i] = len(zaehlungen[2]) + 1
        zaehlungen[3][i] = len(zaehlungen[2])
        zaehlungen[4][i] = moonType

if True:
    parameters(sys.argv)
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
                if len(rest) > textwidth and isItNone is None:
                    cell2 += (rest[0:textwidth-1],)
                    isItNone = (rest[textwidth:],)
            else:
                cell2 += (rest[0:textwidth-1],)
                for k,cellInCells in enumerate(cell2):
                    if k < len(newLines):
                        newLines[k] += [cellInCells]
                    else:
                        pass
            new2Lines += [newLines[t]]
        newRows += [new2Lines]

    finallyDisplayLines = FilterOriginalLines(set(originalLinesRange))
    finallyDisplayLines.add(0)
    finallyDisplayLines= list(finallyDisplayLines)
    finallyDisplayLines.sort()
#    maxPartLineLen = 0
    numlen = len(str(finallyDisplayLines[-1]))
    print('2 '+str(finallyDisplayLines))

    maxCellTextLen = {}
    for k in finallyDisplayLines[1:]: # n Linien einer Zelle, d.h. 1 EL = n Zellen
        for iterWholeLine, m in enumerate(rowsRange): # eine Bildhschirm-Zeile immer
            maxCellTextLen2 = {}
            for i in spalten: # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                if not (i in maxCellTextLen and k in maxCellTextLen[i]):
                    try:
                        maxCellTextLen2[k] = len(newRows[k][i][m])
                        print("_sedftg "+str(i)+' '+str(k))
#                        print('e'+str(len(newRows[k][i][m]))+' '+str(newRows[k][i][m]))
                    except:
                        maxCellTextLen2[k] = 0
                    if not i in maxCellTextLen:
                        maxCellTextLen[i] = maxCellTextLen2
                    else:
                        maxCellTextLen[i] = {**maxCellTextLen[i], **maxCellTextLen2}
#                    print('f'+str(k))
                else:
#                    print('g'+str(maxCellTextLen[i][k]))
                    try:
                        textLen = len(newRows[k][i][m])
#                        print('h'+str(k))
                        if textLen > int(maxCellTextLen[i][k]):
                            print("sedftg "+str(maxCellTextLen[i][k])+' '+str(i)+' '+str(k))
                            maxCellTextLen[i][k] = textLen
                    except:
                        pass
    print(str(maxCellTextLen))
#    maxPartLineLen = 0

if False:
    for k in finallyDisplayLines: # n Linien einer Zelle, d.h. 1 EL = n Zellen
#        actualPartLineLen = 0
        for iterWholeLine, m in enumerate(rowsRange): # eine Bildhschirm-Zeile immer
#            actualPartLineLen += 1
            line='' if not numerierung else ( ''.rjust(numlen + 1) if iterWholeLine != 0 else (str(k)+' ').rjust(numlen + 1) )
            linesEmpty = 0
            #for i in realLinesRange: # Teil-Linien nebeneinander als Teil-Spalten
            maxRowsPossible = math.floor( int(shellRowsAmount) / int(textwidth+1))
            maxCellTextLen = 0
            for i in spalten: # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                #maxRowsPossible = math.floor( int(shellRowsAmount) / int(textwidth+1))
                #if i < maxRowsPossible and k < 6:
                #if i < maxRowsPossible:
                if True:
                    try:
                        #line += colorize(newRows[k][i][m].ljust(textwidth), k, i)+' ' # neben-Einander
                        #print(str(maxCellTextLen[i][k]))
                        #line += colorize(newRows[k][i][m].replace('\n', '').ljust(textwidth if True else maxCellTextLen[i][k]), k, i)+' ' # neben-Einander
                        line += colorize(newRows[k][i][m].replace('\n', '').ljust(textwidth), k, i)+' ' # neben-Einander
                    except:
                        linesEmpty += 1
                        line += colorize(''.ljust(textwidth), k,i ,True)+' ' # neben-Einander
            #if k < 6 and linesEmpty != maxRowsPossible: #and m < actualPartLineLen:
            if linesEmpty != maxRowsPossible and ( iterWholeLine < textheight or textheight == 0): #and m < actualPartLineLen:
                print(line)
                #print(colorize(str(linesEmpty)+' '+str(maxRowsPossible), k))
#        if actualPartLineLen > maxPartLineLen:
#            maxPartLineLen = actualPartLineLen

