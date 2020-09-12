#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pprint
import sys

import bbcode
import html2text
import pyphen
from hyphen import Hyphenator
from textwrap2 import fill

if "Brython" not in sys.version.split():

    h_de = Hyphenator("de_DE")
    dic = pyphen.Pyphen(lang="de_DE")  # Bibliothek für Worteilumbruch bei Zeilenumbruch

    ColumnsRowsAmount, shellRowsAmountStr = (
        os.popen("stty size", "r").read().split()
    )  # Wie viele Zeilen und Spalten hat die Shell ?
else:
    ColumnsRowsAmount, shellRowsAmountStr = "50", "50"
pp = pprint.PrettyPrinter(indent=4)
shellRowsAmount: int = int(shellRowsAmountStr)
infoLog = False
# originalLinesRange = range(1028)  # Maximale Zeilenanzahl
output = True


def alxp(text):
    global output
    """Für mich, damit ich mal alle prints ausschalten kann zum vorführen,
    wenn ich noch beim Entwicklen war."""
    if infoLog and output:
        if type(text) is str:
            print(text)
        else:
            pp.pprint(text)


def cliout(text):
    if output:
        print(text)
