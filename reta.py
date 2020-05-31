#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import pyphen
import os
import math
import sys

dic = pyphen.Pyphen(lang='de_DE')
ColumnsRowsAmount, shellRowsAmount = os.popen('stty size', 'r').read().split()
relitable = None
toYesdisplayRows = set()
toNotDisplayRows = set()
infoLog = True
# c nächste silbe
# b nächste Spalte
# a nächste Zeile
#exit()
#originalLinesRange = range(len(newRows))
originalLinesRange = range(120)
#realLinesRange = range(len(newRows[0]))
realLinesRange = range(50)
#rowsRange = range(len(newRows[0][0]))
RowsLen = None
#rowsRange = range(50)
rowsRange = None
#printalx(newRows[0][1][0])

zaehlungen = [0,{},{},{},{}]
textwidth = 21
textheight = 0
nummerierung = True
spaltegestirn = False
breiten = []
primuniverse = False
puniverseprims = set()
#rowsAsNumbers.add(1)
animalsProfessions = False

def printalx(text):
    if infoLog:
        print(text)

def parameters(argv, neg=''):
    global textwidth, textheight, nummerierung, spaltegestirn, breiten, primuniverse, puniverseprims, animalsProfessions
    rowsAsNumbers =  set()
    paramLines = set()
    bigParamaeter=[]
    for arg in argv[1:]:
        if len(arg) > 0 and  arg[0] == '-':
            if len(arg) > 1 and arg[1] == '-' and len(bigParamaeter) > 0 and bigParamaeter[-1] == 'spalten': # unteres Kommando
                if arg[2:9]=='breite=':
                    if arg[9:].isdecimal():
                        textwidth = abs(int(arg[9:]))
                elif arg[2:10]=='breiten=':
                    for breite in arg[10:].split(','):
                        if breite.isdecimal():
                            breiten += [int(breite)]
                elif arg[2:20]=='keinenummerierung':
                    nummerierung = False
                elif arg[2:13]=='religionen=':
                    for religion in arg[13:].split(','):
                        if religion == neg+'sternpolygon':
                            rowsAsNumbers.add(0)
                            rowsAsNumbers.add(6)
                            rowsAsNumbers.add(36)
                        elif religion in [neg+'babylon',neg+'dertierkreiszeichen']:
                            rowsAsNumbers.add(0)
                            rowsAsNumbers.add(36)
                        elif religion in [neg+'gleichfoermigespolygon',neg+'nichtsternpolygon',neg+'polygon']:
                            rowsAsNumbers.add(16)
                            rowsAsNumbers.add(36)
                        elif religion in [neg+'galaxien',neg+'galaxie',neg+'schwarzesonne',neg+'schwarzesonnen',neg+'universum',neg+'universen',neg+'kreis',neg+'kreise',neg+'kugel',neg+'kugeln']:
                            rowsAsNumbers.add(23)
                elif arg[2:11]=='galaxien=' or arg[2:16]=='alteschriften=' or arg[2:9]=='kreise=':
                    for thing in arg[(arg.find('=')+1):].split(','):
                        if thing in [neg+'babylon', neg+'tierkreiszeichen']:
                            rowsAsNumbers.add(1)
                            rowsAsNumbers.add(2)
                        elif thing in [neg+'thomas', neg+'thomasevangelium']:
                            rowsAsNumbers.add(3)
                elif arg[2:] in ['groessenordnung'+neg, 'strukturgroesse'+neg, 'groesse'+neg, 'stufe'+neg]:
                    rowsAsNumbers.add(4)
                    rowsAsNumbers.add(21)
                elif arg[2:] in ['universum'+neg,'transzendentalien'+neg,'strukturalien'+neg]:
                    rowsAsNumbers.add(5)
                elif arg[2:15] in ['menschliches=']:
                    for thing in arg[(arg.find('=')+1):].split(','):
                        if thing in [neg+'liebe',neg+'ethik']:
                            rowsAsNumbers.add(8)
                            rowsAsNumbers.add(9)
                            rowsAsNumbers.add(28)
                        elif thing in [neg+'motive',neg+'motivation',neg+'motiv']:
                            rowsAsNumbers.add(10)
                            rowsAsNumbers.add(18)
                        elif thing in [neg+'errungenschaften',neg+'ziele',neg+'erhalten']:
                            rowsAsNumbers.add(11)
                        elif thing in [neg+'erwerben',neg+'erlernen',neg+'lernen',neg+'evolutionaer']:
                            rowsAsNumbers.add(12)
                        elif thing in [neg+'brauchen',neg+'benoetigen',neg+'notwendig']:
                            rowsAsNumbers.add(13)
                            rowsAsNumbers.add(14)
                        elif thing in [neg+'krankheit',neg+'pathologisch',neg+'pathologie',neg+'psychiatrisch']:
                            rowsAsNumbers.add(24)
                        elif thing in [neg+'kreativ',neg+'kreativitaet']:
                            rowsAsNumbers.add(27)
                        elif thing in [neg+'anfuehrer',neg+'chef']:
                            rowsAsNumbers.add(29)
                        elif thing in [neg+'beruf',neg+'berufe']:
                            rowsAsNumbers.add(30)
                        elif thing in [neg+'loesungen',neg+'loesung']:
                            rowsAsNumbers.add(31)
                        elif thing in [neg+'musik']:
                            rowsAsNumbers.add(33)
                elif arg[2:12] == 'procontra=' or arg[2:16] == 'dagegendafuer=':
                    for thing in arg[(arg.find('=')+1):].split(','):
                        if thing in [neg+'pro',neg+'dafeuer']:
                            rowsAsNumbers.add(17)
                        elif thing in [neg+'contra',neg+'dagegen']:
                            rowsAsNumbers.add(15)
                elif arg[2:7+len(neg)] == 'licht'+neg:
                            rowsAsNumbers.add(20)
                elif arg[2:12] == 'bedeutung=':
                    for thing in arg[(arg.find('=')+1):].split(','):
                        if thing in [neg+'primzahlen',neg+'vielfache',neg+'vielfacher']:
                            rowsAsNumbers.add(19)
                        elif thing in [neg+'anwendungdersonnen',neg+'anwendungenfuermonde']:
                            rowsAsNumbers.add(22)
                        elif thing in [neg+'zaehlung',neg+'zaehlungen']:
                            rowsAsNumbers.add(25)
                        elif thing in [neg+'liebe',neg+'ethik']:
                            rowsAsNumbers.add(26)
                        elif thing in [neg+'jura', neg+'gesetzeslehre', neg+'recht']:
                            rowsAsNumbers.add(34)
                        elif thing in [neg+'vollkommenheit', neg+'geist']:
                            rowsAsNumbers.add(35)
                        elif thing in [neg+'gestirn', neg+'mond', neg+'sonne', neg+'planet']:
                            spaltegestirn = True
                elif arg[2:11+len(neg)] == 'symbole'+neg:
                    rowsAsNumbers.add(36)
                    rowsAsNumbers.add(37)
                elif arg[2:30] == 'primzahlvielfachesuniversum=':
                    for word in arg[30:].split(','):
                        if word.isdecimal():
                            primuniverse = True
                            puniverseprims.add(int(word))




            if len(arg) > 1 and arg[1] == '-' and len(bigParamaeter) > 0 and bigParamaeter[-1] == 'zeilen': # unteres Kommando
                if arg[2:7]=='zeit=':
                    for subpara in arg[7:].split(','):
                        if neg+'=' == subpara:
                            paramLines.add('=')
                        elif neg+'<' == subpara:
                            paramLines.add('<')
                        elif neg+'>' == subpara:
                            paramLines.add('>')
                elif arg[2:11]=='zaehlung=':
                    for word in arg[11:].split(','):
                        if (word.isdecimal() or (word[1:].isdecimal() and word[0] == neg)) and ((int(word) > 0 and neg == '' ) or (int(word) < 0 and neg != '' )):
                            paramLines.add(str(abs(int(word)))+'z')
                elif arg[2:15]=='hoehemaximal=':
                    if arg[15:].isdecimal():
                        textheight = abs(int(arg[15:]))
                elif arg[2:6]=='typ=':
                    for word in arg[6:].split(','):
                        if word == neg+'sonne':
                            paramLines.add('sonne')
                        elif word == neg+'schwarzesonne':
                            paramLines.add('schwarzesonne')
                        elif word == neg+'planet':
                            paramLines.add('planet')
                        elif word == neg+'mond':
                            paramLines.add('mond')
                elif arg[2:21]=='vielfachevonzahlen=':
                    for word in arg[21:].split(','):
                        if (word.isdecimal() or (word[1:].isdecimal() and word[0] == neg)) and ((int(word) > 0 and neg == '' ) or (int(word) < 0 and neg != '' )):
                            paramLines.add(str(abs(int(word)))+'v')
                elif arg[2:20]=='primzahlvielfache=':
                    for word in arg[20:].split(','):
                        if (word.isdecimal() or (word[1:].isdecimal() and word[0] == neg)) and ((int(word) > 0 and neg == '' ) or (int(word) < 0 and neg != '' )):
                            paramLines.add(str(abs(int(word)))+'p')
                elif arg[2:22]=='vorhervonausschnitt=':
                    paramLines |= parametersBereich(arg[22:],'a',neg)
                elif arg[2:21]=='nachtraeglichdavon=':
                    paramLines |= parametersBereich(arg[21:],'z',neg)
