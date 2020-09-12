#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
# import io
import math
# import os
# import pprint
# import re
# import sys
from copy import copy, deepcopy
from enum import Enum
# from collections.abc import Iterable
from typing import Iterable, Union

from center import alxp, bbcode, cliout, infoLog, os, output, shellRowsAmount

originalLinesRange = range(1028)  # Maximale Zeilenanzahl
parser = bbcode.Parser()
parser.add_simple_formatter("hr", "<hr />", standalone=True)
parser.add_simple_formatter("sub", "<sub>%(value)s</sub>")
parser.add_simple_formatter("sup", "<sup>%(value)s</sup>")


class OutputSyntax:
    def coloredBeginCol(self, num: int, rest: bool = False):
        return self.beginZeile

    def generateCell(self, num: int) -> str:
        return self.beginCell

    beginTable = ""
    endTable = ""
    beginCell = ""
    endCell = ""
    beginZeile = ""
    endZeile = ""


class csvSyntax(OutputSyntax):
    beginTable = ""
    endTable = ""
    beginCell = ""
    endCell = ""
    beginZeile = ""
    endZeile = ""


class markdownSyntax(OutputSyntax):

    beginTable = ""
    endTable = ""
    beginCell = "|"
    endCell = ""
    beginZeile = ""
    endZeile = ""


class bbCodeSyntax(OutputSyntax):
    def coloredBeginCol(self, num: int, rest: bool = False):
        num = int(num) if str(num).isdecimal() else 0
        numberType = primCreativity(num)

        if rest:
            # wenn der Fallm eintritt dass es leerer Text ist der frei ist
            return "[tr]"
            if num == 0:
                return "[tr]"
            elif num % 2 == 0:
                return "[tr]"
            else:
                return "[tr]"
        elif numberType == 1:
            if num % 2 == 0:
                return '[tr="background-color:#66ff66;font-size:18px;color:#000000;"]'
            else:
                return '[tr="background-color:#009900;font-size:18px;color:#ffffff;"]'
        elif numberType == 2 or num == 1:
            if num % 2 == 0:
                return '[tr="background-color:#ffff66;font-size:18px;color:#000099;"]'
            else:
                return '[tr="background-color:#555500;font-size:18px;color:#aaaaff;"]'
        elif numberType == 3:
            if num % 2 == 0:
                return '[tr="background-color:#9999ff;font-size:18px;color:#202000;"]'
            else:
                return '[tr="background-color:#000099;font-size:18px;color:#ffff66;"]'
        elif num == 0:
            return '[tr="background-color:#ff2222;font-size:18px;color:#002222;"]'

    beginTable = "[table]"
    endTable = "[/table]"
    beginCell = "[td]"
    endCell = "[/td]"
    beginZeile = "[tr]"
    endZeile = "[/tr]"


class htmlSyntax(OutputSyntax):
    @staticmethod
    def coloredBeginCol(num: int, rest: bool = False) -> str:
        num = int(num) if str(num).isdecimal() else 0
        numberType = primCreativity(num)

        if rest:
            # wenn der Fallm eintritt dass es leerer Text ist der frei ist
            return "<tr>"
            if num == 0:
                return "<tr>"
            elif num % 2 == 0:
                return "<tr>"
            else:
                return "<tr>"
        elif numberType == 1:
            if num % 2 == 0:
                return '<tr style="background-color:#66ff66;font-size:18px;color:#000000;">'
            else:
                return '<tr style="background-color:#009900;font-size:18px;color:#ffffff;">'
        elif numberType == 2 or num == 1:
            if num % 2 == 0:
                return '<tr style="background-color:#ffff66;font-size:18px;color:#000099;">'
            else:
                return '<tr style="background-color:#555500;font-size:18px;color:#aaaaff;">'
        elif numberType == 3:
            if num % 2 == 0:
                return '<tr style="background-color:#9999ff;font-size:18px;color:#202000;">'
            else:
                return '<tr style="background-color:#000099;font-size:18px;color:#ffff66;">'
        elif num == 0:
            return '<tr style="background-color:#ff2222;font-size:18px;color:#002222;">'

    def generateCell(self, num: int) -> str:
        return '<td  style="display:none" class="RowNumber ' + str(num) + '">'

    beginTable = "<table border=1>"
    endTable = "</table>"
    beginCell = "<td>"
    endCell = "</td>"
    # beginZeile = "<tr>"
    beginZeile = ""
    endZeile = "</tr>"


class Wraptype(Enum):
    pyphen = 1
    pyhyphen = 2
    nohyphen = 3


