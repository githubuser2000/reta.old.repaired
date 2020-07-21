#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import math
import os
import pprint
import re
import sys
from copy import deepcopy
# from collections.abc import Iterable
from typing import Iterable, Union

import bbcode
import html2text
import pyphen

pp = pprint.PrettyPrinter(indent=4)
dic = pyphen.Pyphen(lang="de_DE")  # Bibliothek für Worteilumbruch bei Zeilenumbruch
ColumnsRowsAmount, shellRowsAmount = (
    os.popen("stty size", "r").read().split()
)  # Wie viele Zeilen und Spalten hat die Shell ?
infoLog = False
originalLinesRange = range(120)  # Maximale Zeilenanzahl
output = True

parser = bbcode.Parser()
parser.add_simple_formatter("hr", "<hr />", standalone=True)
parser.add_simple_formatter("sub", "<sub>%(value)s</sub>")
parser.add_simple_formatter("sup", "<sup>%(value)s</sup>")


def render_color(tag_name, value, options, parent, context):
    return '<span style="color:%s;">%s</span>' % (tag_name, value)


# print(os.path.dirname(__file__))
for color in ("red", "blue", "green", "yellow", "black", "white"):
    parser.add_formatter(color, render_color)


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


class Tables:
    def getRowAmountofAnyPart(self):
        return {
            "numerierung": 1 if self.nummeriere else 0,
            #            "irrelevant: gestirn": 1 if self.spalteGestirn else 0,
            #            "alltogether": len(self.puniverseprims)
            #            + len(self.rowsAsNumbers)
            #            + len(self.rowsOfcombi),
            #            "main out": len(self.getOut.rowsAsNumbers),
            "main prepare relitable orignal | combi & concat-prim drin": self.getPrepare.rowsAsNumbers,
            "prim (concat)": self.puniverseprims,
            "combi": (self.getCombis.rowsOfcombi, self.getCombis.ChosenKombiLines),
            "len(AllCombiRows)": self.getCombis.sumOfAllCombiRowsAmount,
            "row of prim multi generated": self.primUniverseRow
            # "concat (prim)": (
            #    self.getConcat.concatRowsAmount,
            #    self.primUniversePrimsSet,
            # ),
        }

    #    @property
    #    def rowsSet(self):
    #        return self.getPrepare.rowsAsNumbers
    #
    #    @rowsSet.setter
    #    def rowsSet(self, value: set):
    #        self.getPrepare.rowsAsNumbers = value

    @property
    def generRows(self):
        return self.__generRows__

    @generRows.setter
    def generRows(self, value: set):
        self.__generRows__ = value

    @property
    def ifPrimMultis(self):
        return self.getPrepare.ifprimmultis

    @ifPrimMultis.setter
    def ifPrimMultis(self, value: bool):
        self.getPrepare.ifprimmultis = value

    @property
    def primUniversePrimsSet(self):
        return self.puniverseprims

    @property
    def breitenn(self):
        return self.getOut.breiten

    @breitenn.setter
    def breitenn(self, value: bool):
        self.getPrepare.breiten = value
        self.getOut.breiten = value

    @property
    def spalteGestirn(self):
        return self.getMainTable.spalteGestirn

    @spalteGestirn.setter
    def spalteGestirn(self, value: bool):
        self.getMainTable.spalteGestirn = value

    @property
    def nummeriere(self):
        """ # Nummerierung der Zeilen, z.B. Religion 1,2,3 """
        return self.getOut.nummerierung

    @nummeriere.setter
    def nummeriere(self, value: bool):
        self.getOut.nummerierung = value
        self.getPrepare.nummerierung = value

    @property
    def textHeight(self):
        return self.getOut.textHeight

    @textHeight.setter
    def textHeight(self, value: int):
        self.getOut.textHeight = value

    @property
    def textWidth(self):
        return self.textwidth

    @textWidth.setter
    def textWidth(self, value: int):
        self.getPrepare.textWidth = value
        self.getOut.textWidth = value
        self.textwidth = value

    def __init__(self):
        self.getPrepare = self.Prepare()
        self.getCombis = self.Combi()
        self.getConcat = self.Concat(self)
        self.getOut = self.Output()
        self.getMainTable = self.Maintable()
        self.textHeight = 0
        self.textWidth = 21
        self.nummeriere = True
        self.spaltegGestirn = False
        self.breitenn: list = []
        self.puniverseprims: set = set()  # welche Spalten von "primenumbers.csv"
        self.getOut.primUniversePrimsSet = self.puniverseprims
        self.getConcat.primUniversePrimsSet = self.puniverseprims
        self.religionNumbers: list = []
        self.getOut.religionNumbers = self.religionNumbers
        self.getPrepare.religionNumbers = self.religionNumbers
        self.getCombis.religionNumbers = self.religionNumbers
        self.getPrepare.ifprimmultis = False
        self.getCombis.rowsOfcombi = set()
        # self.getPrepare.rowsAsNumbers = set()
        self.getConcat.concatRowsAmount = 0
        self.__generRows__: set = set()

    class Output:
        @property
        def primUniversePrimsSet(self):
            return self.puniverseprims

        @primUniversePrimsSet.setter
        def primUniversePrimsSet(self, value: set):
            self.puniverseprims = value

        @property
        def breitenn(self):
            return self.breiten

        @breitenn.setter
        def breitenn(self, value: list):
            self.breiten = value

        @property
        def nummeriere(self):
            """ # Nummerierung der Zeilen, z.B. Religion 1,2,3 """
            return self.nummerierung

        @nummeriere.setter
        def nummeriere(self, value):
            self.nummerierung = value

        @property
        def textHeight(self):
            return self.textheight

        @textHeight.setter
        def textHeight(self, value):
            self.textheight = value

        @property
        def textWidth(self):
            return self.textwidth

        @textWidth.setter
        def textWidth(self, value):
            self.textwidth = value

        def oneTabletoMany(self, table: list, ifmany: bool, rowsRange: range) -> tuple:
            if ifmany:
                lens: int = 0
                tables: list = []
                last_i: int = 0
                lenBefore: int
                rowAmounts: list = []
                # Zelle, Bildschirmzeile, Subzelle - ist die Reihenfolge, auch
                # wenn schwer vorstellbar, dann so: 2. ganze Zeile 3. Subzelle
                # 1. der INDEX der Zelle
                for i, c in enumerate(
                    table[0]
                ):  # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                    lens += len(table[0][i][0])
                    if lens > int(shellRowsAmount) and i != len(table[0]) - 1:
                        # tables += [table[last_i : i - 1]]
                        last_i = i
                        rowAmounts += [i - 1 - last_i]
                    elif i == len(table[0]) - 1:
                        # tables += [table[last_i:i]]
                        rowAmounts += [i - last_i]
                return rowAmounts
            return [len(rowsRange)]

        def cliOut(
            self,
            finallyDisplayLines: set,
            newTable: list,
            numlen: int,
            rowsRange: range,
            rowAmount: int,
        ):
            """gibt eine Tabelle aus

            @type finallyDisplayLines: set
            @param finallyDisplayLines: Zeilen die ausgegeben werden sollen
            @type newRows: list
            @param newRows: Tabelle um die es geht
            @type rowsRange: set
            @param rowsRange: range(spaltenanzahl)
            @rtype:
            @return: nichts
            """
            global output, shellRowsAmount

            def findMaxCellTextLen(
                finallyDisplayLines: set, newTable: list, rowsRange: range
            ) -> dict:
                """Gibt eine Liste zurück mit allen maximalen Zellhoehen pro alle Zellen einer Zeile

                @type finallyDisplayLines: set
                @param finallyDisplayLines: Zeilen die ausgegeben werden sollen
                @type newTable: list
                @param newTable: Tabelle um die es geht
                @type rowsRange: set
                @param rowsRange: range(spaltenanzahl)
                @rtype: dict[int,int]
                @return: Zellhöhen pro Zeile
                """
                maxCellTextLen: dict = {}
                # for k in finallyDisplayLines: # n Linien einer Zelle, d.h. 1 EL = n Zellen
                for k, (f, r) in enumerate(
                    zip(newTable, finallyDisplayLines)
                ):  # n Linien einer Zelle, d.h. 1 EL = n Zellen
                    for iterWholeLine, m in enumerate(
                        rowsRange
                    ):  # eine Bildhschirm-Zeile immer
                        # for i in self.rowsAsNumbers: # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                        for i, c in enumerate(
                            newTable[k]
                        ):  # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                            if not i in maxCellTextLen:
                                try:
                                    maxCellTextLen[i] = len(newTable[k][i][m])
                                except:
                                    pass
                            else:
                                try:
                                    textLen = len(newTable[k][i][m])
                                    if textLen > int(maxCellTextLen[i]):
                                        maxCellTextLen[i] = textLen
                                except:
                                    pass
                return maxCellTextLen

            maxCellTextLen = findMaxCellTextLen(
                finallyDisplayLines, newTable, rowsRange
            )
            finallyDisplayLines = list(finallyDisplayLines)
            finallyDisplayLines.sort()
            for k, (f, r) in enumerate(
                zip(newTable, finallyDisplayLines)
            ):  # n Linien einer Zelle, d.h. 1 EL = n Zellen
                #        actualPartLineLen = 0
                for iterWholeLine, m in enumerate(
                    rowsRange
                ):  # eine Bildhschirm-Zeile immer
                    #            actualPartLineLen += 1
                    line = (
                        ""
                        if not self.nummerierung
                        else (
                            "".rjust(numlen + 1)
                            if iterWholeLine != 0
                            else (str(r) + " ").rjust(numlen + 1)
                        )
                    )
                    rowsEmpty = 0
                    # for i in realLinesRange: # Teil-Linien nebeneinander als Teil-Spalten
                    # maxRowsPossible = math.floor(
                    #    int(shellRowsAmount) / int(self.textwidth + 1)
                    # )
                    # maxCellTextLen = 0
                    # for i in self.rowsAsNumbers: # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                    for i, c in enumerate(
                        newTable[k]
                    ):  # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                        # maxRowsPossible = math.floor( int(shellRowsAmount) / int(self.textwidth+1))
                        # if i < maxRowsPossible and k < 6:
                        # if i < maxRowsPossible:
                        if i < len(self.breiten):
                            # if i + (1 if self.nummerierung else 0) <= len(self.breiten):
                            certaintextwidth = self.breiten[i]
                        else:
                            certaintextwidth = self.textwidth
                        if certaintextwidth > maxCellTextLen[i]:
                            i_textwidth = maxCellTextLen[i]
                        else:
                            i_textwidth = certaintextwidth
                        try:
                            line += (
                                self.colorize(
                                    newTable[k][i][m]
                                    .replace("\n", "")
                                    .ljust(i_textwidth),
                                    r,
                                    i,
                                )
                                + " "
                            )  # neben-Einander
                        except:
                            rowsEmpty += 1
                            line += (
                                self.colorize("".ljust(i_textwidth), r, i, True) + " "
                            )  # neben-Einander
                    if rowsEmpty != len(self.rowsAsNumbers) and (
                        iterWholeLine < self.textheight or self.textheight == 0
                    ):  # and m < actualPartLineLen:
                        cliout(line)

        def colorize(self, text, num: int, row, rest=False) -> str:
            """Die Ausagabe der Tabelle wird coloriert

            @type text: str
            @param text: der zu colorierende Text
            @type num: int
            @param num: die Zeilennummer, die coloriert werden soll
            @type rest: bool
            @param rest: andere Colorierung
            @rtype: str
            @return: der colorierte Text
            """
            # \033[0;34mblaues Huhn\033[0m.
            num = int(num)
            if rest:
                if num == 0:
                    return "\033[41m" + "\033[30m" + "\033[1m" + text + "\033[0m"
                elif num % 2 == 0:
                    return "\033[47m" + "\033[30m" + text + "\033[0m" + "\033[0m"
                else:
                    return "\033[40m" + "\033[37m" + text + "\033[0m" + "\033[0m"
            elif moonNumber(num)[1] != []:
                # 00;33
                return "\033[46m" + "\033[30m" + text + "\033[0m" + "\033[0m"
            elif len(primFak(num)) == 1:
                return "\033[43m" + "\033[30m" + text + "\033[0m" + "\033[0m"
            elif num % 2 == 0:
                if num == 0:
                    return "\033[41m" + "\033[30m" + "\033[1m" + text + "\033[0m"
                else:
                    return "\033[47m" + "\033[30m" + text + "\033[0m" + "\033[0m"
            else:
                return "\033[40m" + "\033[37m" + text + "\033[0m" + "\033[0m"

    class Prepare:
        def __init__(self):
            self.zaehlungen = [
                0,
                {},
                {},
                {},
                {},
            ]  # Strukturangaben zur Zeile wegen Mondzahlen und Sonnenzahlen
            self.religionNumbers = 0

        def setZaehlungen(
            self, num: int
        ):  # mehrere Zählungen finden festlegen zum später auslesen
            """Eine Zahl wird untersucht und die Variable self.zaehlungen wegen dieser Ergänzt
            self.zaehlungen bekommt informationen über mondzahlen und sonnenzahlen
            i ist eine zu Untersuchende Zahl kleinergeich num
            self.zaehlungen[4][i] bekommt die mondtypen, d.h. (Basis, Exponent) immer
            self.zaehlungen[1][zaehlung] welche zählung fängt mit welcher Zahl an
            self.zaehlungen[2][i] ist welcher Zählung es ist für eine beliebige Zahl: 1 ist 1-4, 2 ist 5-9, 3 ist 10-16
            self.zaehlungen[3][i] ist auch welche Zählung es ist für eine beliebige Zahl: 1 ist 1-4, 2 ist 5-9, 3 ist 10-16
            self.zaehlungen[0] ist bis zu welcher Zahl diese Untersuchung beim letzten Mal durchgeführt wurde
            self.zaehlungen  # [bis zu welcher zahl, {zaehlung:zahl},{zahl:zaehlung},{jede zahl,zugehoerigeZaehlung}]

            @type num: int
            @param num: zu untersuchende Zahl
            @rtype: kein Typ
            @return: nichts
            """
            wasMoon: bool = True
            if self.zaehlungen[0] == 0:
                isMoon = True
            else:
                isMoon = moonNumber(self.zaehlungen[0])[0] != []

            for i in range(int(self.zaehlungen[0]) + 1, num + 1):
                wasMoon = isMoon
                moonType = moonNumber(i)
                isMoon = moonType[0] != []
                if wasMoon and not isMoon:
                    isMoon = False
                    self.zaehlungen[1][len(self.zaehlungen[1]) + 1] = i
                    self.zaehlungen[2][i] = len(self.zaehlungen[2]) + 1
                self.zaehlungen[3][i] = len(self.zaehlungen[2])
                self.zaehlungen[4][i] = moonType

        @property
        def breitenn(self):
            return self.breiten

        @breitenn.setter
        def breitenn(self, value: bool):
            self.breiten = value

        @property
        def nummeriere(self):
            """ # Nummerierung der Zeilen, z.B. Religion 1,2,3 """
            return self.nummerierung

        @nummeriere.setter
        def nummeriere(self, value):
            self.nummerierung = value

        @property
        def textWidth(self):
            return self.textwidth

        @textWidth.setter
        def textWidth(self, value):
            self.textwidth = value

        def createRowPrimeMultiples(
            self, relitable: list, rowsAsNumbers: set, certaintextwidth: int
        ):
            self.relitable = relitable
            if self.ifprimmultis:
                if len(self.relitable) > 0:
                    rowsAsNumbers.add(len(self.relitable[0]))
                # moonNumber
                for i, line in enumerate(self.relitable):
                    if i == 0:
                        line += self.wrapping2("Primzahlenvielfache", certaintextwidth)
                    else:
                        line += self.wrapping2("", certaintextwidth)
                    pass

        def wrapping2(self, text: str, length: int) -> list:
            """Hier wird der Zeilenumbruch umgesetzt

            @type text: str
            @param text: Der Text dessen Zeilen umbgebrochen werden sollen
            @type lenght: int
            @param lenght: ab welcher Zeilenlänge umgebrochen werden soll
            @rtype: list[str]
            @return: Liste aus umgebrochenen Teilstrings
            """
            if len(text) > length - 1:
                isItNone = dic.wrap(text, length - 1)
            else:
                isItNone = text
            return isItNone

        def wrapping(self, text: str, length: int) -> list:
            """Hier wird der Zeilenumbruch umgesetzt

            @type text: str
            @param text: Der Text dessen Zeilen umbgebrochen werden sollen
            @type lenght: int
            @param lenght: ab welcher Zeilenlänge umgebrochen werden soll
            @rtype: list[str]
            @return: Liste aus umgebrochenen Teilstrings
            """
            if len(text) > length - 1:
                isItNone = dic.wrap(text, length - 1)
            else:
                isItNone = None
            return isItNone

        def setWidth(self, rowToDisplay: int, combiRows1: int = 0) -> int:
            combiRows = combiRows1 if combiRows1 != 0 else len(self.rowsAsNumbers)
            if len(self.rowsAsNumbers) - combiRows < len(self.breiten):
                breiten: list = self.breiten[len(self.rowsAsNumbers) - combiRows :]
            else:
                breiten: list = []
            # delta = -1 if not self.nummerierung and combiRows1 != 0 else -1
            delta = -1
            if rowToDisplay + delta < len(breiten) and rowToDisplay + delta >= 0:
                certaintextwidth = breiten[rowToDisplay + delta]
            else:
                certaintextwidth = self.textwidth
            return certaintextwidth

        def parametersCmdWithSomeBereich(
            self, MehrereBereiche: str, symbol: str, neg: str
        ) -> set:
            """Erstellen des Befehls: Bereich

            @type MehrereBereiche: str
            @param MehrereBereiche: der Bereich von bis
            @type symbol: str
            @param symbol: welche Art Bereich soll es werden, symbol typisiert den Bereich
            @type neg: string
            @param neg: Vorzeichen, wenn es darum geht dass diese Zeilen nicht angezeigt werden sollen
            @rtype: set
            @return: Alle Zeilen die dann ausgegeben werden sollen
            """
            results = set()
            for EinBereich in MehrereBereiche.split(","):
                if (
                    (neg == "" and len(EinBereich) > 0 and EinBereich[0].isdecimal())
                    or (neg == EinBereich[: len(neg)] and len(neg) > 0)
                ) and len(EinBereich) > 0:
                    EinBereich = (
                        EinBereich[len(neg) :]
                        if neg == EinBereich[: len(neg)]
                        else EinBereich
                    )
                    if EinBereich.isdecimal():
                        EinBereich = EinBereich + "-" + EinBereich
                    BereichCouple = EinBereich.split("-")
                    if (
                        len(BereichCouple) == 2
                        and BereichCouple[0].isdecimal()
                        and BereichCouple[0] != "0"
                        and BereichCouple[1].isdecimal()
                        and BereichCouple[1] != "0"
                    ):
                        results.add(
                            BereichCouple[0] + "-" + symbol + "-" + BereichCouple[1]
                        )

            return results

        def deleteDoublesInSets(
            self, set1: set, set2: set
        ) -> Iterable[Union[set, set]]:
            """Wenn etwas in 2 Mengen doppelt vorkommt wird es gelöscht
            @rtype: tuple[set,set]
            @return: Beide Mengen werden ausgegeben
            """
            intersection = set1 & set2
            return set1 - intersection, set2 - intersection

        def fromUntil(self, a) -> tuple:
            """2 Zahlen sollen ein ordentlicher Zahlenbereich sein, sonst werden sie es^

            @rtype: tuple[int,int]
            @return: Eine Bereichsangabe
            """
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
                    return (1, 1)
                return tuple(a)
            else:
                return (1, 1)

        # ich wollte je pro extra num, nun nicht mehr nur sondern modular ein mal alles und dann pro nummer in 2 funktionen geteilt
        def FilterOriginalLines(self, numRange: set, paramLines: set) -> set:
            """Hier werden die Befehle der Angabe welche Zeilen angezeigt werden in konkrete Zeilen umgewandelt.

            @type results: Menge
            @param set: Bereiche von Zeilen einer Art: Anzeigen, ja, nein, von woanders, etc.
            @rtype: set
            @return: Mehrere Bereichsbezeichnugen
            """

            def diffset(wether, a: set, b: set) -> set:
                if wether:
                    # result = a.difference(b)
                    result = a - b
                    if result is None:
                        return set()
                    else:
                        return result
                return a

            numRange -= {0}

            def cutset(wether, a: set, b: set) -> set:
                if wether:
                    # result = a.intersection(b)
                    result = a & b
                    if result is None:
                        return set()
                    else:
                        return result
                return a

            numRangeYesZ = set()
            if_a_AtAll = False
            for condition in paramLines:
                if "-a-" in condition:
                    if_a_AtAll = True
                    a = self.fromUntil(condition.split("-a-"))
                    for n in numRange.copy():
                        if a[0] <= n and a[1] >= n:
                            # numRange.remove(n)
                            numRangeYesZ.add(n)

            numRange = cutset(if_a_AtAll, numRange, numRangeYesZ)
            numRangeYesZ = set()
            ifZeitAtAll = False

            for condition in paramLines:
                if "=" == condition:
                    ifZeitAtAll = True
                    numRangeYesZ.add(10)
                elif "<" == condition:
                    ifZeitAtAll = True
                    for n in numRange:
                        if n < 10:
                            numRangeYesZ.add(n)
                elif ">" == condition:
                    ifZeitAtAll = True
                    for n in numRange:
                        if n > 10:
                            numRangeYesZ.add(n)

            numRange = cutset(ifZeitAtAll, numRange, numRangeYesZ)

            numRangeYesZ = set()
            ifZaehlungenAtAll = False
            for condition in paramLines:
                if (
                    len(condition) > 1
                    and condition[-1] == "z"
                    and condition[0:-1].isdecimal()
                ):  # ist eine von mehreren Zählungen
                    if not ifZaehlungenAtAll:
                        self.setZaehlungen(originalLinesRange[-1])
                        ifZaehlungenAtAll = True
                    zaehlungGesucht = int(
                        condition[0:-1]
                    )  # eine zählung = eine zahl, beginnend minimal ab 1
                    for n in numRange:  # nur die nummern, die noch infrage kommen
                        # self.zaehlungen = [0,{},{},{}]
                        if self.zaehlungen[3][n] == int(
                            zaehlungGesucht
                        ):  # 1-4:1,5-9:2 == jetzt ?
                            numRangeYesZ.add(n)
                            # numRange.remove(n)
            numRange = cutset(ifZaehlungenAtAll, numRange, numRangeYesZ)
            # set().add
            # exit()
            ifTypAtAll = False
            numRangeYesZ = set()

            def moonsun(MoonNotSun: bool, numRangeYesZ: set):
                if not ifZaehlungenAtAll:
                    self.setZaehlungen(originalLinesRange[-1])
                for n in numRange:
                    if (self.zaehlungen[4][n][0] != []) == MoonNotSun:
                        numRangeYesZ.add(n)
                return numRangeYesZ

            for condition in paramLines:
                if "mond" in condition:
                    numRangeYesZ, ifTypAtAll = moonsun(True, numRangeYesZ), True
                elif "schwarzesonne" in condition:
                    ifTypAtAll = True
                    for n in numRange:
                        if n % 3 == 0:
                            numRangeYesZ.add(n)
                elif "sonne" in condition:
                    numRangeYesZ, ifTypAtAll = moonsun(False, numRangeYesZ), True
                elif "planet" in condition:
                    ifTypAtAll = True
                    for n in numRange:
                        if n % 2 == 0:
                            numRangeYesZ.add(n)

            numRange = cutset(ifTypAtAll, numRange, numRangeYesZ)

            primMultiples: list = []
            ifPrimAtAll = False
            for condition in paramLines:
                if (
                    len(condition) > 1
                    and condition[-1] == "p"
                    and condition[:-1].isdecimal()
                ):
                    ifPrimAtAll = True
                    primMultiples += [int(condition[:-1])]

            numRangeYesZ = set()
            for n in numRange:
                if isPrimMultiple(n, primMultiples):
                    numRangeYesZ.add(n)
            numRange = cutset(ifPrimAtAll, numRange, numRangeYesZ)

            ifMultiplesFromAnyAtAll = False
            anyMultiples = []
            for condition in paramLines:
                if (
                    len(condition) > 1
                    and condition[-1] == "v"
                    and condition[:-1].isdecimal()
                ):
                    ifMultiplesFromAnyAtAll = True
                    anyMultiples += [int(condition[:-1])]

            if ifMultiplesFromAnyAtAll:
                numRangeYesZ = set()
                for n in numRange:
                    for divisor in anyMultiples:
                        if n % divisor == 0:
                            numRangeYesZ.add(n)
                numRange = cutset(ifMultiplesFromAnyAtAll, numRange, numRangeYesZ)

            ifNachtraeglichAtAll = False
            for condition in paramLines:
                if "-z-" in condition:
                    if not ifNachtraeglichAtAll:
                        numRange2: list = list(numRange)
                        numRange2.sort()
                        ifNachtraeglichAtAll = True
                    a = self.fromUntil(condition.split("-z-"))
                    for i, n in enumerate(numRange2.copy()):
                        if a[0] - 1 > i or a[1] - 1 < i:
                            numRange2.remove(n)
            if ifNachtraeglichAtAll:
                numRange = set(numRange2)
            return numRange

        def prepare4out(
            self,
            paramLines: set,
            paramLinesNot: set,
            contentTable: list,
            rowsAsNumbers: set,
            combiRows: int = 0,
        ) -> tuple:
            """Aus einer Tabelle wird eine gemacht, bei der der Zeilenumbruch durchgeführt wird.
            Dabei werden alle Spalten und Zeilen entfernt die nicht ausgegeben werden sollen.

            @type paramLines: set
            @param paramLines: welche Linien ja, andere fallen weg
            @type paramLinesNot: set
            @param paramLinesNot: welche Linien nein, werden abgezogen von ja
            @type contentTable: list
            @param contentTable: die Tabelle die verändert werden soll
            @type rowsAsNumberss: set
            @param rowsAsNumberss: anzuzeigende Spalten
            @rtype: tuple[set,set,int,range,list]
            @return: Zeilen die ausgegeben werden sollen, neue Tabelle, Nummer der letzten Zeile , \
                range aus zu zeigenden Spalten 1-n nicht alle , welche neuen Spalten welche alten waren und umgekehrt
            return finallyDisplayLines, newRows, numlen, rowsRange, old2newRows
            """
            newRows: list = []
            if len(contentTable) > 0:
                headingsAmount = len(contentTable[0])
                rowsRange = range(headingsAmount)
            else:
                headingsAmount = 0
                rowsRange = range(0)
            finallyDisplayLines: set = self.FilterOriginalLines(
                set(originalLinesRange), paramLines
            )
            if not len(paramLinesNot) == 0:
                finallyDisplayLines2 = self.FilterOriginalLines(
                    deepcopy(finallyDisplayLines), paramLinesNot
                )
                hasAnythingCanged = set(originalLinesRange) - finallyDisplayLines2 - {0}
                if len(hasAnythingCanged) > 0:
                    finallyDisplayLines -= finallyDisplayLines2
            finallyDisplayLines.add(0)
            finallyDisplayLines3: list = list(finallyDisplayLines)
            finallyDisplayLines3.sort()
            finallyDisplayLines = set(finallyDisplayLines3)
            #    maxPartLineLen = 0
            numlen = len(str(finallyDisplayLines3[-1]))
            old2newRows: tuple = ({}, {})
            reliNumbersBool = False if self.religionNumbers != [] else True
            for u, line in enumerate(contentTable):
                if u in finallyDisplayLines:
                    if reliNumbersBool:
                        self.religionNumbers += [int(u)]
                    new2Lines: list = []
                    rowToDisplay = 0
                    h = 0
                    for t, cell in enumerate(line):
                        if t in rowsAsNumbers:
                            rowToDisplay += 1
                            newLines = [[]] * headingsAmount
                            certaintextwidth = self.setWidth(rowToDisplay, combiRows)
                            into = self.cellWork(cell, newLines, certaintextwidth, t)
                            if into != [""] or True:
                                new2Lines += [into]
                            if u == 0:
                                old2newRows[0][t] = h
                                old2newRows[1][h] = t
                            h += 1
                    if new2Lines != []:
                        newRows += [new2Lines]

            return finallyDisplayLines, newRows, numlen, rowsRange, old2newRows

        def cellWork(self, cell: str, newLines, certaintextwidth: int, t: int) -> list:
            """aus String mach Liste aus Strings mit korrektem Zeilenumbruch

            @type cell: str
            @param cell: Text, für in Teilstrings, korrekter Zeilenumbruch!
            @type newLines: list[str]
            @param newLines: voran gegangene Versuche dieser Liste aus Strings
            @type certaintextwidth: int
            @param certaintextwidth: an dieser Stelle Zeilenumbruch
            @type t: int
            @param t: welcher Versuch einer Liste aus strings soll von dieser Funktion zurück gegeben werden
            @rtype: list[str]
            @return: Liste aus Strings mit korrektem Zeilenumbruch
            """

            cell = cell.strip()
            isItNone = self.wrapping(cell, certaintextwidth)
            cell2: tuple = tuple()
            rest: str = cell
            while not isItNone is None:
                cell2 += isItNone
                isItNone = self.wrapping(cell2[-1], certaintextwidth)
                rest = cell2[-1]
                cell2 = cell2[:-1]
                if len(rest) > certaintextwidth and isItNone is None:
                    cell2 += (rest[0 : certaintextwidth - 1],)
                    isItNone = (rest[certaintextwidth:],)
            else:
                cell2 += (rest[0 : certaintextwidth - 1],)
                for k, cellInCells in enumerate(cell2):
                    if k < len(newLines):
                        newLines[k] += [cellInCells]
                    else:
                        pass
            return newLines[t]

    @staticmethod
    def fillBoth(liste1, liste2) -> Iterable[Union[list, list]]:
        """eine der beiden Listen erhält so viele Listenelemente
        aus Strings dazu wie die andere hat, bis beide gleich viel haben

        @type liste1: list[str]
        @param liste1: die erste Liste
        @type liste2: list[str]
        @param liste2: die zweite Liste
        @rtype: tuple(list[str],list[str])
        @return: 2 Listen mit gleicher Länger, maximiert statt minimiert
        """
        while len(liste1) < len(liste2):
            liste1 += [""]
        while len(liste2) < len(liste1):
            liste2 += [""]
        return liste1, liste2

    class Combi:
        def __init__(self):
            self.ChosenKombiLines: dict = {}
            self.sumOfAllCombiRowsAmount = 0

        def tableJoin(
            self,
            mainTable,
            manySubTables,
            maintable2subtable_Relation,
            old2newRows,
            rowsOfcombi,
        ):
            rowsOfcombi = list(rowsOfcombi)
            rowsOfcombi.sort()
            table2 = mainTable
            for colNum, (reliNum, col) in enumerate(
                zip(self.religionNumbers, mainTable)
            ):
                for subTable in manySubTables:
                    if reliNum in subTable:
                        for row, bigCell in enumerate(mainTable[colNum]):
                            if old2newRows[1][row] in maintable2subtable_Relation[0]:
                                subRowNum = maintable2subtable_Relation[0][
                                    old2newRows[1][row]
                                ]
                                for subTableCell in subTable[reliNum]:
                                    if rowsOfcombi.index(subRowNum + 1) < len(
                                        subTableCell
                                    ) and subTableCell != [[""]]:
                                        if (
                                            len(table2[colNum][row]) == 1
                                            and table2[colNum][row][0] == ""
                                        ):
                                            table2[colNum][row] = deepcopy(
                                                subTableCell[
                                                    rowsOfcombi.index(subRowNum + 1)
                                                ]
                                            )
                                        else:
                                            table2[colNum][row] += deepcopy(
                                                subTableCell[
                                                    rowsOfcombi.index(subRowNum + 1)
                                                ]
                                            )
            return table2

        def prepare_kombi(
            self,
            finallyDisplayLines_kombi_1: set,
            kombiTable: list,
            paramLines: set,
            displayingMainLines: set,
            kombiTable_Kombis: list,
        ):
            """Vorbereiten zum Kombinieren von Tabellen, wie bei einem SQL-Join

            @type finallyDisplayLines: set
            @param finallyDisplayLines: set
            @type kombiTable: list
            @param kombiTable: Tabelle um die es geht, die zur Haupttabelle dazu kommt
            @type paramLines: set
            @param paramLines: Befehle die aus den Shell Paramentern konstruiert wurden
            @type displayingMainLines: set
            @param displayingMainLines: Zeilen die angezeigt werden sollen
            @type kombiTable_Kombis: list
            @param kombiTable_Kombis: wird anscheinend hier gar nicht gebraucht
            @rtype: dict[set[int]]
            @return: Zeilen die miteinander als Join kombiniert werden sollen zwischen Haupttabelle und weiterer
            """

            kombitypes = {"displaying": False, "or": False, "and": False}
            self.ChosenKombiLines: dict = {}
            for condition in paramLines:
                if "ka" == condition:
                    kombitypes["displaying"] = True
                    for MainLineNum in displayingMainLines:
                        for kombiLineNumber, kombiLine in enumerate(kombiTable_Kombis):
                            for kombiNumber in kombiLine:
                                if (
                                    kombiNumber in displayingMainLines
                                    and kombiNumber == MainLineNum
                                ):
                                    if MainLineNum in self.ChosenKombiLines:
                                        self.ChosenKombiLines[MainLineNum] |= {
                                            kombiLineNumber + 1
                                        }
                                    else:
                                        self.ChosenKombiLines[MainLineNum] = {
                                            kombiLineNumber + 1
                                        }
            return self.ChosenKombiLines

        def readKombiCsv(
            self, relitable: list, rowsAsNumbers: set, rowsOfcombi: set
        ) -> tuple:
            """Fügt eine Tabelle neben der self.relitable nicht daneben sondern als join an, wie ein sql-join
            Hier wird aber noch nicht die join Operation durchgeführt
            momentan ist es noch fix auf animalsProfessions.csv

            @type relitable: list
            @param relitable: Haupttabelle self.relitable
            @type rowsAsNumbers: set
            @param rowsAsNumbers: welche Spalten der neuen Tabelle dazu kommen sollen
            @type rowsOfcombi: set
            @param rowsOfcombi: welche Spalten der neuen Tabelle dazu kommen sollen
            @rtype: tuple[list,list,list,list]
            @return: neue Tabelle, haupttabelle self.relitable, \
                Liste mit allen Zeilen der neuen Tabelle aus der ersten Spalte je Liste aus allem darin \
                das mit Komma getrennt wurde , was zu was gehört als Info für den join später
            return kombiTable, self.relitable, kombiTable_Kombis, maintable2subtable_Relation
            """
            global folder
            place = os.path.join(
                os.getcwd(), os.path.dirname(__file__), os.path.basename("./kombi.csv")
            )
            self.sumOfAllCombiRowsAmount += len(rowsOfcombi)
            self.relitable = relitable
            headingsAmount = len(self.relitable[0])
            maintable2subtable_Relation: tuple = ({}, {})
            if len(rowsOfcombi) > 0:
                with open(place, mode="r") as csv_file:
                    kombiTable: list = []
                    kombiTable_Kombis: list = []
                    for z, col in enumerate(csv.reader(csv_file, delimiter=";")):
                        """for i, c in enumerate(col):
                            if i not in rowsOfcombi and i != 0:
                                col[i] = ""
                        """
                        for i, row in enumerate(col):
                            if i > 0 and col[i].strip() != "":
                                col[i] += " (" + col[0] + ")"
                        kombiTable += [col]
                        kombiTable_Kombis_Col: list = []
                        if len(col) > 0 and z > 0:
                            for num in col[0].split(","):
                                if num.isdecimal():
                                    kombiTable_Kombis_Col += [int(num)]
                                else:
                                    raise BaseException("not NUM !!!!! ")
                            kombiTable_Kombis += [kombiTable_Kombis_Col]
                    self.relitable, animalsProfessionsCol = Tables.fillBoth(
                        self.relitable, list(kombiTable)
                    )
                    lastlen = 0
                    maxlen = 0
                    for i, (animcol, relicol) in enumerate(
                        zip(animalsProfessionsCol, self.relitable)
                    ):
                        if i == 0:
                            lastlen = len(animcol)
                            if lastlen > maxlen:
                                maxlen = lastlen
                            for t, ac in enumerate(animcol[1:]):
                                maintable2subtable_Relation[0][
                                    len(self.relitable[0]) + t
                                ] = t
                                maintable2subtable_Relation[1][t] = (
                                    len(self.relitable[0]) + t
                                )
                            self.relitable[0] += list(animcol[1:]) + [""] * (
                                maxlen - len(animcol)
                            )
                        else:
                            self.relitable[i] += len(animcol[1:]) * [""] + [""] * (
                                maxlen - len(animcol)
                            )
                        if i == 0:
                            for u, heading in enumerate(self.relitable[0]):
                                for a in rowsOfcombi:
                                    if (
                                        u >= headingsAmount
                                        and u == headingsAmount + a - 1
                                    ):
                                        rowsAsNumbers.add(int(u))
            else:
                kombiTable = [[]]
                kombiTable_Kombis = [[]]
            if len(kombiTable) > 0:
                self.rowsOfcombi = len(rowsAsNumbers) - 1
            else:
                self.rowsOfcombi = 0
            return (
                kombiTable,
                self.relitable,
                kombiTable_Kombis,
                maintable2subtable_Relation,
            )

    class Concat:
        def __init__(self, tables):
            self.tables = tables

        @property
        def primUniversePrimsSet(self):
            return self.puniverseprims

        @primUniversePrimsSet.setter
        def primUniversePrimsSet(self, value: set):
            self.puniverseprims = value

        def concatLovePolygon(self, relitable: list, rowsAsNumbers: set) -> tuple:
            self.relitable = relitable
            if rowsAsNumbers >= {8}:
                rowsAsNumbers |= {len(self.relitable[0])}
                for i, cols in enumerate(deepcopy(self.relitable)):
                    if self.relitable[i][8].strip() != "":
                        self.relitable[i] += [
                            self.relitable[i][8]
                            + " der eigenen Strukturgröße ("
                            + self.relitable[i][4]
                            + ") auf dich"
                        ]
                    else:
                        self.relitable[i] += [""]
            return self.relitable, rowsAsNumbers

        def concatPrimCreativityType(
            self, relitable: list, rowsAsNumbers: set
        ) -> tuple:
            self.relitable = relitable
            if self.tables.spalteGestirn:
                rowsAsNumbers |= {len(self.relitable[0])}
                for i, cols in enumerate(deepcopy(self.relitable)):
                    primCreativityType = primCreativity(i)
                    self.relitable[i] += [
                        "Evolutions-Züchtungs-Kreativität"
                        if i == 0
                        else (
                            "0. Primzahl 1"
                            if primCreativityType == 0
                            else (
                                "1. Primzahl und Sonnenzahl"
                                if primCreativityType == 1
                                else (
                                    "2. Sonnenzahl, aber keine Primzahl"
                                    if primCreativityType == 2
                                    else "3. Mondzahl"
                                )
                            )
                        )
                    ]
            return self.relitable, rowsAsNumbers

        def concatMondExponzierenLogarithmusTyp(
            self, relitable: list, rowsAsNumbers: set
        ) -> tuple:
            self.relitable = relitable
            if self.tables.spalteGestirn:
                for rownum, rowheading in zip(
                    [44, 56],
                    [
                        "Mond-Typ eines Sternpolygons",
                        "Mond-Typ eines gleichförmigen Polygons",
                    ],
                ):
                    rowsAsNumbers |= {len(self.relitable[0])}
                    for i, cols in enumerate(deepcopy(self.relitable)):
                        moonTypesOf1Num = moonNumber(i)
                        if i == 0:
                            into = rowheading
                        else:
                            into = ""
                            for k, (basis, exponentMinus2) in enumerate(
                                zip(*moonTypesOf1Num)
                            ):
                                if k > 0:
                                    into += " | "
                                insert = re.sub(
                                    r"<SG>",
                                    self.relitable[i][4].strip(),
                                    self.relitable[basis][rownum].rstrip(),
                                )
                                into += (
                                    insert
                                    + " - "
                                    + self.relitable[exponentMinus2 + 2][10]
                                )
                                into += " | "
                                into += (
                                    self.relitable[i][10]
                                    + " + "
                                    + self.relitable[i][11]
                                    + ", obwohl man nicht kann"
                                )
                        self.relitable[i] += [into]
            return self.relitable, rowsAsNumbers

        def concatRowsOfConcepts(
            self, relitable: list, conceptsRowsSetOfTuple: set, rowsAsNumbers: set
        ) -> tuple:
            self.relitable: list = relitable
            self.concepts: list = []
            for i, paar in enumerate(conceptsRowsSetOfTuple):
                first = []
                second = []
                self.concepts += [(first, second)]
                for cols in self.relitable:
                    first += [cols[paar[0]]]
                    second += [cols[paar[1]]]
                rowsAsNumbers |= {len(self.relitable[0]) + i}
            for concept in self.concepts:
                for i, (cols, row1, row2) in enumerate(
                    zip(deepcopy(self.relitable), concept[0], concept[1])
                ):
                    if i == 0:
                        into = "Generiert: " + row1
                    else:
                        into = ""
                        if row1.strip() != "":
                            into += "sehr: " + row1 + "| "
                        if i > 2 and concept[0][i - 2].strip() != "":
                            into += "ganz gut: " + concept[0][i - 2] + "| "
                        if len(concept[0]) > i + 2 and concept[0][i + 2].strip() != "":
                            into += "ganz gut: " + concept[0][i + 2] + "| "
                        if i > 4 and concept[0][i - 4].strip() != "":
                            into += "noch etwas: " + concept[0][i - 4] + "| "
                        if len(concept[0]) > i + 4 and concept[0][i + 4].strip() != "":
                            into += "noch etwas: " + concept[0][i + 4] + "| "
                        if i > 1 and concept[1][i - 1].strip() != "":
                            into += concept[1][i - 1] + "| "
                        if i > 3 and concept[1][i - 3].strip() != "":
                            into += "ein wenig: " + concept[1][i - 3] + "| "
                        if len(concept[1]) > i + 3 and concept[1][i + 3].strip() != "":
                            into += "ein wenig: " + concept[1][i + 3] + "| "
                        if len(concept[1]) > i + 1 and concept[1][i + 1].strip() != "":
                            into += concept[1][i + 1] + "| "
                        if into != "":
                            into += "alles zur selben Strukturgröße einer " + cols[4]
                    self.relitable[i] += [into]
            return self.relitable, rowsAsNumbers

        def concat1RowPrimUniverse2(self, relitable: list, rowsAsNumbers: set) -> tuple:
            """Fügt eine Spalte ein, in der Primzahlen mit Vielfachern
            auf dem Niveau des Universums nicht einfach nur aus einer
            CSV Tabelle geladen werden, sondern durch Primzahlen und
            deren Vielfachern generiert werden.

            @type relitable: list
            @param relitable: Haupttabelle self.relitable
            @return: relitable + weitere Tabelle daneben
            """
            global originalLinesRange
            self.relitable = relitable
            if len(self.tables.primUniversePrimsSet) > 0:
                self.tables.primUniverseRowNum = len(self.relitable[0])
                rowsAsNumbers |= {len(self.relitable[0]), len(self.relitable[0]) + 1}
                for polytype, polytypename in zip(
                    [10, 42], ["Sternpolygone", "gleichförmiges Polygone"]
                ):
                    self.transzendentalien = []
                    self.rolle = []
                    self.motivation = []
                    self.ziel = []
                    for cols in self.relitable:
                        self.motivation += [cols[polytype]]
                        self.rolle += [cols[19]]
                        self.transzendentalien += [cols[5]]
                        self.ziel += [cols[11]]
                    for i, cols in enumerate(deepcopy(self.relitable)):
                        primMultiples = primMultiple(i)
                        into = (
                            ""
                            if i != 0
                            else "generierte Multiplikationen " + polytypename
                        )
                        for k, multi in enumerate(primMultiples[1:]):
                            if k > 0:
                                into += ", außerdem: "
                            into += (
                                "("
                                + (
                                    self.transzendentalien[multi[0]]
                                    if self.transzendentalien[multi[0]].strip() != ""
                                    else "..."
                                )
                                + " UND "
                                + (
                                    self.rolle[multi[0]]
                                    if self.rolle[multi[0]].strip() != ""
                                    else "..."
                                )
                                + ") * ("
                                + (
                                    self.motivation[multi[1]]
                                    if self.motivation[multi[1]].strip() != ""
                                    else "..."
                                )
                                + (
                                    " UND "
                                    + (
                                        self.ziel[multi[1]]
                                        if self.ziel[multi[1]].strip() != ""
                                        else "..."
                                    )
                                    if polytype == 10
                                    else ""
                                )
                                + ")"
                            )
                        self.relitable[i] += [into]
            return self.relitable, rowsAsNumbers

        def readConcatCsv(self, relitable: list, rowsAsNumbers: set) -> list:
            """Fügt eine Tabelle neben der self.relitable an
            momentan ist es noch fix auf primnumbers.csv

            @type relitable: list
            @param relitable: Haupttabelle self.relitable
            @type rowsAsNumbers: set
            @param rowsAsNumbers: welche Spalten der neuen Tabelle dazu kommen sollen
            @rtype: list[list]
            @return: relitable + weitere Tabelle daneben
            """
            global folder
            place = os.path.join(
                os.getcwd(),
                os.path.dirname(__file__),
                os.path.basename("./primenumbers.csv"),
            )
            self.relitable = relitable
            headingsAmount = len(self.relitable[0])
            if len(self.puniverseprims) > 0:
                with open(place, mode="r") as csv_file:
                    self.relitable, primUniverseLine = Tables.fillBoth(
                        self.relitable, list(csv.reader(csv_file, delimiter=";"))
                    )
                    lastlen = 0
                    maxlen = 0
                    for i, (primcol, relicol) in enumerate(
                        zip(primUniverseLine, self.relitable)
                    ):
                        lastlen = len(primcol)
                        if lastlen > maxlen:
                            maxlen = lastlen
                        self.relitable[i] += list(primcol) + [""] * (
                            maxlen - len(primcol)
                        )
                        if i == 0:
                            for u, heading in enumerate(self.relitable[0]):
                                if (
                                    heading.isdecimal()
                                    and int(heading) in self.puniverseprims
                                    and u >= headingsAmount
                                ):
                                    rowsAsNumbers.add(int(u))

                self.concatRowsAmount = len(primcol)
            return self.relitable, rowsAsNumbers

    class Maintable:
        @property
        def spalteGestirn(self):
            return self.spaltegestirn

        @spalteGestirn.setter
        def spalteGestirn(self, value: bool):
            self.spaltegestirn = value

        def __init__(self):
            self.spaltegestirn = False

        def createSpalteGestirn(self, relitable: list, rowsAsNumbers: set):
            """Fügt self.relitable eine Spalte hinzu, ob eine Zahl ein Mond oder eine Sonne ist
            Die Information muss dazu kommt aus moonNumber(i)[1]

            @type relitable: list
            @param relitable: Haupttabelle self.relitable
            @type rowsAsNumbers: set
            @param rowsAsNumbers: welche Spalten der neuen Tabelle nur betroffen sind
            @rtype:
            @return: nichts
            """
            self.relitable = relitable
            if self.spaltegestirn:
                if len(self.relitable) > 0:
                    rowsAsNumbers.add(len(self.relitable[0]))
                # moonNumber
                for i, line in enumerate(self.relitable):
                    if i == 0:
                        line += ["Gestirn"]
                    else:
                        if moonNumber(i)[1] != []:
                            text = "Mond"
                        else:
                            text = "Sonne"
                        if i % 2 == 0:
                            line += [text + ", Planet"]
                        else:
                            line += [text]

    def tableReducedInLinesByTypeSet(self, table: list, linesAllowed: set):
        """nur Zeilen aus dem set aus der Tabelle verwenden als Ausgabe der Tabelle

        @type table: list[list]
        @param table: Tabelle
        @type table: set[int]
        @param table: erlaubte Zeilen
        @rtype: list[list]
        @return: neue Tabelle mit nur den Zeilen aus linesAllowed
        """
        newTable: list = []
        for i, line in enumerate(table):
            if i in linesAllowed:
                newTable += [line]
        return newTable