#                    if arg[21:21+len(neg)] == neg:
#                        maybeAmounts=arg[21+len(neg):].split('-')
#                        if len(maybeAmounts) == 1 and maybeAmounts[0].isdecimal() and maybeAmounts[0] != "0":
#                            paramLines.add('1-z-'+maybeAmounts[0])
#                        elif len(maybeAmounts) == 2 and maybeAmounts[0].isdecimal() and maybeAmounts[0] != "0" and maybeAmounts[1].isdecimal() and maybeAmounts[1] != "0":
#                            paramLines.add(maybeAmounts[0]+'-z-'+maybeAmounts[1])
            if len(arg) > 1 and arg[1] == '-' and len(bigParamaeter) > 0 and bigParamaeter[-1] == 'kombination': # unteres Kommando
                if arg[2:6]=='und=':
                    for word in arg[6:].split(','):
                        if (word.isdecimal() or (word[1:].isdecimal() and word[0] == neg)) and ((int(word) > 0 and neg == '' ) or (int(word) < 0 and neg != '' )):
                            animalsProfessions = True
                            paramLines.add(str(abs(int(word)))+'ku')
                elif arg[2:7]=='oder=':
                    for word in arg[7:].split(','):
                        if (word.isdecimal() or (word[1:].isdecimal() and word[0] == neg)) and ((int(word) > 0 and neg == '' ) or (int(word) < 0 and neg != '' )):
                            animalsProfessions = True
                            paramLines.add(str(abs(int(word)))+'ko')
                elif arg[2:]=='vonangezeigten'+neg:
                    animalsProfessions = True
                    paramLines.add("ka")
            else: # oberes Kommando
                if arg[1:] in ['zeilen','spalten','kombination']:
                    bigParamaeter += [arg[1:]]
    return paramLines, rowsAsNumbers

