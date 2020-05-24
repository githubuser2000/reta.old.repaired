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
    with open('religion.csv', mode='r') as csv_file:
        relitable = []
        for row in list(csv.reader(csv_file, delimiter=';')):
            relitable += [row]
    for line in relitable:
        for cell in line:
            isItNone = dic.wrap(cell, 21)
            cell2 = tuple()
            rest = cell
            while not isItNone is None:
                cell2 += isItNone
                isItNone = dic.wrap(cell2[-1], 21)
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
                print(str(cell2))
                    #if not cell2 == None:
                    #    for cell3 in cell2:
                    #        print(cell3+'\n')













