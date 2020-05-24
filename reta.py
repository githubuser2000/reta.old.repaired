#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import pyphen

dic = pyphen.Pyphen(lang='de_DE')

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
    new2Lines = zip(*newRows)
    print(str(list(new2Lines[0])))
    exit()
    new4Line = ''
    for k,new2Line in enumerate(new2Lines):
        new3Line = ''
        for i,line in enumerate(new2Line):
            #partLines = ''
            #for partLine in line:
            line.ljust(textwidth)
            new3Line += line.ljust(textwidth)+' '
            if i > 3:
                break
        new4Line += new3Line.ljust(textwidth)
        print(new4Line)
#                break
 #1                   exit()