def parametersBereich( bereiche1 : str, symbol : str, neg : str):
    results = set()
#    if bereiche1[:len(neg)] == neg:
#        bereiche2 = bereiche1[len(neg):].split(',')
#    else:
#        bereiche2 = bereiche1[len(neg):].split(',')
    for bereiche3 in (bereiche1[len(neg):].split(',') if bereiche1[:len(neg)] == neg else bereiche1.split(',')):
        printalx("aa "+bereiche3)
        if ( len(bereiche3) > len(neg) and bereiche3 == neg+bereiche3[len(neg):] and len(neg) > 0) or (len(bereiche3)>0 and (neg+bereiche3[0]).isdigit()):
            printalx(bereiche3+' '+str(len(neg)))
            maybeAmounts = bereiche3[len(neg):].split('-')
            printalx(str(maybeAmounts)+' '+str(neg))
            if len(maybeAmounts) == 1 and maybeAmounts[0].isdecimal() and maybeAmounts[0] != "0":
                results.add('1-'+symbol+'-'+maybeAmounts[0])
            elif len(maybeAmounts) == 2 and maybeAmounts[0].isdecimal() and maybeAmounts[0] != "0" and maybeAmounts[1].isdecimal() and maybeAmounts[1] != "0":
                results.add(maybeAmounts[0]+'-'+symbol+'-'+maybeAmounts[1])
    return results