wrappingType: Wraptype = Wraptype.pyhyphen
# wrappingType: Wraptype = Wraptype.nohyphen
# wrappingType: Wraptype = Wraptype.pyphen


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def splitMoreIfNotSmall(textList: list, lenToBe: int) -> tuple:
    newList: list = []
    neededToBeDoneAtAll = False
    lenToBe -= 0
    for k, text in enumerate(textList):
        if len(text) > lenToBe:
            neededToBeDoneAtAll = True
    if neededToBeDoneAtAll:
        for k, text in enumerate(textList):
            if len(text) > lenToBe:
                newList += list(chunks(text, lenToBe))
            else:
                newList += [text]
    if neededToBeDoneAtAll:
        return tuple(newList)
    else:
        return tuple(textList)


def alxwrap(text: str, len_: int):
    global wrappingType
    """ Ich könnte hier beschleunigen, indem ich funktionszeiger verwende,
    anstelle jedes mal hier ein if durch gehen zu lassen
    """
    try:
        fill
    except NameError:
        return (text,)
    if "Brython" in sys.version.split():
        return (text,)
    try:
        return (
            dic.wrap(text, len_)
            if wrappingType == Wraptype.pypheni and len_ != 0
            else (
                splitMoreIfNotSmall(
                    fill(text, width=len_, use_hyphenator=h_de).split("\n"), len_
                )
                if wrappingType == Wraptype.pyhyphen and len_ != 0
                else (text,)
            )
        )
    except:
        return (
            dic.wrap(text, len_)
            if wrappingType == Wraptype.pyhyphen and len_ != 0
            else (
                splitMoreIfNotSmall(
                    fill(text, width=len_, use_hyphenator=h_de).split("\n"), len_
                )
                if wrappingType == Wraptype.pyphen and len_ != 0
                else (text,)
            )
        )


def render_color(tag_name, value, options, parent, context):
    return '<span style="color:%s;">%s</span>' % (tag_name, value)


# print(os.path.dirname(__file__))
for color in ("red", "blue", "green", "yellow", "black", "white"):
    parser.add_formatter(color, render_color)