def moonNumber(num: int):
    """Hier wird der Zeilenumbruch umgesetzt

    @type num: int
    @param num: zu untersuchende Zahl
    @rtype: tuple(list[int],list[int])
    @return: () wenn keine Mondzahl, sonst 2 Listen mit gleicher Länge aus Elementen: Liste1: Basis der Mondzahl, Liste2: Exponent der Mondzahl
    """
    results: list = []
    exponent: list = []
    for i in range(2, num):
        oneResult = math.pow(num, 1 / i)
        if math.floor(oneResult) == oneResult:
            results += [int(oneResult)]
            exponent += [i - 2]
    return results, exponent


def primFak(n: int) -> list:
    """Alle Primfaktoren einer Zahl als Liste mit mehrfachvorkommen, sofern ja

    @type n: int
    @param n: ein natürliche Zahl
    @rtype: list
    @return: alle Primfaktoren, ggf. mit Mehrfachvorkommen
    """
    faktoren: list = []
    z = n
    while z > 1:
        i = 2
        gefunden = False
        while i * i <= n and not gefunden:
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


def primCreativity(num: int):
    fak = primFak(num)
    moon = True
    if len(fak) == 0:
        return 0
    for f in fak[1:]:
        if f != fak[0]:
            moon = False
    if len(fak) == 1:
        return 1
    if moon:
        return 3
    else:
        return 2