def deleteDoublesInSets(set1 : set, set2 : set) -> tuple:
    intersection = set1 & set2
    return set1 - intersection, set2 - intersection

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


def FilterOriginalLines(numRange : set, paramLines : set) -> set: # ich wollte je pro extra num, nun nicht mehr nur sondern modular ein mal alles und dann pro nummer in 2 funktionen geteilt
    global zaehlungen

    def diffset(wether, a : set, b : set) -> set:
        if wether:
            #result = a.difference(b)
            result = a - b
            if result is None:
                return set()
            else:
                return result
        return a
    numRange.remove(0)
    def cutset(wether, a : set, b : set) -> set:
        if wether:
            #result = a.intersection(b)
            result = a & b
            #printalx("x "+str(result))
            if result is None:
                return set()
            else:
                return result
        return a

    numRangeYesZ = set()
    if_a_AtAll = False
    for condition in paramLines:
        if '-a-' in condition:
            if_a_AtAll = True
            a = fromUntil(condition.split('-a-'))
            for n in numRange.copy():
                if a[0] <= n and a[1] >= n:
                    #numRange.remove(n)
                    numRangeYesZ.add(n)

    numRange = cutset(if_a_AtAll, numRange, numRangeYesZ)
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

    #printalx("x0 "+str(numRange))
    #printalx("y0 "+str(paramLines))
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
    #printalx("xi "+str(numRangeYesZ))
    #printalx("xt "+str(numRange))
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

    #printalx("x2 "+str(numRangeYesZ))
    numRange = cutset(ifTypAtAll, numRange, numRangeYesZ)
    #printalx("x3 "+str(numRange))

    primMultiples = []
    ifPrimAtAll = False
    for condition in paramLines:
        if len(condition) > 1 and condition[-1] == 'p' and condition[:-1].isdecimal():
            ifPrimAtAll = True
            primMultiples += [int(condition[:-1])]

    #printalx("x3 "+str(numRange))
    numRangeYesZ = set()
    for n in numRange:
        if isPrimMultiple(n, primMultiples):
            numRangeYesZ.add(n)
    numRange = cutset(ifPrimAtAll, numRange, numRangeYesZ)
    #printalx("x4 "+str(numRangeYesZ))
    #printalx("x5 "+str(numRange))


    ifMultiplesFromAnyAtAll = False
    anyMultiples = []
    for condition in paramLines:
        if len(condition) > 1 and condition[-1] == 'v' and condition[:-1].isdecimal():
            ifMultiplesFromAnyAtAll = True
            anyMultiples += [int(condition[:-1])]

    if ifMultiplesFromAnyAtAll:
        numRangeYesZ = set()
        for n in numRange:
            #printalx(str(n))
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
#    printalx("w "+str(isPrimMultiple(e, [2])))

def wrapping(text : str, length : int):
    if len(text) > length-1:
        isItNone = dic.wrap(text, length-1)
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

def fillBoth(liste1,liste2):
    while len(liste1) < len(liste2):
        liste1 += ['']
    while len(liste2) < len(liste1):
        liste2 += ['']
    return liste1, liste2