class Tables:
    def getRowAmountofAnyPart(self):
        return {
            "numerierung": 1 if self.nummeriere else 0,
            "main prepare relitable orignal | combi & concat-prim drin": self.getPrepare.rowsAsNumbers,
            "prim (concat)": self.puniverseprims,
            "combi": (self.getCombis.rowsOfcombi, self.getCombis.ChosenKombiLines),
            "len(AllCombiRows)": self.getCombis.sumOfAllCombiRowsAmount,
            "row of prim multi generated": self.primUniverseRow,
        }

    @property
    def outType(self) -> OutputSyntax:
        return self.getOut.outType

    @outType.setter
    def outType(self, value: OutputSyntax):
        self.getOut.outType = value

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
    def breitenn(self, value: list):
        global shellRowsAmount
        for i, v in enumerate(copy(value)):
            value[i] = (
                v
                if shellRowsAmount > v + 7 or shellRowsAmount == 0
                else shellRowsAmount - 7
            )
        self.getPrepare.breiten = value
        self.getOut.breiten = value

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
        self.getCombis = self.Combi(self)
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
        def __init__(self):
            self.__oneTable = False
            self.__color = True
            self.__outType: OutputSyntax = OutputSyntax()

        @property
        def outType(self) -> OutputSyntax:
            return self.__outType

        @outType.setter
        def outType(self, value: OutputSyntax):
            self.__outType = value

        @property
        def color(self):
            return self.__color

        @color.setter
        def color(self, value: bool):
            self.__color = value

        @property
        def oneTable(self):
            return self.__oneTable

        @oneTable.setter
        def oneTable(self, value: bool):
            self.__oneTable = value

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
            global shellRowsAmount
            self.textwidth = (
                value
                if shellRowsAmount > value + 7 or shellRowsAmount == 0
                else shellRowsAmount - 7
            )

        def onlyThatColumns(self, table, onlyThatColumns):
            if len(onlyThatColumns) > 0:
                newTable = []
                for row in table:
                    newCol = []
                    for i in onlyThatColumns:
                        try:
                            newCol += [deepcopy(row[i - 1])]
                        except IndexError:
                            pass
                    newTable += [newCol]
                if len(newTable) > 0:
                    return newTable
                else:
                    return table
            else:
                return table

        def cliOut(
            self,
            finallyDisplayLinesSet: set,
            newTable: list,
            numlen: int,
            rowsRange: range,
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
            ):
                """Gibt eine Liste mit Integern zurück, bzw. eigentlich ein Dict.
                Die Integer sind die Zellbreite, die an einer Stelle mindestens
                maximal war. Dieses Maximum wird zurück gegeben, als eine Zahl,
                bestimmt durch Überprüfung mehrerer Felder.

                @type finallyDisplayLines: set
                @param finallyDisplayLines: Zeilen die ausgegeben werden sollen
                @type newTable: list
                @param newTable: Tabelle um die es geht
                @type rowsRange: set
                @param rowsRange: range(spaltenanzahl)
                @rtype: dict[int,int]
                @return: Zellbreiten
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

            def determineRowWidth(i, maxCellTextLen):
                if i < len(self.breiten):
                    # if i + (1 if self.nummerierung else 0) <= len(self.breiten):
                    certaintextwidth = self.breiten[i]
                else:
                    certaintextwidth = self.textwidth
                if certaintextwidth > maxCellTextLen[i]:
                    i_textwidth = maxCellTextLen[i]
                else:
                    i_textwidth = certaintextwidth
                return i_textwidth

            maxCellTextLen = findMaxCellTextLen(
                finallyDisplayLinesSet, newTable, rowsRange
            )
            self.finallyDisplayLines: list = list(finallyDisplayLinesSet)
            self.finallyDisplayLines.sort()
            # ColumnsRowsAmount, shellRowsAmount1 = (
            ##    os.popen("stty size", "r").read().split()
            # )  # Wie viele Zeilen und Spalten hat die Shell ?
            shellRowsAmount -= (
                len(str(self.finallyDisplayLines[-1]))
                if len(self.finallyDisplayLines) > 0 and shellRowsAmount != 0
                else 0
            )
            self.finallyDisplayLines[0] = ""
            lastSubCellIndex = -1
            lastlastSubCellIndex = -2
            headingfinished = False
            if type(self.__outType) is csvSyntax:
                strio = io.StringIO()
                writer = csv.writer(
                    strio,
                    quoting=csv.QUOTE_NONE,
                    delimiter=";",
                    quotechar="",
                )
            while (
                len(newTable) > 0
                and lastSubCellIndex < len(newTable[0]) - 1
                and lastSubCellIndex > lastlastSubCellIndex
            ):
                cliout(self.__outType.beginTable)
                lastlastSubCellIndex = lastSubCellIndex
                for (
                    BigCellLineNumber,
                    (TablesLineOfBigCells, filteredLineNumbersofOrignal),
                ) in enumerate(
                    zip(newTable, self.finallyDisplayLines)
                ):  # n Linien einer Zelle, d.h. 1 EL = n Zellen
                    for iterWholeLine, OneWholeScreenLine_AllSubCells in enumerate(
                        rowsRange
                    ):  # eine Bildhschirm-Zeile immer
                        line = (
                            ""
                            if not self.nummerierung
                            else self.__outType.generateCell(-1)
                            + (
                                "".rjust(numlen + 1)
                                if iterWholeLine != 0
                                else (str(filteredLineNumbersofOrignal) + " ").rjust(
                                    numlen + 1
                                )
                            )
                            + self.__outType.endCell
                        )
                        if type(self.__outType) is csvSyntax:
                            line = [line]
                        rowsEmpty = 0
                        sumWidths = 0
                        lastSubCellIndex = 0
                        emptyEntries: int = 0
                        entriesHere: int = 0
                        for subCellIndexRightLeft, subCellContentLeftRight in enumerate(
                            newTable[BigCellLineNumber]
                        ):  # SUBzellen: je Teil-Linie für machen nebeneinander als Teil-Spalten
                            if (
                                subCellIndexRightLeft > lastlastSubCellIndex
                                or self.__oneTable
                            ):
                                subCellWidth = determineRowWidth(
                                    subCellIndexRightLeft, maxCellTextLen
                                )
                                sumWidths += subCellWidth + 1
                                if sumWidths < shellRowsAmount or self.__oneTable:
                                    lastSubCellIndex = subCellIndexRightLeft
                                    try:
                                        entry = newTable[BigCellLineNumber][
                                            subCellIndexRightLeft
                                        ][OneWholeScreenLine_AllSubCells]
                                        entriesHere += 1
                                        if len(entry.strip()) == 0:
                                            emptyEntries += 1
                                        if (
                                            self.color
                                            and type(self.__outType) is OutputSyntax
                                        ):
                                            coloredSubCell = self.colorize(
                                                entry.replace("\n", "").ljust(
                                                    subCellWidth
                                                ),
                                                filteredLineNumbersofOrignal,
                                            )
                                        elif type(self.__outType) is csvSyntax:
                                            coloredSubCell = newTable[
                                                BigCellLineNumber
                                            ][subCellIndexRightLeft][
                                                OneWholeScreenLine_AllSubCells
                                            ].replace(
                                                "\n", ""
                                            )
                                        else:
                                            coloredSubCell = (
                                                self.__outType.generateCell(
                                                    subCellIndexRightLeft
                                                )
                                                + (
                                                    entry.replace("\n", "").ljust(
                                                        subCellWidth
                                                    )
                                                )
                                                + self.__outType.endCell
                                            )
                                        if type(self.__outType) is csvSyntax:
                                            line += [coloredSubCell]
                                        else:
                                            line += (
                                                coloredSubCell + " "
                                            )  # neben-Einander
                                    except:
                                        rowsEmpty += 1
                                        if (
                                            self.color
                                            and type(self.__outType) is OutputSyntax
                                        ):
                                            coloredSubCell = self.colorize(
                                                "".ljust(subCellWidth),
                                                filteredLineNumbersofOrignal,
                                                True,
                                            )
                                        else:
                                            coloredSubCell = (
                                                self.__outType.generateCell(
                                                    subCellIndexRightLeft
                                                )
                                                + "".ljust(subCellWidth)
                                                + self.__outType.endCell
                                            )
                                        if type(self.__outType) is csvSyntax:
                                            line += [coloredSubCell]
                                        else:
                                            line += (
                                                coloredSubCell + " "
                                            )  # neben-Einander
                                else:
                                    rowsEmpty += 1
                            else:
                                rowsEmpty += 1

                        if rowsEmpty != len(self.rowsAsNumbers) and (
                            iterWholeLine < self.textheight or self.textheight == 0
                        ):  # and m < actualPartLineLen:
                            if type(self.__outType) is markdownSyntax:
                                line += self.__outType.generateCell(
                                    subCellIndexRightLeft
                                )

                                if BigCellLineNumber > 0 and not headingfinished:
                                    headingfinished = True
                                if BigCellLineNumber == 0 and not headingfinished:
                                    addionalLine = ""
                                    for l in line:
                                        if l != self.__outType.generateCell(
                                            subCellIndexRightLeft
                                        ):
                                            addionalLine += "-"
                                        else:
                                            addionalLine += self.__outType.generateCell(
                                                subCellIndexRightLeft
                                            )

                                    line += "\n" + addionalLine
                            if emptyEntries != entriesHere:
                                if type(self.__outType) is csvSyntax:
                                    writer.writerow(line)
                                else:
                                    if (
                                        type(filteredLineNumbersofOrignal) is str
                                        and filteredLineNumbersofOrignal == ""
                                    ):
                                        filteredLineNumbersofOrignal = 0
                                    # if (
                                    #    not str(
                                    #        filteredLineNumbersofOrignal
                                    #    ).isdecimal()
                                    #    or True
                                    # ):
                                    #    sys.stderr.write(
                                    #        " ALXALX "
                                    #        + str(filteredLineNumbersofOrignal)
                                    #        + " "
                                    #        + line
                                    #        + "\n"
                                    #    )
                                    cliout(
                                        self.__outType.coloredBeginCol(
                                            filteredLineNumbersofOrignal
                                        )
                                        + line
                                        + self.__outType.endZeile
                                    )
                cliout(self.__outType.endTable)
                if self.__oneTable:
                    break
                if type(self.__outType) is csvSyntax:
                    cliout(strio.getvalue())

        def colorize(self, text, num: int, rest=False) -> str:

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
            num = int(num) if str(num).isdecimal() else 0
            if rest:
                if num == 0:
                    return "\033[41m" + "\033[30m" + "\033[1m" + text + "\033[0m"
                elif num % 2 == 0:
                    return "\033[47m" + "\033[30m" + text + "\033[0m" + "\033[0m"
                else:
                    return "\033[40m" + "\033[37m" + text + "\033[0m" + "\033[0m"
            elif moonNumber(num)[1] != []:
                # 00;33
                if num % 2 == 0:
                    return "\033[106m" + "\033[30m" + text + "\033[0m" + "\033[0m"
                else:
                    return "\033[46m" + "\033[30m" + text + "\033[0m" + "\033[0m"
            elif len(primFak(num)) == 1:
                if num % 2 == 0:
                    return "\033[103m" + "\033[30m" + "\033[1m" + text + "\033[0m"
                else:
                    return "\033[43m" + "\033[30m" + text + "\033[0m" + "\033[0m"
            elif num % 2 == 0:
                if num == 0:
                    return "\033[41m" + "\033[30m" + "\033[1m" + text + "\033[0m"
                else:
                    return "\033[47m" + "\033[30m" + text + "\033[0m" + "\033[0m"
            else:
                return "\033[100m" + "\033[37m" + text + "\033[0m" + "\033[0m"

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
            self.gezaehlt = False

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
            num = originalLinesRange[-1]
            if self.gezaehlt:
                return
            else:
                self.gezaehlt = True
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

        def wrapping(self, text: str, length: int) -> list:
            """Hier wird der Zeilenumbruch umgesetzt

            @type text: str
            @param text: Der Text dessen Zeilen umbgebrochen werden sollen
            @type lenght: int
            @param lenght: ab welcher Zeilenlänge umgebrochen werden soll
            @rtype: list[str]
            @return: Liste aus umgebrochenen Teilstrings
            """
            if len(text) > length and length != 0:
                isItNone = alxwrap(text, length)
            else:
                isItNone = None
            return isItNone

        def setWidth(self, rowToDisplay: int, combiRows1: int = 0) -> int:
            global shellRowsAmount
            if shellRowsAmount == 0:
                return 0
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
            """2 Zahlen sollen ein ordentlicher Zahlenbereich sein, sonst werden sie es

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

            for condition in paramLines:
                if "all" == condition:
                    return set(originalLinesRange)

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
                if "-n-" in condition:
                    ifZaehlungenAtAll = True
                    a = self.fromUntil(condition.split("-n-"))
                    for n in numRange.copy():
                        if a[0] <= n and a[1] >= n:
                            # numRange.remove(n)
                            numRangeYesZ.add(n)
            if ifZaehlungenAtAll:
                self.setZaehlungen(originalLinesRange[-1])
                numRangeYesZ2 = set()
                for n in numRange:  # nur die nummern, die noch infrage kommen
                    for z in numRangeYesZ:
                        if self.zaehlungen[3][n] == int(z):  # 1-4:1,5-9:2 == jetzt ?
                            numRangeYesZ2.add(n)
                            # numRange.remove(n)
                numRange = cutset(ifZaehlungenAtAll, numRange, numRangeYesZ2)
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

            toPowerIt: list = []
            ifPowerAtall: bool = False
            for condition in paramLines:
                if (
                    len(condition) > 1
                    and condition[-1] == "^"
                    and condition[:-1].isdecimal()
                ):
                    ifPowerAtall = True
                    toPowerIt += [int(condition[:-1])]
            if ifPowerAtall:
                numRangeYesZ = set()
                for base in toPowerIt:
                    for n in numRange:
                        onePower = pow(base, n)
                        numRangeMax = max(numRange)
                        if onePower <= numRangeMax:
                            numRangeYesZ |= {onePower}
                        else:
                            break
                numRange = cutset(ifPowerAtall, numRange, numRangeYesZ)

            numRangeYesZ = set()

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
            return finallyDisplayLines, newerTable, numlen, rowsRange, old2Rows
            """
            newerTable: list = []
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
            old2Rows: tuple = ({}, {})
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
                                old2Rows[0][t] = h
                                old2Rows[1][h] = t
                            h += 1
                    if new2Lines != []:
                        newerTable += [new2Lines]

            return finallyDisplayLines, newerTable, numlen, rowsRange, old2Rows

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
            # certaintextwidth -= 1
            cell = cell.strip()
            isItNone = self.wrapping(cell, certaintextwidth)
            cell2: tuple = tuple()
            rest: str = cell
            if certaintextwidth == 0:
                return [cell]

            while isItNone not in [None, ()]:
                cell2 += isItNone
                isItNone = self.wrapping(cell2[-1], certaintextwidth)
                rest = cell2[-1]
                cell2 = cell2[:-1]
                if len(rest) > certaintextwidth and isItNone is None:
                    cell2 += (rest[0:certaintextwidth],)
                    isItNone = (rest[certaintextwidth:],)
            else:
                cell2 += (rest[0:certaintextwidth],)
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
        def __init__(self, table):
            self.ChosenKombiLines: dict = {}
            self.sumOfAllCombiRowsAmount = 0
            self.table = table
            """alle  Schritte für kombi:
            1. lesen: KombiTable und relation, was von kombitable zu haupt gehört
                      und matrix mit zellen sind zahlen der kombinationen
                      d.h. 3 Sachen sind das Ergebnis
            2. prepare: die Zeilen, die infrage kommen für Kombi, d.h.:
                                    key = haupttabellenzeilennummer
                                    value = kombitabellenzeilennummer
            3. Zeilenumbruch machen, wie es bei der Haupt+Anzeige-Tabelle auch gemacht wurde
               prepare4out
            4. Vorbereiten des Joinens beider Tabellen direkt hier ( in völlig falsche Klasse ) rein programmiert
               (Müsste ich unbedingt mal refactoren!)
            5. joinen
            6. noch mal nur das ausgeben lassen, das nur ausgegeben werden soll
            7. letztendliche Ausagebe von allem!!
            """

        def prepareTableJoin(self, ChosenKombiLines, newTable_kombi_1):
            KombiTables = []
            for key, value in ChosenKombiLines.items():
                """Zeilennummern der kombi, die hinten dran kommen sollen
                     an die Haupt- und Anzeigetabelle
                     key = haupttabellenzeilennummer
                g    value = kombitabellenzeilennummer
                """
                tables = {}
                for kombiLineNumber in value:
                    """
                    alle kombitabellenzeilennummern hier durchiterieren
                    pro haupttabellenzeilennummer (diese umschließende Schleife)

                    into = eine neue Tabelle mit nur erlaubten Zeilen, gemacht
                    aus der Tabelle von der kombi.csv, die schon mit Zeilenumbrüchen
                    usw. vorbereitet wurde.
                    """

                    into = self.table.tableReducedInLinesByTypeSet(
                        newTable_kombi_1, {kombiLineNumber}
                    )
                    """into = self.tables.tableReducedInLinesByTypeSet(
                        animalsProfessionsTable, {kombiLineNumber}
                    )"""
                    if len(into) > 0:
                        if key in tables:
                            """Ergibt Matrix:
                            KombigesamttabelleMitZeilenumbruchVorbereitung[kombi.csv Zeilenummer][nur die relevanten Spaltens ihre erste Spalte ]
                            d.h. das ist aus kombi.csv die erste Spalte mit den Kombinationszahlen
                            die hier zugeordnet zu den kombi.csv zeilennummern gespeichert werden,
                            d.h. nicht den haupt+ausgabezeilen
                            """
                            tables[key] += [into[0]]
                        else:
                            tables[key] = [into[0]]
                    # cliOut({0,kombiLineNumber}, oneTable, 2, rowsRange_kombi_1)
                    """ Liste aus Tabellen: eine Untertabelle = was in Haupttabellenzeilennummer rein soll aus der Kombitabelle
                    Zusammen ist das die Matrix der Kombis, die an die Haupt+Anzeige Tabelle deneben ran soll
                """
                KombiTables += [tables]
            return KombiTables

        def tableJoin(
            self,
            mainTable: list,
            manySubTables: list,
            maintable2subtable_Relation: list,
            old2newRows: list,
            rowsOfcombi,
        ) -> list:
            """Verbindet kombi tabelle mit haupttabelle
            @type mainTable: list
            @param mainTable: Haupttabelle, die angezeigt werden soll
            @type manySubTables: list
            @param manySubTables: Die Teiltabellen, von denen Teile pro Spalte in die Haupttabelle als Spalten und Zeilen rein sollen
            @type maintable2subtable_Relation: list
            @param maintable2subtable_Relation: Wie die Kombitabelle in die Haupttabelle rein kommen soll, d.h. hier sind die Verknüpfungspunkte beider Seiten enthalten
            @type old2newRows: list
            @param old2newRows: list
            @type rowsOfcombi: list
            @param rowsOfcombi: Welche Spalten der Kombitabelle in die Haupttabelle rein sollen
            @rtype table2: list[list]
            @return table2: Die resultierende gesamte später anzuzeigende Haupttabelle

            """
            rowsOfcombi = list(rowsOfcombi)
            rowsOfcombi.sort()
            table2 = mainTable
            """ Hätte ich mich gleich für SQL entschieden, oder hätte ich Pandas gewählt, dann hätte ich diesen Komplizierten Mist nicht programmieren müssen!
            """
            # if self.table.textWidth == 0 and type(self.table.getOut.outType) in [
            if type(self.table.getOut.outType) in [
                htmlSyntax,
                bbCodeSyntax,
            ]:
                oneLinePerLine = True
            else:
                oneLinePerLine = False
            for colNum, (reliNum, col) in enumerate(
                zip(self.religionNumbers, mainTable)
            ):
                """geht die Zeilen der anzuzeigenden Haupttabelle durch
                1. Zeilenummer, 2. richtige Nummer der Religion (z.B: 1-10), 3. anzuzeigende Haupttabellenzeile
                """
                for subTable in manySubTables:
                    """Liste aus Tabellen: eine Untertabelle = was in Haupttabellenzeilennummer rein soll aus der Kombitabelle
                    Zusammen ist das die Matrix der Kombis, die an die Haupt+Anzeige Tabelle deneben ran soll

                    hier werden also alle Orginal-Haupt+Anzeige Zeilen durchgegangen
                    """
                    if reliNum in subTable:
                        """Wenn z.B. Religion 2 als Spalte 2 auch als Spalte 2 drin ist als Zelle der kombis die als Zelle in die Haupt+Anzeige Tabelle rein soll
                        d.h. hier die Frage ob z.B. 2==2    viel mehr ist das nicht"""
                        for row, bigCell in enumerate(mainTable[colNum]):
                            """HauptTabellenzeilen werden durchIteriert"""
                            if old2newRows[1][row] in maintable2subtable_Relation[0]:
                                """Wenn Haupttabellenzeile der Kombitabellenzeile entspricht"""
                                subRowNum = maintable2subtable_Relation[0][
                                    old2newRows[1][row]
                                ]
                                for subTableCell in subTable[reliNum]:
                                    """Die zu wählenden Religionen z.B. 1-10 durchiterieren
                                    und dessen zugehörige subTableZellen die als Zellen in die Haupt+Anzeige Tabelle rein sollen
                                    genomen
                                    """
                                    if rowsOfcombi.index(subRowNum + 1) < len(
                                        subTableCell
                                    ) and subTableCell != [[""]]:
                                        """Hier kommt jetzt endlich die Zelle in die Zelle rein:
                                        D.h. die Sache aus der Kombitabelle kommt in die Zelle der Haupt+Anzeige-Tabelle rein.
                                        Dabei ist die Zelle in die die Zelle rein kommt, widerum selbst eine kleine Tabelle, eigentlich.
                                        """
                                        if oneLinePerLine:

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
                                                table2[colNum][row][
                                                    -1
                                                ] += " | " + deepcopy(
                                                    subTableCell[
                                                        rowsOfcombi.index(subRowNum + 1)
                                                    ][0]
                                                )
                                        else:
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
        ) -> dict:
            """Vorbereiten zum Kombinieren von Tabellen, wie bei einem SQL-Join
            siehe hier Return-Value, der hiermit erstellt wird.
            Nur darum geht es.

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
            @return: ZeilenNummern die miteinander als Join kombiniert werden sollen zwischen Haupttabelle und weiterer
                key = haupttabellenzeilennummer
                value = kombitabellenzeilennummer
            """
            # kombitypes = {"displaying": False, "or": False, "and": False}
            # self.ChosenKombiLines: dict = {}
            for condition in paramLines:
                if "ka" == condition:
                    # kombitypes["displaying"] = True
                    for MainLineNum in displayingMainLines:
                        for kombiLineNumber, kombiLine in enumerate(kombiTable_Kombis):
                            """kombiLineNumber ist die csv Zeilennummer in der Kombitabelle
                            kombiLine ist aus der ersten Spalte die jeweilige Liste an Zahlenkombinationen pro Zeile"""
                            for kombiNumber in kombiLine:
                                """kombiNumber ist demzufolge eine so eine Zahl
                                von n*m Zahlen
                                if: wenn eine dieser Zahlen zu denen gehört, die am Ende angezeigt werden sollen und
                                wenn diese Zahl eine ist, die genau der richtigen Anzeigezeile entspricht"""
                                if (
                                    kombiNumber in displayingMainLines
                                    and kombiNumber == MainLineNum
                                ):
                                    try:
                                        """Zugehörig zur richtigen Anzeigeezeile wird diese Kombizeile ausgewählt
                                        d.h. anzeige in zeile enthält die richtige kombizeile
                                        NUMMERN werden da rein gelistet
                                        key = haupttabellenzeilennummer
                                        value = kombitabellenzeilennummer
                                        """
                                        self.ChosenKombiLines[MainLineNum] |= {
                                            kombiLineNumber + 1
                                        }
                                    except KeyError:
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
            @param rowsAsNumbers: welche Spalten  der Anzeigetabelle sind gewählt
            @type rowsOfcombi: set
            @param rowsOfcombi: welche Spalten der kombi Tabelle dazu kommen sollen
            @rtype: tuple[list,list,list,list]
            @return: neue Tabelle - die der kombi.csv entspricht, haupttabelle self.relitable, \
                Liste mit allen Zeilen der neuen Tabelle aus der ersten Spalte je Liste aus allem darin \
                das mit Komma getrennt wurde , was zu was gehört als Info für den join später
            return kombiTable, self.relitable, kombiTable_Kombis, maintable2subtable_Relation
            """
            global folder
            self.rowsOfcombi = rowsOfcombi
            place = os.path.join(
                os.getcwd(), os.path.dirname(__file__), os.path.basename("./kombi.csv")
            )
            self.sumOfAllCombiRowsAmount += len(self.rowsOfcombi)
            self.relitable = relitable
            headingsAmount = len(self.relitable[0])
            self.maintable2subtable_Relation: tuple = ({}, {})
            if len(self.rowsOfcombi) > 0:
                with open(place, mode="r") as csv_file:
                    self.kombiTable: list = []
                    self.kombiTable_Kombis: list = []
                    for z, col in enumerate(csv.reader(csv_file, delimiter=";")):
                        """jede Zeile in der kombi.csv"""
                        for i, row in enumerate(col):
                            """jede Spalte also dann eigentlich Zelle der kombi.csv"""
                            if (
                                i > 0
                                and col[i].strip() != ""
                                and len(col[0].strip()) != 0
                            ):
                                col[i] += " (" + col[0] + ")"
                        self.kombiTable += [col]
                        self.kombiTable_Kombis_Col: list = []
                        if len(col) > 0 and z > 0:
                            """die Behandlung des Auslesens von Religionsnummern in Kombination
                            in der ersten Spalte der kombi.csv"""
                            for num in col[0].split("|"):
                                """self.kombiTable_Kombis:
                                Liste mit allen Zeilen der neuen Tabelle aus der ersten
                                Spalte je Liste aus allem darin das mit Komma getrennt wurde
                                """
                                if num.isdecimal() or (
                                    num[0] in ["+", "-"] and num[1:].isdecimal()
                                ):
                                    """Nummer ... Liste mit alles Zahlen einer Religionskombination
                                    in eine Zeile pro Religionskombination und nicht bereits hier
                                    mit was eine Religion mit anderen Zahlen kombiniert werden würde,
                                    denn das kommt später und wird genau daraus hier gebaut.
                                    """
                                    self.kombiTable_Kombis_Col += [abs(int(num))]
                                elif num[1:-1].isdecimal() or (
                                    num[1] in ["+", "-"] and num[2:-1].isdecimal()
                                ):
                                    self.kombiTable_Kombis_Col += [abs(int(num[1:-1]))]
                                    # arg[(arg.find("=") + 1) :].split(",")
                                elif (
                                    "/" in num and num[num.find("/") + 1 :].isdecimal()
                                ):
                                    self.kombiTable_Kombis_Col += [
                                        abs(int(num[num.find("/") + 1 :])),
                                        abs(int(num[: num.find("/")])),
                                    ]
                                elif (
                                    "/" in num
                                    and num[num.find("/") + 2 : -1].isdecimal()
                                ):
                                    self.kombiTable_Kombis_Col += [
                                        abs(int(num[num.find("/") + 2 : -1])),
                                        abs(int(num[1 : num.find("/")])),
                                    ]
                                else:
                                    raise BaseException(
                                        "Die kombi.csv ist in der ersten Spalte nicht so wie sie sein soll mit den Zahlen."
                                    )
                            self.kombiTable_Kombis += [self.kombiTable_Kombis_Col]
                    self.relitable, animalsProfessionsCol = Tables.fillBoth(
                        self.relitable, list(self.kombiTable)
                    )
                    lastlen = 0
                    maxlen = 0
                    for i, (animcol, relicol) in enumerate(
                        zip(animalsProfessionsCol, self.relitable)
                    ):
                        """jede Zeile bei der Haupttabellenzeile der Kombitabellenzeile (noch) NICHT richtig entspricht
                        beide sind auf die gleiche richtig Länge vorher verlängert worden.
                        (irgendwie komisch von mir programmiert)
                        """
                        if i == 0:
                            """Zur richtigen Zeile kommt der Leerraum rein,
                            der später aufgefüllt wird durch die wirklichen
                            Inhalte der kombi.csv
                            """
                            lastlen = len(animcol)
                            if lastlen > maxlen:
                                maxlen = lastlen
                            for t, ac in enumerate(animcol[1:]):
                                """Spalte hinten dran und nächste usw.
                                entspricht Spalte in Kombitabelle und umgehert
                                genauso, also Äquivalenz!
                                """
                                self.maintable2subtable_Relation[0][
                                    len(self.relitable[0]) + t
                                ] = t
                                self.maintable2subtable_Relation[1][t] = (
                                    len(self.relitable[0]) + t
                                )
                            self.relitable[0] += list(animcol[1:]) + [""] * (
                                maxlen - len(animcol)
                            )
                        else:
                            """Zur richtigen Zeile kommt der Leerraum rein,
                            der später aufgefüllt wird durch die wirklichen
                            Inhalte der kombi.csv
                            """
                            self.relitable[i] += len(animcol[1:]) * [""] + [""] * (
                                maxlen - len(animcol)
                            )
                        if i == 0:
                            for u, heading in enumerate(self.relitable[0]):
                                for a in self.rowsOfcombi:
                                    if (
                                        u >= headingsAmount
                                        and u == headingsAmount + a - 1
                                    ):
                                        rowsAsNumbers.add(int(u))
                                        """ rowsAsNumbers müsste hier verzeigert sein
                                        Es kommen genau diese Spaltennummern hinzu,
                                        (die überzählig sind) die nicht mehr in der
                                        anzuzeigenden tabelle entahlten sind also
                                        zu hoch wären, weil es die dazu kommenden
                                        Spalten der kombi.csv sind.
                                        """
            else:
                self.kombiTable = [[]]
                self.kombiTable_Kombis = [[]]
            # if len(self.kombiTable) > 0:
            #    self.rowsOfcombi = len(rowsAsNumbers) - 1
            # else:
            #    self.rowsOfcombi = 0
            return (
                self.kombiTable,
                self.relitable,
                self.kombiTable_Kombis,
                self.maintable2subtable_Relation,
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
            if rowsAsNumbers >= {64}:
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
            if rowsAsNumbers >= {64}:
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


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def primCreativity(num: int):
    if num == 0:
        return 0
    fak = primRepeat(primFak(num))
    if len(fak) == 1 and fak[0][1] == 1:
        return 1
    if len(fak) == 1:
        return 3
    if len(fak) < 1:
        return 0
    primAmounts = []
    for (prim, primAmount) in fak:
        primAmounts += [primAmount]
    for primAmount in primAmounts:
        divisors = set(divisorGenerator(primAmount)) - {1}
        if len(divisors) == 0:
            try:
                del schnittmenge
            except NameError:
                pass
            break
        try:
            schnittmenge &= divisors
        except NameError:
            schnittmenge = divisors
    try:
        if len(schnittmenge) != 0:
            return 3
        else:
            return 2
    except NameError:
        return 2
    return None


# def getLogarithmOnlyAsPureInt(potenz: int, basis: int) -> int:
#    exponent = math.log(potenz) / math.log(basis)
#    if exponent == round(exponent):
#        return exponent
#    else:
#        return None


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
