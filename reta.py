#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import pyphen
import os
import math

dic = pyphen.Pyphen(lang='de_DE')
shellRowsAmount, ColumnsRowsAmount = os.popen('stty size', 'r').read().split()
#def wortumbruch(text,maxlen):
#    text = text.split()
#    wordLens = 0
#    wordAmountPerLine = 0
#    newtext3 = []
#    newtext4 = ''
#    for i,word in enumerate(text):
#        wordLens += 1 + len(word)
#        wordAmountPerLine += 1
#        if wordLens > maxlen:
#            if wordAmountPerLine == 1:
#                restword = word
#                while restword != word and len(restword) > maxlen:
#                    newtext3 += [restword[:maxlen]]
#                    newtext3 += ['\n']
#                    restword = word[maxlen:]
#                if wordAmountPerLine == 1 and len(restword) <= maxlen:
#                    newtext3 += [restword[maxlen:]]
#            else:
#                newtext3 += ['\n']
#                newtext3 += [word]
#            wordLens = 0
#            wordAmountPerLine = 0
#        else:
#            newtext3 += [word]
#        newtext4 += '_'.join(newtext3) + '_'
#        newtext3 = []
#    return str(newtext4)

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
        #newLines[20] += ['a']
        for t, cell in enumerate(line):
            newLines = [[]]*headingsAmount
            isItNone = dic.wrap(cell, textwidth)
            cell2 = tuple()
            rest = cell
            while not isItNone is None:
                cell2 += isItNone
                isItNone = dic.wrap(cell2[-1], textwidth)
                rest = cell2[-1]
                cell2 = cell2[:-1]
#                print(str(cell2))
#                exit()
                # 2 sind da, wir wollen 4
                # 1 + 2 unvollständig
                # 1 + 2 + rest
                #
                # 1 + neues 2 + neues 3
                #
                # 1 + 2 + neues 3 + neues 4
            else:
                cell2 += (rest,)
                #print(str(len(cell2)))
                for k,cellInCells in enumerate(cell2):
                    #print(str(cellInCells))
                    if k < len(newLines):
                        newLines[k] += [cellInCells]
                    else:
                        pass
                        #print("Fehler A")
                #print(str(newLines[t]))
                #exit()
                    #if not cell2 == None:
                    #    for cell3 in cell2:
                    #        print(cell3+'\n')
                #print(str(line))
        #print(str(newLines[0]))
        #exit()
            new2Lines += [newLines[t]]
        newRows += [new2Lines]
        #print(str((new2Lines)))
        #exit()
    #new2Lines = list(zip(*newRows))
    #for line in new2Lines:
    #    print(str(line[0]))
    #exit()
    #new4Line = ''
    #print(str(new2Lines))
    #print(new2Lines[0][0])
    #print(str(newRows[0][0][0]))
    # newRows: [a][b][c]
    # c nächste silbe
    # b nächste Spalte
    # a nächste Zeile
    #exit()
    originalLinesRange = range(len(newRows))
    realLinesRange = range(len(newRows[0]))
    rowsRange = range(len(newRows[0][0]))

    #print(newRows[0][1][0])
    #exit()
    for k in originalLinesRange:
        for m in rowsRange:
            line=''
            for i in realLinesRange:
                iterRealLinesAmount = math.floor( int(shellRowsAmount) / int(textwidth))
                if i < iterRealLinesAmount and k < 6:
                    #print(newRows[k][i][m])
                    line += newRows[k][i][m].ljust(textwidth)+' '
            print(line)
        exit()
    for k,new2Line in enumerate(newRows): # nächste Zeile
        #new3Line = ''
        for i,line in enumerate(new2Line): # nächste Spalte
            for m, partline in enumerate(line): # nächste silbe
                # Ich brauche zuerst nächste Spalte, dann nächste Silbentrannung
                # und dann nächste Zeile
                print(partline)
                exit()
            #partLines = ''
            #for partLine in line:
            #line.ljust(textwidth)
            #new3Line += line.ljust(textwidth)+' '
            #if i > 3:
            #    break
        #new4Line += new3Line.ljust(textwidth)
        #print(new4Line)
#                break
 #1                   exit()