def getLogarithmOnlyAsPureInt(potenz: int, basis: int) -> int:
    exponent = math.log(potenz) / math.log(basis)
    if exponent == round(exponent):
        return exponent
    else:
        return None


def primRepeat(n: list) -> list:
    """Primfaktoren werden zusammengefasst in Liste aus Primfaktor hoch n

    @type n:  list
    @param n: Primfaktoren
    @rtype: list[tuple(n1,n2)]
    @return: Liste aus geordneten Paaren mit Primfaktor hoch n
    """
    n.reverse()
    c = 1
    b = None
    d: list = []
    for a in n:
        if b == a:
            c += 1
        else:
            c = 1
        d += [[a, c]]
        b = a
    d.reverse()
    b = None
    f: list = []
    for e, g in d:
        if b != e:
            if g == 1:
                f += [(e, 1)]
            else:
                f += [(e, g)]
        b = e
    return f


def primMultiple(n: int) -> list:
    """Gibt Liste aus geordneten Paaren aus mit Primzahl und Vielfacher der Primzahl aus denen die Zahl n besteht

    @type n: int
    @param n: eine natürliche Zahl, die zu untersuchen ist
    @rtype: list[tuple(primzahl,vielfacher der Primzahl)] oder bool
    @return: Primzahl und dessen Vielfacher, das mehrmals, so viele Primzahlen wie es gibt, aus denen n besteht
    """
    multiples = [(1, n)]
    for prim in primRepeat(primFak(n)):
        multiples += [(prim[0], round(n / prim[0]))]
    return multiples


