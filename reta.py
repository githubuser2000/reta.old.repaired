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
            cell2 = dic.wrap(cell, 21)
            if len(cell2) > 1:
                second = dic.wrap(cell2[1], 21)
                if not second is None:
                    cell2 = (cell2[0],) + dic.wrap(cell2[1], 21)
                else:
                    cell2 = (cell2[0],) + (cell2[1],)
                print(str(cell2))
                #if not cell2 == None:
                #    for cell3 in cell2:
                #        print(cell3+'\n')













