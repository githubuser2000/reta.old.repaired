#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import math
import os
import sys
from copy import deepcopy
# from collections.abc import Iterable
from typing import Iterable, Union

import pyphen

dic = pyphen.Pyphen(lang="de_DE")  # Bibliothek für Worteilumbruch bei Zeilenumbruch
ColumnsRowsAmount, shellRowsAmount = (
    os.popen("stty size", "r").read().split()
)  # Wie viele Zeilen und Spalten hat die Shell ?
relitable = None
toYesdisplayRows: set = set()  # Welche Spalten anzeigen
toNotDisplayRows: set = set()  # Welche Spalten nicht anzeigen
infoLog = False
# c nächste silbe
# b nächste Spalte
# a nächste Zeile
# exit()
# originalLinesRange = range(len(newRows))
originalLinesRange = range(120)  # Maximale Zeilenanzahl
# realLinesRange = range(len(newRows[0]))
realLinesRange = range(100)  # Maximale Zeilenanzahl pro Tabellenzelle
# rowsRange = range(len(newRows[0][0]))
RowsLen = None
# rowsRange = range(50)
# printalx(newRows[0][1][0])

zaehlungen = [
    0,
    {},
    {},
    {},
    {},
]  # Strukturangaben zur Zeile wegen Mondzahlen und Sonnenzahlen
textwidth = 21  # Feste Spaltenbreite
textheight = 0
nummerierung = True  # Nummerierung der Zeilen, z.B. Religion 1,2,3
spaltegestirn = False
breiten: list = []
primuniverse = False  # ob "primenumbers.csv" gelesen werden soll
puniverseprims: set = set()  # welche Spalten von "primenumbers.csv"
ifCombi = False
# rowsAsNumbers.add(1)
religionNumbers: list = []
ifprimmultis = False


# def getRowAmountofAnyPart():
#    global puniverseprims, rowsAsNumbers
#    return {
#        "alltogether": len(puniverseprims) + len(rowsAsNumbers) + len(rowsOfcombi),
#        "main": len(rowsAsNumbers),
#        "prim": len(puniverseprims),
#        "combi": len(rowsOfcombi),
#    }


def printalx(text):
    """Für mich, damit ich mal alle prints ausschalten kann zum vorführen,
    wenn ich noch beim Entwicklen war."""
    if infoLog:
        print(text)