if True:
    with open('religion.csv', mode='r') as csv_file:
        for col in csv.reader(csv_file, delimiter=';'):
            RowsLen = len(col)
            rowsRange  = range(RowsLen)

    paramLines, rowsAsNumbers = parameters(sys.argv)
    paramLinesNot, rowsAsNumbersNot = parameters(sys.argv, '-')
    printalx(str(paramLines)+' '+str(rowsAsNumbers))
    printalx(str(paramLinesNot)+' '+str(rowsAsNumbersNot))

    paramLines, paramLinesNot = deleteDoublesInSets(paramLines, paramLinesNot)
    rowsAsNumbers, rowsAsNumbersNot = deleteDoublesInSets(rowsAsNumbers, rowsAsNumbersNot)
    printalx(str(paramLines)+' '+str(rowsAsNumbers))
    printalx(str(paramLinesNot)+' '+str(rowsAsNumbersNot))


    with open('religion.csv', mode='r') as csv_file:
        relitable = []
        for col in csv.reader(csv_file, delimiter=';'):
            relitable += [col]
    headingsAmount = len(relitable[0])
    if primuniverse:
        with open('primenumbers.csv', mode='r') as csv_file:
            relitable, primuniversetable = fillBoth(relitable, list(csv.reader(csv_file, delimiter=';')))
            lastlen = 0
            maxlen = 0
            for i, (primcol, relicol) in enumerate(zip(primuniversetable, relitable)):
                lastlen = len(primcol)
                if lastlen > maxlen:
                    maxlen = lastlen
                relitable[i] += list(primcol) + [''] * (maxlen-len(primcol))
                #printalx(str(list(primcol)))
                if i == 0:
                    for u, heading in enumerate(relitable[0]):
                        if heading.isdecimal() and int(heading) in puniverseprims and u >= headingsAmount:
                            printalx(str(heading)+'ö'+str(puniverseprims))
                            rowsAsNumbers.add(int(u))

               # print(str(len(primuniversetable[i]))+' '+str(len(relitable[i])))
                #print(str((relitable[i])))
    headingsAmount = len(relitable[0])
    if animalsProfessions:
        with open('animalsProfessions.csv', mode='r') as csv_file:
            relitable, animalsProfessionstable = fillBoth(relitable, list(csv.reader(csv_file, delimiter=';')))
            lastlen = 0
            maxlen = 0
            for i, (animcol, relicol) in enumerate(zip(animalsProfessionstable, relitable)):
                lastlen = len(animcol)
                if lastlen > maxlen:
                    maxlen = lastlen
                relitable[i] += list(animcol) + [''] * (maxlen-len(animcol))
                printalx(str(list(animcol)))
                if i == 0:
                    for u, heading in enumerate(relitable[0]):
                        if u >= headingsAmount and u < headingsAmount + len(animalsProfessionstable[0]):
                            printalx(str(heading)+'ö'+str(puniverseprims))
                            rowsAsNumbers.add(int(u))

    printalx(str(paramLines)+' '+str(rowsAsNumbers))
    headingsAmount = len(relitable[0])
    newRows = []
    if spaltegestirn:
        if len(relitable) > 0:
            rowsAsNumbers.add(len(relitable[0]))
        #moonNumber
        for i, line in enumerate(relitable):
            if i == 0:
                line += ['Gestirn']
            else:
                if moonNumber(i)[1] != []:
                    text = 'Mond'
                else:
                    text = 'Sonne'
                if i %  2 == 0:
                    line += [text+', Planet']
                else:
                    line += [text]
    #    printalx(str(relitable))
    if len(relitable) > 0:
        RowsLen = len(relitable[0])
        rowsRange  = range(RowsLen)
    headingsAmount = RowsLen
    onlyShowRowAmount = len(rowsAsNumbers)
    onlyShowRowNum = 0
    finallyDisplayLines = FilterOriginalLines(set(originalLinesRange), paramLines)
    #printalx('s1 '+str(finallyDisplayLines))
    if not len(paramLinesNot) == 0:
        finallyDisplayLines -= FilterOriginalLines(set(originalLinesRange), paramLinesNot)
    #printalx('s2 '+str(finallyDisplayLines))
    finallyDisplayLines.add(0)
    finallyDisplayLines= list(finallyDisplayLines)
    finallyDisplayLines.sort()
