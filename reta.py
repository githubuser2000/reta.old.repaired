#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv


def wortumbruch(text,maxlen):
    text = text.split()
    wordLens = 0
    wordAmountPerLine = 0
    newtext3 = []
    newtext4 = ''
    for i,word in enumerate(text):
        wordLens += 1 + len(word)
        wordAmountPerLine += 1
        if wordLens > maxlen:
            if wordAmountPerLine == 1:
                newtext3 += [word[:maxlen]]
                newtext3 += ['\n']
                newtext3 += [word[maxlen:]]
            else:
                newtext3 += ['\n']
                newtext3 += [word]
            wordLens = 0
            wordAmountPerLine = 0
        else:
            newtext3 += [word]

        #if i == 0 :
        #    newtext4 += '_'.join(newtext3)
        #elif newtext3[i-1] == '\n':
        #    newtext4 += '_'.join(newtext3)
        #else:
        newtext4 += (' '.join(newtext3))
        newtext3 = []
    return str(newtext4)

if True:
    with open('religion.csv', mode='r') as csv_file:
        relitable = []
        for row in list(csv.reader(csv_file, delimiter=';')):
            relitable += [row]
    for line in relitable:
        for cell in line:
            cell2 = wortumbruch(cell,4)
            print(cell2+'\n')