class Tables:
    def __init__(self):
        self.getPrepare = self.prepare()
        self.getCombis = self.combi()
        self.getConcat = self.concat()
        self.getOut = self.output()

    class output:
        def cliOut(
            self, finallyDisplayLines: set, newRows: list, numlen: int, rowsRange: range
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
            global religionNumbers

            def findMaxCellTextLen(
                self, finallyDisplayLines: set, newRows: list, rowsRange: set
            ) -> list:
                """Gibt eine Liste zurück mit allen maximalen Zwellhoehen pro alle Zellen einer Zeile

                @type finallyDisplayLines: set
                @param finallyDisplayLines: Zeilen die ausgegeben werden sollen
                @type newRows: list
                @param newRows: Tabelle um die es geht
                @type rowsRange: set
                @param rowsRange: range(spaltenanzahl)
                @rtype: dict[int,int]
                @return: Zellhöhen pro Zeile
                """
                global religionNumbers
                maxCellTextLen: dict = {}
                # for k in finallyDisplayLines: # n Linien einer Zelle, d.h. 1 EL = n Zellen
                for k, (f, r) in enumerate(
                    zip(newRows, finallyDisplayLines)
                ):  # n Linien einer Zelle, d.h. 1 EL = n Zellen
                    for iterWholeLine, m in enumerate(
                        rowsRange
                    ):  # eine Bildhschirm-Zeile immer
                        # for i in rowsAsNumbers: # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                        for i, c in enumerate(
                            newRows[k]
                        ):  # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
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
                return maxCellTextLen

            maxCellTextLen = findMaxCellTextLen(finallyDisplayLines, newRows, rowsRange)
            # for k in finallyDisplayLines: # n Linien einer Zelle, d.h. 1 EL = n Zellen
            # printalx("sdfsad"+str(len(newRows)))
            for k, (f, r) in enumerate(
                zip(newRows, finallyDisplayLines)
            ):  # n Linien einer Zelle, d.h. 1 EL = n Zellen
                #        actualPartLineLen = 0
                for iterWholeLine, m in enumerate(
                    rowsRange
                ):  # eine Bildhschirm-Zeile immer
                    #            actualPartLineLen += 1
                    line = (
                        ""
                        if not nummerierung
                        else (
                            "".rjust(numlen + 1)
                            if iterWholeLine != 0
                            else (str(r) + " ").rjust(numlen + 1)
                        )
                    )
                    rowsEmpty = 0
                    # for i in realLinesRange: # Teil-Linien nebeneinander als Teil-Spalten
                    maxRowsPossible = math.floor(
                        int(shellRowsAmount) / int(textwidth + 1)
                    )
                    # maxCellTextLen = 0
                    # for i in rowsAsNumbers: # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                    for i, c in enumerate(
                        newRows[k]
                    ):  # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                        # maxRowsPossible = math.floor( int(shellRowsAmount) / int(textwidth+1))
                        # if i < maxRowsPossible and k < 6:
                        # if i < maxRowsPossible:
                        if i + (1 if nummerierung else 0) <= len(breiten):
                            certaintextwidth = breiten[i + (0 if nummerierung else -1)]
                        else:
                            certaintextwidth = textwidth
                        if certaintextwidth > maxCellTextLen[i]:
                            i_textwidth = maxCellTextLen[i]
                        else:
                            i_textwidth = certaintextwidth
                        try:
                            # line += colorize(newRows[k][i][m].replace('\n', '').ljust(textwidth if textwidth < maxCellTextLen[i] else maxCellTextLen[i]), k, i)+' ' # neben-Einander
                            line += (
                                self.cliOut.colorize(
                                    newRows[k][i][m]
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
                                self.cliOut.colorize("".ljust(i_textwidth), r, i, True)
                                + " "
                            )  # neben-Einander
                    # if k < 6 and rowsEmpty != maxRowsPossible: #and m < actualPartLineLen:
                    #            printalx("sdf "+str(len(rowsAsNumbers))+' '+str(rowsEmpty))
                    if rowsEmpty != len(rowsAsNumbers) and (
                        iterWholeLine < textheight or textheight == 0
                    ):  # and m < actualPartLineLen:
                        print(line)
                        # printalx(colorize(str(rowsEmpty)+' '+str(maxRowsPossible), k))

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

    class prepare:
        def setWidth(self, rowsToDisplay, isMainTable):
            global rowsAsNumbers, relitable, puniverseprims
            # if not isMainTable:
            #    printalx("ee " + str(getRowAmountofAnyPart()))
            if (
                rowsToDisplay + (1 if nummerierung else 0) <= len(breiten) + 1
                and isMainTable
            ):
                certaintextwidth = breiten[rowsToDisplay + (-1 if nummerierung else -2)]
                printalx("ää " + str(rowsToDisplay + (-1 if nummerierung else -2)))
                printalx(
                    "ää2 "
                    + str(rowsToDisplay + (1 if nummerierung else 0))
                    + "<="
                    + str(len(breiten) + 1)
                )
            elif (
                not isMainTable
                and rowsToDisplay <= len(breiten) + 1 + len(rowsAsNumbers)
                and (rowsToDisplay - 2 + len(rowsAsNumbers)) in breiten
            ):
                printalx("üü " + str(rowsToDisplay - 2 + len(rowsAsNumbers)))
                certaintextwidth = breiten[rowsToDisplay - 2 + len(rowsAsNumbers)]
            else:
                printalx("öö " + str(rowsToDisplay - 2 + len(rowsAsNumbers)))
                printalx(
                    "öö "
                    + str(rowsToDisplay)
                    + "<="
                    + str(len(breiten))
                    + " + 1 + "
                    + str(len(rowsAsNumbers))
                )
                certaintextwidth = textwidth
            return certaintextwidth

        def parametersBereich(self, bereiche1: str, symbol: str, neg: str) -> set:
            """Erstellen des Befehls: Bereich

            @type bereiche1: str
            @param bereiche1: der Bereich von bis
            @type symbol: str
            @param symbol: welche Art Bereich soll es werden, symbol typisiert den Bereich
            @type neg: string
            @param neg: Vorzeichen, wenn es darum geht dass diese Zeilen nicht angezeigt werden sollen
            @rtype: set
            @return: Alle Zeilen die dann ausgegeben werden sollen
            """
            results = set()
            #    if bereiche1[:len(neg)] == neg:
            #        bereiche2 = bereiche1[len(neg):].split(',')
            #    else:
            #        bereiche2 = bereiche1[len(neg):].split(',')
            for bereiche3 in (
                bereiche1[len(neg) :].split(",")
                if bereiche1[: len(neg)] == neg
                else bereiche1.split(",")
            ):
                # printalx("aa " + bereiche3)
                if (
                    len(bereiche3) > len(neg)
                    and bereiche3 == neg + bereiche3[len(neg) :]
                    and len(neg) > 0
                ) or (len(bereiche3) > 0 and (neg + bereiche3[0]).isdigit()):
                    printalx(bereiche3 + " " + str(len(neg)))
                    maybeAmounts = bereiche3[len(neg) :].split("-")
                    printalx(str(maybeAmounts) + " " + str(neg))
                    if (
                        len(maybeAmounts) == 1
                        and maybeAmounts[0].isdecimal()
                        and maybeAmounts[0] != "0"
                    ):
                        results.add("1-" + symbol + "-" + maybeAmounts[0])
                    elif (
                        len(maybeAmounts) == 2
                        and maybeAmounts[0].isdecimal()
                        and maybeAmounts[0] != "0"
                        and maybeAmounts[1].isdecimal()
                        and maybeAmounts[1] != "0"
                    ):
                        results.add(
                            maybeAmounts[0] + "-" + symbol + "-" + maybeAmounts[1]
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
            global zaehlungen

            def diffset(wether, a: set, b: set) -> set:
                if wether:
                    # result = a.difference(b)
                    result = a - b
                    if result is None:
                        return set()
                    else:
                        return result
                return a

            numRange.remove(0)

            def cutset(wether, a: set, b: set) -> set:
                if wether:
                    # result = a.intersection(b)
                    result = a & b
                    # printalx("x "+str(result))
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

            # printalx("x0 "+str(numRange))
            # printalx("y0 "+str(paramLines))
            numRangeYesZ = set()
            ifZaehlungenAtAll = False
            for condition in paramLines:
                if (
                    len(condition) > 1
                    and condition[-1] == "z"
                    and condition[0:-1].isdecimal()
                ):  # ist eine von mehreren Zählungen
                    if not ifZaehlungenAtAll:
                        setZaehlungen(originalLinesRange[-1])
                        ifZaehlungenAtAll = True
                    zaehlungGesucht = int(
                        condition[0:-1]
                    )  # eine zählung = eine zahl, beginnend minimal ab 1
                    for n in numRange:  # nur die nummern, die noch infrage kommen
                        # zaehlungen = [0,{},{},{}]
                        if zaehlungen[3][n] == int(
                            zaehlungGesucht
                        ):  # 1-4:1,5-9:2 == jetzt ?
                            numRangeYesZ.add(n)
                            # numRange.remove(n)
            # printalx("xi "+str(numRangeYesZ))
            # printalx("xt "+str(numRange))
            numRange = cutset(ifZaehlungenAtAll, numRange, numRangeYesZ)
            # set().add
            # exit()
            ifTypAtAll = False
            numRangeYesZ = set()

            def moonsun(self, MoonNotSun: bool, numRangeYesZ: set):
                if not ifZaehlungenAtAll:
                    setZaehlungen(originalLinesRange[-1])
                for n in numRange:
                    if (zaehlungen[4][n][0] != []) == MoonNotSun:
                        numRangeYesZ.add(n)
                return numRangeYesZ

            for condition in paramLines:
                if "mond" in condition:
                    numRangeYesZ, ifTypAtAll = moonsun(True, numRangeYesZ), True
                elif "sonne" in condition:
                    numRangeYesZ, ifTypAtAll = moonsun(False, numRangeYesZ), True
                elif "planet" in condition:
                    ifTypAtAll = True
                    for n in numRange:
                        if n % 2 == 0:
                            numRangeYesZ.add(n)

            # printalx("x2 "+str(numRangeYesZ))
            numRange = cutset(ifTypAtAll, numRange, numRangeYesZ)
            # printalx("x3 "+str(numRange))

            primMultiples = []
            ifPrimAtAll = False
            for condition in paramLines:
                if (
                    len(condition) > 1
                    and condition[-1] == "p"
                    and condition[:-1].isdecimal()
                ):
                    ifPrimAtAll = True
                    primMultiples += [int(condition[:-1])]

            # printalx("x3 "+str(numRange))
            numRangeYesZ = set()
            for n in numRange:
                if isPrimMultiple(n, primMultiples):
                    numRangeYesZ.add(n)
            numRange = cutset(ifPrimAtAll, numRange, numRangeYesZ)
            # printalx("x4 "+str(numRangeYesZ))
            # printalx("x5 "+str(numRange))

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
                    # printalx(str(n))
                    for divisor in anyMultiples:
                        if n % divisor == 0:
                            numRangeYesZ.add(n)
                numRange = cutset(ifMultiplesFromAnyAtAll, numRange, numRangeYesZ)

            ifNachtraeglichAtAll = False
            for condition in paramLines:
                if "-z-" in condition:
                    if not ifNachtraeglichAtAll:
                        numRange = list(numRange)
                        numRange.sort()
                        ifNachtraeglichAtAll = True
                    a = fromUntil(condition.split("-z-"))
                    for i, n in enumerate(numRange.copy()):
                        if a[0] - 1 > i or a[1] - 1 < i:
                            numRange.remove(n)
            if ifNachtraeglichAtAll:
                numRange = set(numRange)
            # printalx(str(ifNachtraeglichAtAll)+' '+str(ifMultiplesFromAnyAtAll)+' '+str(ifPrimAtAll)+' '+str(ifTypAtAll)+' '+str(ifZeitAtAll)+' '+str(numRange))
            return numRange

        def prepare4out(
            paramLines: set,
            paramLinesNot: set,
            contentTable: list,
            rowsAsNumbers: set,
            isMainTable: bool = False,
        ) -> tuple:
            """Aus einer Tabelle wird eine gemacht, bei der der Zeilenumbruch durchgeführt wird.
            Dabei werden alle Spalten und Zeilen entfernt die nicht ausgegeben werden sollen.

            @type paramLines: set
            @param paramLines: welche Linien ja, andere fallen weg
            @type paramLinesNot: set
            @param paramLinesNot: welche Linien nein, werden abgezogen von ja
            @type contentTable: list
            @param contentTable: die Tabelle die verändert werden soll
            @type rowsAsNumbers: set
            @param rowsAsNumbers: anzuzeigende Spalten
            @rtype: tuple[set,set,int,range,list]
            @return: Zeilen die ausgegeben werden sollen, neue Tabelle, Nummer der letzten Zeile , \
                range aus zu zeigenden Spalten 1-n nicht alle , welche neuen Spalten welche alten waren und umgekehrt
            return finallyDisplayLines, newRows, numlen, rowsRange, old2newRows
            """
            global religionNumbers, breiten
            printalx("rr " + str(breiten))
            newRows: list = []
            printalx("1 " + str(originalLinesRange))
            if len(contentTable) > 0:
                headingsAmount = len(contentTable[0])
                rowsRange = range(headingsAmount)
            else:
                headingsAmount = 0
                rowsRange = range(0)
            finallyDisplayLines = FilterOriginalLines(
                set(originalLinesRange), paramLines
            )
            printalx("1,5 " + str(finallyDisplayLines))
            # printalx('s1 '+str(finallyDisplayLines))
            if not len(paramLinesNot) == 0:
                finallyDisplayLines2 = FilterOriginalLines(
                    set(originalLinesRange), paramLinesNot
                )
                printalx("34567 " + str(set(originalLinesRange) - finallyDisplayLines2))
                hasAnythingCanged = set(originalLinesRange) - finallyDisplayLines2 - {0}
                if len(hasAnythingCanged) > 0:
                    finallyDisplayLines -= finallyDisplayLines2
            # printalx('s2 '+str(finallyDisplayLines))
            finallyDisplayLines.add(0)
            finallyDisplayLines = list(finallyDisplayLines)
            finallyDisplayLines.sort()
            #    maxPartLineLen = 0
            numlen = len(str(finallyDisplayLines[-1]))
            printalx("2 " + str(finallyDisplayLines))
            old2newRows = ({}, {})
            for u, line in enumerate(contentTable):
                if u in finallyDisplayLines:
                    if isMainTable:
                        religionNumbers += [int(u)]
                    new2Lines = []
                    rowsToDisplay = 0
                    h = 0
                    for t, cell in enumerate(line):
                        if t in rowsAsNumbers:
                            # printalx(str(u)+' '+str(t)+' '+str(contentTable[u][t]))
                            rowsToDisplay += 1
                            newLines = [[]] * headingsAmount
                            # printalx(str(rowsToDisplay+(1 if nummerierung else 0))+' '+str(len(breiten)))
                            certaintextwidth = setWidth(rowsToDisplay, isMainTable)

                            new2Lines += [cellWork(cell, newLines, certaintextwidth, t)]
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
            isItNone = wrapping(cell, certaintextwidth)
            cell2: tuple = tuple()
            rest: str = cell
            while not isItNone is None:
                cell2 += isItNone
                isItNone = wrapping(cell2[-1], certaintextwidth)
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

    class combi:
        def fillBoth(self, liste1, liste2) -> Iterable[Union[list, list]]:
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

        def tableJoin(
            self,
            mainTable,
            manySubTables,
            maintable2subtable_Relation,
            old2newRows,
            rowsOfcombi,
        ):
            global religionNumbers
            rowsOfcombi = list(rowsOfcombi)
            rowsOfcombi.sort()
            # printalx("__ " + str(manySubTables))
            # table2 = deepcopy(mainTable)
            table2 = mainTable
            for colNum, (reliNum, col) in enumerate(zip(religionNumbers, mainTable)):
                for subTable in manySubTables:
                    if reliNum in subTable:
                        printalx(str(reliNum) + " " + str(subTable))
                        for row, bigCell in enumerate(mainTable[colNum]):
                            if old2newRows[1][row] in maintable2subtable_Relation[0]:
                                subRowNum = maintable2subtable_Relation[0][
                                    old2newRows[1][row]
                                ]
                                for subTableCell in subTable[reliNum]:
                                    if rowsOfcombi.index(subRowNum + 1) < len(
                                        subTableCell
                                    ):
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
            # printalx(str(table2))
            return table2

        def prepare_kombi(
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
            ChosenKombiLines: dict = {}
            for condition in paramLines:
                if "ka" == condition:
                    kombitypes["displaying"] = True
                    for MainLineNum in displayingMainLines:
                        for kombiLineNumber, kombiLine in enumerate(kombiTable_Kombis):
                            # printalx('ka '+str(displayingMainLines)+' '+str(kombiLine)+' '+str(finallyDisplayLines_kombi_1))
                            for kombiNumber in kombiLine:
                                if (
                                    kombiNumber in displayingMainLines
                                    and kombiNumber == MainLineNum
                                ):
                                    # printalx(str(MainLineNum) + "=" + str(kombiLineNumber + 1))
                                    if MainLineNum in ChosenKombiLines:
                                        ChosenKombiLines[MainLineNum] |= {
                                            kombiLineNumber + 1
                                        }
                                    else:
                                        ChosenKombiLines[MainLineNum] = {
                                            kombiLineNumber + 1
                                        }
            return ChosenKombiLines

        def cursorOf_2Tables(
            table1: list, table2: list, key: str
        ) -> Iterable[Union[list, list]]:
            """2 Tabellen, beide je erste Spalte muss der gleiche string key sein
            erstes Vorkommen jeweils dann stelle in Liste merken bei beiden
            Ergebnis sind 2 Listen mit den Stellen wo key:str in der ersten Spalte jeweils übereinstimmend ist

            @type table1: list
            @param table1: erste Tabell
            @type table2: list
            @param table2: zweite Tabelle
            @type key: str
            @param key: text bei dem beide Tabellen gleich sein sollen
            @rtype: tuple(list[int],list[int])
            @return: 2 Listen mit Zahlen wo Stellen sind wo key in beiden Tabellen vorkommt in der ersten Spalte
            """

            def perTable(self, table: list, key: str):
                result: list = []
                if len(table) > 0:
                    for i, row in enumerate(table[0]):
                        if key == row:
                            result += [i]
                return result

            return perTable(table1, key), perTable(table2, key)

        def readKombiCsv(
            self, relitable: list, rowsAsNumbers: set, rowsOfcombi: set
        ) -> tuple:
            """Fügt eine Tabelle neben der relitable nicht daneben sondern als join an, wie ein sql-join
            Hier wird aber noch nicht die join Operation durchgeführt
            momentan ist es noch fix auf animalsProfessions.csv

            @type relitable: list
            @param relitable: Haupttabelle relitable
            @type rowsAsNumbers: set
            @param rowsAsNumbers: welche Spalten der neuen Tabelle dazu kommen sollen
            @type rowsOfcombi: set
            @param rowsOfcombi: welche Spalten der neuen Tabelle dazu kommen sollen
            @rtype: tuple[list,list,list,list]
            @return: neue Tabelle, haupttabelle relitable, \
                Liste mit allen Zeilen der neuen Tabelle aus der ersten Spalte je Liste aus allem darin \
                das mit Komma getrennt wurde , was zu was gehört als Info für den join später
            return kombiTable, relitable, kombiTable_Kombis, maintable2subtable_Relation
            """
            headingsAmount = len(relitable[0])
            if not rowsOfcombi.isdisjoint({1, 2}):
                with open("animalsProfessions.csv", mode="r") as csv_file:
                    kombiTable = []
                    kombiTable_Kombis = []
                    for z, col in enumerate(csv.reader(csv_file, delimiter=";")):
                        kombiTable += [col]
                        kombiTable_Kombis_Col = []
                        if len(col) > 0 and z > 0:
                            for num in col[0].split(","):
                                if num.isdecimal():
                                    kombiTable_Kombis_Col += [int(num)]
                                else:
                                    raise ("not NUM !!!!! ")
                            kombiTable_Kombis += [kombiTable_Kombis_Col]
                    # printalx(str(kombiTable_Kombis))
                    relitable, animalsProfessionsCol = fillBoth(
                        relitable, list(kombiTable)
                    )
                    lastlen = 0
                    maxlen = 0
                    maintable2subtable_Relation = ({}, {})
                    for i, (animcol, relicol) in enumerate(
                        zip(animalsProfessionsCol, relitable)
                    ):
                        if i == 0:
                            lastlen = len(animcol)
                            if lastlen > maxlen:
                                maxlen = lastlen
                            for t, ac in enumerate(animcol[1:]):
                                maintable2subtable_Relation[0][
                                    len(relitable[0]) + t
                                ] = t
                                maintable2subtable_Relation[1][t] = (
                                    len(relitable[0]) + t
                                )
                            relitable[0] += list(animcol[1:]) + [""] * (
                                maxlen - len(animcol)
                            )
                        else:
                            relitable[i] += len(animcol[1:]) * [""] + [""] * (
                                maxlen - len(animcol)
                            )
                        if i == 0:
                            for u, heading in enumerate(relitable[0]):
                                for a in rowsOfcombi:
                                    if (
                                        u >= headingsAmount
                                        and u == headingsAmount + a - 1
                                    ):
                                        rowsAsNumbers.add(int(u))
            else:
                kombiTable = [[]]
                kombiTable_Kombis = [[]]
            return kombiTable, relitable, kombiTable_Kombis, maintable2subtable_Relation

    class concat:
        def readConcatCsv(self, relitable: list, rowsAsNumbers: set) -> list:
            """Fügt eine Tabelle neben der relitable an
            momentan ist es noch fix auf primnumbers.csv

            @type relitable: list
            @param relitable: Haupttabelle relitable
            @type rowsAsNumbers: set
            @param rowsAsNumbers: welche Spalten der neuen Tabelle dazu kommen sollen
            @rtype: list[list]
            @return: relitable + weitere Tabelle daneben
            """
            headingsAmount = len(relitable[0])
            if primuniverse:
                with open("primenumbers.csv", mode="r") as csv_file:
                    relitable, primUniverseLine = fillBoth(
                        relitable, list(csv.reader(csv_file, delimiter=";"))
                    )
                    lastlen = 0
                    maxlen = 0
                    for i, (primcol, relicol) in enumerate(
                        zip(primUniverseLine, relitable)
                    ):
                        lastlen = len(primcol)
                        if lastlen > maxlen:
                            maxlen = lastlen
                        relitable[i] += list(primcol) + [""] * (maxlen - len(primcol))
                        # printalx(str(list(primcol)))
                        if i == 0:
                            for u, heading in enumerate(relitable[0]):
                                if (
                                    heading.isdecimal()
                                    and int(heading) in puniverseprims
                                    and u >= headingsAmount
                                ):
                                    printalx(str(heading) + "ö" + str(puniverseprims))
                                    rowsAsNumbers.add(int(u))

                    # print(str(len(primUniverseLine[i]))+' '+str(len(relitable[i])))
                    # print(str((relitable[i])))
            return relitable

    class maintable:
        def createSpalteGestirn(self, relitable: list, rowsAsNumbers: set):
            """Fügt relitable eine Spalte hinzu, ob eine Zahl ein Mond oder eine Sonne ist
            Die Information muss dazu kommt aus moonNumber(i)[1]

            @type relitable: list
            @param relitable: Haupttabelle relitable
            @type rowsAsNumbers: set
            @param rowsAsNumbers: welche Spalten der neuen Tabelle nur betroffen sind
            @rtype:
            @return: nichts
            """
            if spaltegestirn:
                if len(relitable) > 0:
                    rowsAsNumbers.add(len(relitable[0]))
                # moonNumber
                for i, line in enumerate(relitable):
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

        def createRowPrimeMultiples(
            self, relitable: list, rowsAsNumbers: set, certaintextwidth: int
        ):
            if ifprimmultis:
                if len(relitable) > 0:
                    rowsAsNumbers.add(len(relitable[0]))
                # moonNumber
                for i, line in enumerate(relitable):
                    if i == 0:
                        line += wrapping("Primzahlenvielfache", certaintextwidth)
                    else:
                        line += wrapping("", certaintextwidth)
                    pass

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
            results += [oneResult]
            exponent += [i - 2]
    return results, exponent


def setZaehlungen(num: int,):  # mehrere Zählungen finden festlegen zum später auslesen
    """Eine Zahl wird untersucht und die Variable zaehlungen wegen dieser Ergänzt
    zaehlungen bekommt informationen über mondzahlen und sonnenzahlen
    i ist eine zu Untersuchende Zahl kleinergeich num
    zaehlungen[4][i] bekommt die mondtypen, d.h. (Basis, Exponent) immer
    zaehlungen[1][zaehlung] welche zählung fängt mit welcher Zahl an
    zaehlungen[2][i] ist welcher Zählung es ist für eine beliebige Zahl: 1 ist 1-4, 2 ist 5-9, 3 ist 10-16
    zaehlungen[3][i] ist auch welche Zählung es ist für eine beliebige Zahl: 1 ist 1-4, 2 ist 5-9, 3 ist 10-16
    zaehlungen[0] ist bis zu welcher Zahl diese Untersuchung beim letzten Mal durchgeführt wurde

    @type num: int
    @param num: zu untersuchende Zahl
    @rtype: kein Typ
    @return: nichts
    """
    global zaehlungen  # [bis zu welcher zahl, {zaehlung:zahl},{zahl:zaehlung},{jede zahl,zugehoerigeZaehlung}]
    wasMoon: bool = True
    if zaehlungen[0] == 0:
        isMoon = True
    else:
        isMoon = moonNumber(zaehlungen[0])[0] != []

    for i in range(int(zaehlungen[0]) + 1, num + 1):
        wasMoon = isMoon
        moonType = moonNumber(i)
        isMoon = moonType[0] != []
        if wasMoon and not isMoon:
            isMoon = False
            zaehlungen[1][len(zaehlungen[1]) + 1] = i
            zaehlungen[2][i] = len(zaehlungen[2]) + 1
        zaehlungen[3][i] = len(zaehlungen[2])
        zaehlungen[4][i] = moonType


def primFak(n: int) -> list:
    """Alle Primfaktoren einer Zahl als Liste mit mehrfachvorkommen, sofern ja

    @type n: int
    @param n: ein natürliche Zahl
    @rtype: list
    @return: alle Primfaktoren, ggf. mit Mehrfachvorkommen
    """
    global zaehlungen
    faktoren = []
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


def primRepeat(n: list) -> list:
    """Primfaktoren werden zusammengefasst in Liste aus Primfaktor hoch n

    @type n:  list
    @param n: Primfaktoren
    @rtype: list[tuple(n1,n2)]
    @return: Liste aus geordneten Paaren mit Primfaktor hoch n
    """
    global zaehlungen
    n.reverse()
    c = 1
    b = None
    d = []
    for a in n:
        if b == a:
            c += 1
        else:
            c = 1
        d += [[a, c]]
        b = a
    d.reverse()
    b = None
    f = []
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
    """Ist die Zahl der Vielfache n überhaupt irgendeiner Primzahl

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


# for e in range(1,11):
#    printalx("w "+str(isPrimMultiple(e, [2])))


class program:
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
        global textwidth, textheight, nummerierung, spaltegestirn, breiten, primuniverse, puniverseprims, ifCombi, infoLog, ifprimmultis
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
                            textwidth = abs(int(arg[9:]))
                    elif arg[2:10] == "breiten=":
                        breiten = []
                        for breite in arg[10:].split(","):
                            if breite.isdecimal():
                                breiten += [int(breite)]
                        # printalx("qq " + str(breiten))
                    elif arg[2:20] == "keinenummerierung":
                        nummerierung = False
                    elif arg[2:13] == "religionen=":
                        for religion in arg[13:].split(","):
                            if religion == neg + "sternpolygon":
                                rowsAsNumbers.add(0)
                                rowsAsNumbers.add(6)
                                rowsAsNumbers.add(36)
                            elif religion in [
                                neg + "babylon",
                                neg + "dertierkreiszeichen",
                            ]:
                                rowsAsNumbers.add(0)
                                rowsAsNumbers.add(36)
                            elif religion in [
                                neg + "gleichfoermigespolygon",
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
                        rowsAsNumbers.add(5)
                    elif arg[2:15] in ["menschliches="]:
                        for thing in arg[(arg.find("=") + 1) :].split(","):
                            if thing in [neg + "liebe", neg + "ethik"]:
                                rowsAsNumbers.add(8)
                                rowsAsNumbers.add(9)
                                rowsAsNumbers.add(28)
                            elif thing in [
                                neg + "motive",
                                neg + "motivation",
                                neg + "motiv",
                            ]:
                                rowsAsNumbers.add(10)
                                rowsAsNumbers.add(18)
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
                            ]:
                                rowsAsNumbers.add(12)
                            elif thing in [
                                neg + "brauchen",
                                neg + "benoetigen",
                                neg + "notwendig",
                            ]:
                                rowsAsNumbers.add(13)
                                rowsAsNumbers.add(14)
                            elif thing in [
                                neg + "krankheit",
                                neg + "pathologisch",
                                neg + "pathologie",
                                neg + "psychiatrisch",
                            ]:
                                rowsAsNumbers.add(24)
                            elif thing in [neg + "kreativ", neg + "kreativitaet"]:
                                rowsAsNumbers.add(27)
                            elif thing in [neg + "anfuehrer", neg + "chef"]:
                                rowsAsNumbers.add(29)
                            elif thing in [neg + "beruf", neg + "berufe"]:
                                rowsAsNumbers.add(30)
                            elif thing in [neg + "loesungen", neg + "loesung"]:
                                rowsAsNumbers.add(31)
                            elif thing in [neg + "musik"]:
                                rowsAsNumbers.add(33)
                    elif arg[2:12] == "procontra=" or arg[2:16] == "dagegendafuer=":
                        for thing in arg[(arg.find("=") + 1) :].split(","):
                            if thing in [neg + "pro", neg + "dafeuer"]:
                                rowsAsNumbers.add(17)
                            elif thing in [neg + "contra", neg + "dagegen"]:
                                rowsAsNumbers.add(15)
                    elif arg[2 : 7 + len(neg)] == "licht" + neg:
                        rowsAsNumbers.add(20)
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
                            elif thing in [neg + "zaehlung", neg + "zaehlungen"]:
                                rowsAsNumbers.add(25)
                            elif thing in [neg + "liebe", neg + "ethik"]:
                                rowsAsNumbers.add(26)
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
                                spaltegestirn = True
                            elif thing in [
                                neg + "primvielfache",
                                neg + "primvielfacher",
                                neg + "primzahlenvielfacher",
                                neg + "primzahlenvielfache",
                            ]:
                                ifprimmultis = True
                    elif arg[2 : 11 + len(neg)] == "symbole" + neg:
                        rowsAsNumbers.add(36)
                        rowsAsNumbers.add(37)
                    elif arg[2:30] == "primzahlvielfachesuniversum=":
                        for word in arg[30:].split(","):
                            if word.isdecimal():
                                primuniverse = True
                                puniverseprims.add(int(word))

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
                            textheight = abs(int(arg[15:]))
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
                        paramLines |= self.tables.getPrepare.parametersBereich(
                            arg[22:], "a", neg
                        )
                    elif arg[2:21] == "nachtraeglichdavon=":
                        paramLines |= self.tables.getPrepare.parametersBereich(
                            arg[21:], "z", neg
                        )
                #                    if arg[21:21+len(neg)] == neg:
                #                        maybeAmounts=arg[21+len(neg):].split('-')
                #                        if len(maybeAmounts) == 1 and maybeAmounts[0].isdecimal() and maybeAmounts[0] != "0":
                #                            paramLines.add('1-z-'+maybeAmounts[0])
                #                        elif len(maybeAmounts) == 2 and maybeAmounts[0].isdecimal() and maybeAmounts[0] != "0" and maybeAmounts[1].isdecimal() and maybeAmounts[1] != "0":
                #                            paramLines.add(maybeAmounts[0]+'-z-'+maybeAmounts[1])
                elif (
                    len(arg) > 1
                    and arg[1] == "-"
                    and len(bigParamaeter) > 0
                    and bigParamaeter[-1] == "kombination"
                ):  # unteres Kommando
                    ifCombi = True
                    if arg[2:6] == "und=":
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
                        paramLines.add("ka")
                    elif arg[2:6] == "was=":
                        for thing in arg[(arg.find("=") + 1) :].split(","):
                            if thing in [
                                neg + "tiere",
                                neg + "tier",
                                neg + "lebewesen",
                            ]:
                                rowsOfcombi |= {1}
                            elif thing in [neg + "berufe", neg + "beruf"]:
                                rowsOfcombi |= {2}
                else:  # oberes Kommando
                    if arg[1:] in ["zeilen", "spalten", "kombination"]:
                        bigParamaeter += [arg[1:]]
                if arg[1:] in ["debug"]:
                    infoLog = True
        return paramLines, rowsAsNumbers, rowsOfcombi

    def start(self) -> tuple:
        """Einlesen der ersten Tabelle "religion.csv" zu relitable
        aller anderen csv dateien
        Parameter werden in Befehle und Nummernlisten gewandelt
        csv Dateien werden angehangen an relitable


        @rtype: tuple(int,set,set,list,set,list,set,list,list)
        @return: Spaltenanzahl, Zeilen Ja, Zeilen Nein, Religionstabelle, Spalten, weitere Tabelle daneben, spalten weitere Tabelle, weitere Tabelle für wie sql-join, deren spalten
        """
        with open("religion.csv", mode="r") as csv_file:
            relitable = []
            for i, col in enumerate(csv.reader(csv_file, delimiter=";")):
                relitable += [col]
                if i == 0:
                    RowsLen = len(col)
        paramLines, rowsAsNumbers, rowsOfcombi = self.parameters(sys.argv)
        paramLinesNot, rowsAsNumbersNot, rowsOfcombiNot = self.parameters(sys.argv, "-")
        #    printalx(str(paramLines) + ' ' + str(rowsAsNumbers))
        #    printalx(str(paramLinesNot) + ' ' + str(rowsAsNumbersNot))
        paramLines, paramLinesNot = self.tables.getPrepare.deleteDoublesInSets(
            paramLines, paramLinesNot
        )
        rowsAsNumbers, rowsAsNumbersNot = self.tables.getPrepare.deleteDoublesInSets(
            rowsAsNumbers, rowsAsNumbersNot
        )
        rowsOfcombi, rowsOfcombiNot = self.tables.getPrepare.eleteDoublesInSets(
            rowsOfcombi, rowsOfcombiNot
        )
        #    printalx(str(paramLines) + ' ' + str(rowsAsNumbers))
        #    printalx(str(paramLinesNot) + ' ' + str(rowsAsNumbersNot))
        relitable = self.tables.concat.readConcatCsv(relitable, rowsAsNumbers)
        if ifCombi:
            (
                animalsProfessionsTable,
                relitable,
                kombiTable_Kombis,
                maintable2subtable_Relation,
            ) = self.tables.combi.readKombiCsv(relitable, rowsAsNumbers, rowsOfcombi)
        else:
            animalsProfessionsTable = []
            kombiTable_Kombis = []
            maintable2subtable_Relation = []
        return (
            RowsLen,
            paramLines,
            paramLinesNot,
            relitable,
            rowsAsNumbers,
            animalsProfessionsTable,
            rowsOfcombi,
            kombiTable_Kombis,
            maintable2subtable_Relation,
        )

    def __init__(self):
        global relitable, rowsAsNumbers, Tables
        (
            RowsLen,
            paramLines,
            paramLinesNot,
            relitable,
            rowsAsNumbers,
            animalsProfessionsTable,
            rowsOfcombi,
            kombiTable_Kombis,
            maintable2subtable_Relation,
        ) = self.start()
        # printalx(str(animalsProfessionsTable))
        printalx(str(paramLines) + " " + str(rowsAsNumbers))
        # headingsAmount = len(relitable[0])
        self.tables = Tables()
        self.tables.createSpalteGestirn(relitable, rowsAsNumbers)
        self.tables.createRowPrimeMultiples(
            relitable,
            rowsAsNumbers,
            self.tables.getPrepare.setWidth(len(rowsAsNumbers), False),
        )
        #    printalx(str(relitable))
        (
            finallyDisplayLines,
            newTable,
            numlen,
            rowsRange,
            old2newTable,
        ) = self.tables.getPrepare.prepare4out(
            paramLines, paramLinesNot, relitable, rowsAsNumbers, isMainTable=True
        )
        printalx(str(paramLines) + " " + str(paramLinesNot))
        if ifCombi:
            (
                finallyDisplayLines_kombi_1,
                newTable_kombi_1,
                lineLen_kombi_1,
                rowsRange_kombi_1,
                old2newTableAnimalsProfessions,
            ) = self.tables.getPrepare.prepare4out(
                set(), set(), animalsProfessionsTable, rowsOfcombi
            )
            # printalx(str(newTable))
            finallyDisplayLines_kombi_1 = self.tables.getPrepare.repare_kombi(
                finallyDisplayLines_kombi_1,
                animalsProfessionsTable,
                paramLines,
                finallyDisplayLines,
                kombiTable_Kombis,
            )
            KombiTables = []
            for key, value in finallyDisplayLines_kombi_1.items():
                Tables = {}
                for kombiLineNumber in value:
                    # printalx(str(kombiLineNumber))
                    if key in Tables:
                        Tables[key] += [
                            self.tables.tableReducedInLinesByTypeSet(
                                newTable_kombi_1, {kombiLineNumber}
                            )[0]
                        ]
                    else:
                        Tables[key] = [
                            self.tables.tableReducedInLinesByTypeSet(
                                newTable_kombi_1, {kombiLineNumber}
                            )[0]
                        ]
                    # cliOut({0,kombiLineNumber}, oneTable, 2, rowsRange_kombi_1)
                KombiTables += [Tables]
                printalx("-----------------------")

            printalx(str(finallyDisplayLines_kombi_1))
            printalx(str(newTable_kombi_1))
            printalx(str(maintable2subtable_Relation))
            printalx(str(old2newTable))
            printalx("")
            printalx(str(KombiTables))
            printalx("")
            #    cliOut(
            #        {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},
            #        newTable_kombi_1,
            #        lineLen_kombi_1,
            #        rowsRange_kombi_1,
            #    )
            newTable = self.tables.combi.tableJoin(
                newTable,
                KombiTables,
                maintable2subtable_Relation,
                old2newTable,
                rowsOfcombi,
            )
        self.tables.cliOut(finallyDisplayLines, newTable, numlen, rowsRange)
        print("1. Refactoring, dass alle Tabellenerweiterungen vereinheitlicht werden")
        print("2. darauf aufbauend die manuelle Spaltenbreiten programmieren")
        print(
            "3. Spalte ifprimmultis optional hinzufügen, die semantisch sagt was primzahl mit vielfacher derer bedeutet und meint, aber generiert"
        )


program()
# inverted:
# \e[7mi
"""
Wie refactoren?
Es gibt:
+ Es gibt Funktionen,
  + die mathematische Operationen ausführen
  + kleine Hilfsfunktionen sind
+ Es gibt Funktionen, die csv dateien
  + einlesen
  + vorverarbeiten
  + ausgeben
  + umverarbeiten
+ es gibt Programm-Hauptteil-Funktionen
  + start
  + programmparameter
  + Ausgabe-Hilfs-Funktionen

Mein Problem ist jetzt:
+ Mehrere Tabllenverarbeitungsmethoden unter einen Hut bekommen und deren
  Standards vereinheitlichen, so dass ich es einheitlich ansprechen kann
+ es sollte besser schon einprogrammiert sein, dass es mehrere
  + kombitabellen
  + nebentabellen
  geben kann

Was gibt es davon:
    + Haupttabelle
    + Nebentabelle
    + Kombitabelle
    + Gesamttabelle

Werte die davon vereinheitlicht werden sollten:
    + Tabelle selbst: eingelesene + angepasste
    + Spaltenanzahl und Zeilenanzahl
    + erlaubte Spalten und Zeilen als sets
    + bool werte

Funktionen davon, außer weniger relevante Hilfsfunktionen:
    + tableJoin
    + readKombiCsv, readConcatCsv
    + prepare4out, prepare_kombi
    + Tabellen und Listen, die Informationen enthalten über das Zusammenspiel
      dieser aller Tabellen

Lösungsgedanken:
    + eine Klasse für Tabellenarbeit
        + darin eine Klasse jeweils für
            + Kombitabellen
            + Nebentabellen
            + Haupttabelle
            + Gesamttabelle
        + daraus soll möglichst alles andere was geht raus gehalten werden
    + ich sollte das als erstes tun und alles andere darauf aufbauen
      d.h. ich überlege später was ich weiteres für Refactoring plane

"""