def isPrimMultiple(isIt: int, multiples1: list, dontReturnList=True):
    """Ist die Zahl der Vielfache in überhaupt irgendeiner Primzahl

    @type isIt: int
    @param isIt: die Zahl die zu untersuchen ist
    @type multiples1: list[int]
    @param multiple1: Liste an Vielfachern von denen einer zutreffen muss, bei [2,3] ist es True, wenn es das zweifache oder dreifache einer Primzahl ist
    @type dontReturnList: bool
    @param dontReturnList: wenn ja, dann wird nur ausgegeben ob es ein Vielfacher einer Primzahl ist, ansonsten die Liste für welche Vielfacher es zutrifft
    @rtype: list[bool] oder bool
    @return: True wenn Primzahlvielfacher, Liste aus True für ja für welche Multiplikatioren ja
    """
    areThey: list = []
    multiples2 = primMultiple(isIt)
    for multiple1 in multiples1:
        for multiple2 in multiples2:
            areThey += [True if multiple1 == multiple2[1] else False]
            if dontReturnList and areThey[-1]:
                return True
    if dontReturnList:
        return False
    return areThey


class Program:
    def parameters(self, argv, neg="") -> Iterable[Union[set, set, set]]:
        """Parameter in der Shell werden hier vorverarbeitet.
        Die Paraemter führen dazu, dass Variablen gesetzt werden, z.B.
        eine Menge die als Befehl kodiert, welche Zeilen und eine die kodiert
        welche Spaltennummer ausgegeben werden sollen.
        Außerdem welche extra Tabellen geladen werden sollen.

        return paramLines, rowsAsNumbers, rowsOfcombi

        @type  argv: list
        @param argv: Programmparamenter
        @type  neg: str
        @param neg: MinusZeichen davor ?
        @rtype: set, set, set
        @return: Zeilen, Spalten, Spalten anderer Tabellen
        """
        global infoLog
        if len(argv) == 1 and neg == "":
            cliout("Versuche Parameter -h")
        rowsAsNumbers = set()
        paramLines = set()
        bigParamaeter: list = []
        rowsOfcombi: set = set()
        for arg in argv[1:]:
            if len(arg) > 0 and arg[0] == "-":
                if (
                    len(arg) > 1
                    and arg[1] == "-"
                    and len(bigParamaeter) > 0
                    and bigParamaeter[-1] == "spalten"
                ):  # unteres Kommando
                    if arg[2:9] == "breite=":
                        if arg[9:].isdecimal():
                            self.tables.textWidth = abs(int(arg[9:]))
                    elif arg[2:10] == "breiten=":
                        self.tables.breitenn = []
                        for breite in arg[10:].split(","):
                            if breite.isdecimal():
                                self.tables.breitenn += [int(breite)]
                    elif arg[2:20] == "keinenummerierung":
                        self.tables.nummeriere = False
                    elif arg[2:13] == "religionen=" or arg[2:11] == "religion=":
                        for religion in (
                            arg[13:].split(",")
                            if arg[2:13] == "religionen="
                            else arg[11:].split(",")
                        ):
                            if religion == neg + "sternpolygon":
                                rowsAsNumbers |= {0, 6, 36}
                            elif religion in [
                                neg + "babylon",
                                neg + "dertierkreiszeichen",
                            ]:
                                rowsAsNumbers.add(0)
                                rowsAsNumbers.add(36)
                            elif religion in [
                                neg + "gleichfoermigespolygon",
                                neg + "gleichförmigespolygon",
                                neg + "nichtsternpolygon",
                                neg + "polygon",
                            ]:
                                rowsAsNumbers.add(16)
                                rowsAsNumbers.add(36)
                            elif religion in [
                                neg + "galaxien",
                                neg + "galaxie",
                                neg + "schwarzesonne",
                                neg + "schwarzesonnen",
                                neg + "universum",
                                neg + "universen",
                                neg + "kreis",
                                neg + "kreise",
                                neg + "kugel",
                                neg + "kugeln",
                            ]:
                                rowsAsNumbers.add(23)
                    elif (
                        arg[2:11] == "galaxien="
                        or arg[2:16] == "alteschriften="
                        or arg[2:9] == "kreise="
                    ):
                        for thing in arg[(arg.find("=") + 1) :].split(","):
                            if thing in [neg + "babylon", neg + "tierkreiszeichen"]:
                                rowsAsNumbers.add(1)
                                rowsAsNumbers.add(2)
                            elif thing in [neg + "thomas", neg + "thomasevangelium"]:
                                rowsAsNumbers.add(3)
                    elif arg[2:] in [
                        "groessenordnung" + neg,
                        "strukturgroesse" + neg,
                        "groesse" + neg,
                        "stufe" + neg,
                    ]:
                        rowsAsNumbers.add(4)
                        rowsAsNumbers.add(21)
                    elif arg[2:] in [
                        "universum" + neg,
                        "transzendentalien" + neg,
                        "strukturalien" + neg,
                    ]:
                        rowsAsNumbers |= {5, 54, 55}
                    elif arg[2:15] in ["menschliches="]:
                        for thing in arg[(arg.find("=") + 1) :].split(","):
                            if thing in [neg + "liebe", neg + "ethik"]:
                                rowsAsNumbers |= {8, 9, 28}
                            if thing in [
                                neg + "glauben",
                                neg + "erkenntnis",
                                neg + "glaube",
                            ]:
                                rowsAsNumbers |= {59}
                            elif thing in [
                                neg + "angreifbar",
                                neg + "angreifbarkeit",
                            ]:
                                rowsAsNumbers |= {58, 57}
                            elif thing in [
                                neg + "motive",
                                neg + "motivation",
                                neg + "motiv",
                            ]:
                                rowsAsNumbers |= {10, 18, 42}
                            elif thing in [
                                neg + "errungenschaften",
                                neg + "ziele",
                                neg + "erhalten",
                            ]:
                                rowsAsNumbers.add(11)
                            elif thing in [
                                neg + "erwerben",
                                neg + "erlernen",
                                neg + "lernen",
                                neg + "evolutionaer",
                                neg + "evolutionär",
                                neg + "intelligenz",
                                neg + "kreativität",
                                neg + "kreativitaet",
                                neg + "kreativ",
                            ]:
                                rowsAsNumbers |= {12, 47, 27, 13}
                            elif thing in [
                                neg + "brauchen",
                                neg + "benoetigen",
                                neg + "benötigen",
                                neg + "notwendig",
                            ]:
                                rowsAsNumbers |= {13, 14}
                            elif thing in [
                                neg + "krankheit",
                                neg + "krankheiten",
                                neg + "pathologisch",
                                neg + "pathologie",
                                neg + "psychiatrisch",
                            ]:
                                rowsAsNumbers.add(24)
                            elif thing in [
                                neg + "alpha",
                                neg + "beta",
                                neg + "omega",
                                neg + "sigma",
                            ]:
                                rowsAsNumbers.add(46)
                            elif thing in [neg + "anfuehrer", neg + "chef"]:
                                rowsAsNumbers.add(29)
                            elif thing in [neg + "beruf", neg + "berufe"]:
                                rowsAsNumbers.add(30)
                            elif thing in [
                                neg + "loesungen",
                                neg + "loesung",
                                neg + "lösungen",
                                neg + "lösungen",
                            ]:
                                rowsAsNumbers.add(31)
                            elif thing in [neg + "musik"]:
                                rowsAsNumbers.add(33)
                    elif arg[2:12] == "procontra=" or arg[2:16] == "dagegendafuer=":
                        for thing in arg[(arg.find("=") + 1) :].split(","):
                            if thing in [neg + "pro", neg + "dafeuer"]:
                                rowsAsNumbers |= {17, 48}
                            elif thing in [neg + "contra", neg + "dagegen"]:
                                rowsAsNumbers |= {15, 26}
                    elif arg[2 : 7 + len(neg)] == "licht" + neg:
                        rowsAsNumbers |= {20, 27}
                    elif arg[2:12] == "bedeutung=":
                        for thing in arg[(arg.find("=") + 1) :].split(","):
                            if thing in [
                                neg + "primzahlen",
                                neg + "vielfache",
                                neg + "vielfacher",
                            ]:
                                rowsAsNumbers.add(19)
                            elif thing in [
                                neg + "anwendungdersonnen",
                                neg + "anwendungenfuermonde",
                            ]:
                                rowsAsNumbers.add(22)
                            elif thing in [
                                neg + "zaehlung",
                                neg + "zaehlungen",
                                neg + "zählungen",
                                neg + "zählung",
                            ]:
                                rowsAsNumbers |= {25, 45}
                            elif thing in [
                                neg + "jura",
                                neg + "gesetzeslehre",
                                neg + "recht",
                            ]:
                                rowsAsNumbers.add(34)
                            elif thing in [neg + "vollkommenheit", neg + "geist"]:
                                rowsAsNumbers.add(35)
                            elif thing in [
                                neg + "gestirn",
                                neg + "mond",
                                neg + "sonne",
                                neg + "planet",
                            ]:
                                self.tables.spalteGestirn = True
                            elif thing in [
                                neg + "primvielfache",
                                neg + "primvielfacher",
                                neg + "primzahlenvielfacher",
                                neg + "primzahlenvielfache",
                            ]:
                                self.tables.ifPrimMultis = True
                    elif arg[2 : 11 + len(neg)] == "symbole" + neg:
                        rowsAsNumbers |= {36, 37}
                    elif arg[2:30] == "primzahlvielfachesuniversum=":
                        for word in arg[30:].split(","):
                            if word.isdecimal():
                                self.tables.primUniversePrimsSet.add(int(word))
                    elif arg[2:29] == "primzahlvielfachesuniversum":
                        self.tables.primUniverseRow = True
                    elif arg[2:10] == "konzept=" or arg[2:11] == "konzepte=":
                        for word in (
                            arg[10:].split(",")
                            if arg[2:10] == "konzept="
                            else arg[11:].split(",")
                        ):
                            if word in [
                                neg + "weisheit",
                                neg + "metaweisheit",
                                neg + "meta-weisheit",
                                neg + "idiot",
                                neg + "weise",
                                neg + "optimal",
                                neg + "optimum",
                            ]:
                                self.tables.generRows |= {(40, 41)}
                            elif word in [
                                neg + "gut",
                                neg + "böse",
                                neg + "lieb",
                                neg + "schlecht",
                            ]:
                                self.tables.generRows |= {(38, 39)}
                                rowsAsNumbers |= {52, 53}
                            elif word in [
                                neg + "zeit",
                                neg + "raum",
                                neg + "zeitlich",
                                neg + "räumlich",
                            ]:
                                self.tables.generRows |= {(49, 50)}
                            elif word in [
                                neg + "meinungen",
                                neg + "anderemenschen",
                                neg + "ruf",
                            ]:
                                self.tables.generRows |= {(60, 61)}
                    elif arg[2:17] == "inkrementieren=":
                        for word in arg[17:].split(","):
                            if word in [
                                neg + "universum",
                            ]:
                                rowsAsNumbers.add(43)

                if (
                    len(arg) > 1
                    and arg[1] == "-"
                    and len(bigParamaeter) > 0
                    and bigParamaeter[-1] == "zeilen"
                ):  # unteres Kommando
                    if arg[2:7] == "zeit=":
                        for subpara in arg[7:].split(","):
                            if neg + "=" == subpara:
                                paramLines.add("=")
                            elif neg + "<" == subpara:
                                paramLines.add("<")
                            elif neg + ">" == subpara:
                                paramLines.add(">")
                    elif arg[2:11] == "zaehlung=":
                        for word in arg[11:].split(","):
                            if (
                                word.isdecimal()
                                or (word[1:].isdecimal() and word[0] == neg)
                            ) and (
                                (int(word) > 0 and neg == "")
                                or (int(word) < 0 and neg != "")
                            ):
                                paramLines.add(str(abs(int(word))) + "z")
                    elif arg[2:15] == "hoehemaximal=":
                        if arg[15:].isdecimal():
                            self.tables.textHeight = abs(int(arg[15:]))
                    elif arg[2:6] == "typ=":
                        for word in arg[6:].split(","):
                            if word == neg + "sonne":
                                paramLines.add("sonne")
                            elif word == neg + "schwarzesonne":
                                paramLines.add("schwarzesonne")
                            elif word == neg + "planet":
                                paramLines.add("planet")
                            elif word == neg + "mond":
                                paramLines.add("mond")
                    elif arg[2:21] == "vielfachevonzahlen=":
                        for word in arg[21:].split(","):
                            if (
                                word.isdecimal()
                                or (word[1:].isdecimal() and word[0] == neg)
                            ) and (
                                (int(word) > 0 and neg == "")
                                or (int(word) < 0 and neg != "")
                            ):
                                paramLines.add(str(abs(int(word))) + "v")
                    elif arg[2:20] == "primzahlvielfache=":
                        for word in arg[20:].split(","):
                            if (
                                word.isdecimal()
                                or (word[1:].isdecimal() and word[0] == neg)
                            ) and (
                                (int(word) > 0 and neg == "")
                                or (int(word) < 0 and neg != "")
                            ):
                                paramLines.add(str(abs(int(word))) + "p")
                    elif arg[2:22] == "vorhervonausschnitt=":
                        paramLines |= self.tables.getPrepare.parametersCmdWithSomeBereich(
                            arg[22:], "a", neg
                        )
                    elif arg[2:21] == "nachtraeglichdavon=":
                        paramLines |= self.tables.getPrepare.parametersCmdWithSomeBereich(
                            arg[21:], "z", neg
                        )
                elif (
                    len(arg) > 1
                    and arg[1] == "-"
                    and len(bigParamaeter) > 0
                    and bigParamaeter[-1] == "kombination"
                ):  # unteres Kommando
                    self.ifCombi = True
                    """if arg[2:6] == "und=":
                        for word in arg[6:].split(","):
                            if (
                                word.isdecimal()
                                or (word[1:].isdecimal() and word[0] == neg)
                            ) and (
                                (int(word) > 0 and neg == "")
                                or (int(word) < 0 and neg != "")
                            ):
                                paramLines.add(str(abs(int(word))) + "ku")
                    elif arg[2:7] == "oder=":
                        for word in arg[7:].split(","):
                            if (
                                word.isdecimal()
                                or (word[1:].isdecimal() and word[0] == neg)
                            ) and (
                                (int(word) > 0 and neg == "")
                                or (int(word) < 0 and neg != "")
                            ):
                                paramLines.add(str(abs(int(word))) + "ko")
                    elif arg[2:] == "vonangezeigten" + neg:
                        paramLines.add("ka")"""
                    if arg[2:6] == "was=":
                        if neg == "":
                            paramLines.add("ka")
                        for thing in arg[(arg.find("=") + 1) :].split(","):
                            if thing in [
                                neg + "tiere",
                                neg + "tier",
                                neg + "lebewesen",
                            ]:
                                rowsOfcombi |= {1}
                            elif thing in [neg + "berufe", neg + "beruf"]:
                                rowsOfcombi |= {2}
                            elif thing in [
                                neg + "kreativität",
                                neg + "intelligenz",
                                neg + "kreativitaet",
                            ]:
                                rowsOfcombi |= {3}
                            elif thing in [neg + "liebe"]:
                                rowsOfcombi |= {4}
                            elif thing in [
                                neg + "transzendenz",
                                neg + "transzendentalien",
                                neg + "strukturalien",
                                neg + "alien",
                            ]:
                                rowsOfcombi |= {5}
                else:  # oberes Kommando
                    if arg[1:] in ["zeilen", "spalten", "kombination"]:
                        bigParamaeter += [arg[1:]]
                    elif arg[1:] in ["debug"]:
                        infoLog = True
                    elif arg[1:] in ["h", "help"] and neg == "":
                        self.help()
        return paramLines, rowsAsNumbers, rowsOfcombi

    def help(self):
        global folder
        place = os.path.join(
            os.getcwd(), os.path.dirname(__file__), os.path.basename("./readme.txt")
        )
        with open(place) as f:
            read_data = f.read()
        parser.REPLACE_COSMETIC = ()
        html = parser.format(read_data, replace_cosmetic=False)
        h = html2text.HTML2Text()
        h.style = "compact"
        plaintext = h.handle(html)
        plaintext = re.sub(r"\\--", "--", plaintext)
        plaintext = re.sub(r"(\*\s+[^\-])", r"\t\1", plaintext)
        plaintext = re.sub(r" \*\*", r"", plaintext)
        plaintext = re.sub(r"\*\s\*", r"", plaintext)
        plaintext = re.sub(r"(\n)([^\s])", r"\1\t\t\2", plaintext)
        cliout(plaintext)

    def start(self) -> tuple:
        global folder
        place = os.path.join(
            os.getcwd(), os.path.dirname(__file__), os.path.basename("./religion.csv")
        )
        """Einlesen der ersten Tabelle "religion.csv" zu self.relitable
        aller anderen csv dateien
        Parameter werden in Befehle und Nummernlisten gewandelt
        csv Dateien werden angehangen an self.relitable


        @rtype: tuple(int,set,set,list,set,list,set,list,list)
        @return: Spaltenanzahl, Zeilen Ja, Zeilen Nein, Religionstabelle, Spalten, weitere Tabelle daneben, spalten weitere Tabelle, weitere Tabelle für wie sql-join, deren spalten
        """
        with open(place, mode="r") as csv_file:
            self.relitable: list = []
            for i, col in enumerate(csv.reader(csv_file, delimiter=";")):
                self.relitable += [col]
                if i == 0:
                    self.RowsLen = len(col)
        paramLines, self.rowsAsNumbers, rowsOfcombi = self.parameters(sys.argv)
        paramLinesNot, self.rowsAsNumbersNot, rowsOfcombiNot = self.parameters(
            sys.argv, "-"
        )
        paramLines, paramLinesNot = self.tables.getPrepare.deleteDoublesInSets(
            paramLines, paramLinesNot
        )
        (
            self.rowsAsNumbers,
            self.rowsAsNumbersNot,
        ) = self.tables.getPrepare.deleteDoublesInSets(
            self.rowsAsNumbers, self.rowsAsNumbersNot
        )
        (rowsOfcombi, rowsOfcombiNot,) = self.tables.getPrepare.deleteDoublesInSets(
            rowsOfcombi, rowsOfcombiNot
        )
        self.tables.getPrepare.rowsAsNumbers = self.rowsAsNumbers
        self.tables.getOut.rowsAsNumbers = self.rowsAsNumbers

        self.relitable, rowsAsNumbers = self.tables.getConcat.readConcatCsv(
            self.relitable, self.rowsAsNumbers
        )
        self.relitable, self.rowsAsNumbers = self.tables.getConcat.concatRowsOfConcepts(
            self.relitable, self.tables.generRows, self.rowsAsNumbers
        )
        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.concatPrimCreativityType(
            self.relitable, self.rowsAsNumbers
        )
        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.concatMondExponzierenLogarithmusTyp(
            self.relitable, self.rowsAsNumbers
        )
        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.concat1RowPrimUniverse2(
            self.relitable, self.rowsAsNumbers
        )
        (self.relitable, self.rowsAsNumbers,) = self.tables.getConcat.concatLovePolygon(
            self.relitable, self.rowsAsNumbers
        )

        if self.ifCombi:
            (
                animalsProfessionsTable,
                self.relitable,
                kombiTable_Kombis,
                maintable2subtable_Relation,
            ) = self.tables.getCombis.readKombiCsv(
                self.relitable, self.rowsAsNumbers, rowsOfcombi
            )
        else:
            animalsProfessionsTable = []
            kombiTable_Kombis = []
            maintable2subtable_Relation = []
        return (
            self.RowsLen,
            paramLines,
            paramLinesNot,
            self.relitable,
            self.rowsAsNumbers,
            animalsProfessionsTable,
            rowsOfcombi,
            kombiTable_Kombis,
            maintable2subtable_Relation,
        )

    def __init__(self):
        global Tables
        self.ifCombi = False
        self.tables = Tables()
        (
            self.RowsLen,
            paramLines,
            paramLinesNot,
            self.relitable,
            self.rowsAsNumbers,
            animalsProfessionsTable,
            rowsOfcombi,
            kombiTable_Kombis,
            maintable2subtable_Relation,
        ) = self.start()
        self.tables.getMainTable.createSpalteGestirn(self.relitable, self.rowsAsNumbers)
        self.tables.getPrepare.createRowPrimeMultiples(
            self.relitable,
            self.rowsAsNumbers,
            self.tables.getPrepare.setWidth(len(self.rowsAsNumbers)),
        )
        (
            finallyDisplayLines,
            newTable,
            numlen,
            rowsRange,
            old2newTable,
        ) = self.tables.getPrepare.prepare4out(
            paramLines, paramLinesNot, self.relitable, self.rowsAsNumbers,
        )
        if self.ifCombi:
            ChosenKombiLines = self.tables.getCombis.prepare_kombi(
                finallyDisplayLines,
                animalsProfessionsTable,
                paramLines,
                finallyDisplayLines,
                kombiTable_Kombis,
            )
            (
                finallyDisplayLines_kombi,
                newTable_kombi_1,
                lineLen_kombi_1,
                rowsRange_kombi_1,
                old2newTableAnimalsProfessions,
            ) = self.tables.getPrepare.prepare4out(
                set(),
                set(),
                animalsProfessionsTable,
                rowsOfcombi,
                self.tables.getCombis.sumOfAllCombiRowsAmount,
            )
            KombiTables = []
            for key, value in ChosenKombiLines.items():
                Tables = {}
                for kombiLineNumber in value:
                    into = self.tables.tableReducedInLinesByTypeSet(
                        newTable_kombi_1, {kombiLineNumber}
                    )
                    if len(into) > 0:
                        if key in Tables:
                            Tables[key] += [into[0]]
                        else:
                            Tables[key] = [into[0]]
                    # cliOut({0,kombiLineNumber}, oneTable, 2, rowsRange_kombi_1)
                KombiTables += [Tables]

            newTable = self.tables.getCombis.tableJoin(
                newTable,
                KombiTables,
                maintable2subtable_Relation,
                old2newTable,
                rowsOfcombi,
            )

        rowAmounts = self.tables.getOut.oneTabletoMany(newTable, True, rowsRange)
        for rowAmount in rowAmounts:
            self.tables.getOut.cliOut(
                finallyDisplayLines, newTable, numlen, rowsRange, rowAmount
            )
        alxp("4. minus-SPALTEN machen von nicht-HAUPT.csv")


Program()
# alxp(ColumnsRowsAmount)
# alxp(shellRowsAmount)
# inverted:
# \e[7mi