#    maxPartLineLen = 0
    numlen = len(str(finallyDisplayLines[-1]))
    printalx('2 '+str(finallyDisplayLines))

    for u, line in enumerate(relitable):
        new2Lines = []
        rowsToDisplay = 0
        for t, cell in enumerate(line):
            if t in rowsAsNumbers and u in finallyDisplayLines:
                #printalx(str(u)+' '+str(t)+' '+str(relitable[u][t]))
                rowsToDisplay += 1
                newLines = [[]]*headingsAmount
                #printalx(str(rowsToDisplay+(1 if nummerierung else 0))+' '+str(len(breiten)))
                if rowsToDisplay+(1 if nummerierung else 0) <= len(breiten) + 1:
                    certaintextwidth = breiten[rowsToDisplay+(-1 if nummerierung else -2)]
                else:
                    certaintextwidth = textwidth
                isItNone = wrapping(cell, certaintextwidth)
                cell2 = tuple()
                rest = cell
                while not isItNone is None:
                    cell2 += isItNone
                    isItNone = wrapping(cell2[-1], certaintextwidth)
                    rest = cell2[-1]
                    cell2 = cell2[:-1]
                    if len(rest) > certaintextwidth and isItNone is None:
                        cell2 += (rest[0:certaintextwidth-1],)
                        isItNone = (rest[certaintextwidth:],)
                else:
                    cell2 += (rest[0:certaintextwidth-1],)
                    for k,cellInCells in enumerate(cell2):
                        if k < len(newLines):
                            newLines[k] += [cellInCells]
                        else:
                            pass
                new2Lines += [newLines[t]]
        if new2Lines != []:
            newRows += [new2Lines]
    #printalx(str(newRows))
    maxCellTextLen = {}
    #for k in finallyDisplayLines: # n Linien einer Zelle, d.h. 1 EL = n Zellen
    for k, (f, r) in enumerate(zip(newRows,finallyDisplayLines)): # n Linien einer Zelle, d.h. 1 EL = n Zellen
        for iterWholeLine, m in enumerate(rowsRange): # eine Bildhschirm-Zeile immer
            #for i in rowsAsNumbers: # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
            for i, c in enumerate(newRows[k]): # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                if not i in maxCellTextLen:
                    try:
                        maxCellTextLen[i] = len(newRows[k][i][m])
                    except:
                        pass
                else:
                    try:
                        textLen = len(newRows[k][i][m])
                        if textLen > int(maxCellTextLen[i]):
                            maxCellTextLen[i] = textLen
                    except:
                        pass

    #for k in finallyDisplayLines: # n Linien einer Zelle, d.h. 1 EL = n Zellen
    #printalx("sdfsad"+str(len(newRows)))
    for k, (f, r) in enumerate(zip(newRows,finallyDisplayLines)): # n Linien einer Zelle, d.h. 1 EL = n Zellen
#        actualPartLineLen = 0
        for iterWholeLine, m in enumerate(rowsRange): # eine Bildhschirm-Zeile immer
#            actualPartLineLen += 1
            line='' if not nummerierung else ( ''.rjust(numlen + 1) if iterWholeLine != 0 else (str(r)+' ').rjust(numlen + 1) )
            rowsEmpty = 0
            #for i in realLinesRange: # Teil-Linien nebeneinander als Teil-Spalten
            maxRowsPossible = math.floor( int(shellRowsAmount) / int(textwidth+1))
            #maxCellTextLen = 0
            #for i in rowsAsNumbers: # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
            for i, c in enumerate(newRows[k]): # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                #maxRowsPossible = math.floor( int(shellRowsAmount) / int(textwidth+1))
                #if i < maxRowsPossible and k < 6:
                #if i < maxRowsPossible:
                if i+(1 if nummerierung else 0) <= len(breiten):
                    certaintextwidth = breiten[i+(0 if nummerierung else -1)]
                else:
                    certaintextwidth = textwidth
                if certaintextwidth > maxCellTextLen[i]:
                    i_textwidth = maxCellTextLen[i]
                else:
                    i_textwidth = certaintextwidth
                try:
                    #line += colorize(newRows[k][i][m].replace('\n', '').ljust(textwidth if textwidth < maxCellTextLen[i] else maxCellTextLen[i]), k, i)+' ' # neben-Einander
                    line += colorize(newRows[k][i][m].replace('\n', '').ljust(i_textwidth), r, i)+' ' # neben-Einander
                except:
                    rowsEmpty += 1
                    line += colorize(''.ljust(i_textwidth), r,i ,True)+' ' # neben-Einander
            #if k < 6 and rowsEmpty != maxRowsPossible: #and m < actualPartLineLen:
#            printalx("sdf "+str(len(rowsAsNumbers))+' '+str(rowsEmpty))
            if rowsEmpty != len(rowsAsNumbers) and ( iterWholeLine < textheight or textheight == 0): #and m < actualPartLineLen:
                print(line)
                #printalx(colorize(str(rowsEmpty)+' '+str(maxRowsPossible), k))
#        if actualPartLineLen > maxPartLineLen:
#            maxPartLineLen = actualPartLineLen

