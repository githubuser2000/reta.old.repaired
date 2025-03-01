#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import math
import re
import sys
from collections import namedtuple
from copy import copy, deepcopy
from enum import Enum
# from collections.abc import Iterable
from typing import Iterable, Union

from center import (alxp, bbcode, cliout, html2text, infoLog, os, output,
                    shellRowsAmount)
from tableHandling import (OutputSyntax, Tables, alxp, bbCodeSyntax, csvSyntax,
                           htmlSyntax, markdownSyntax, primCreativity)

parser = bbcode.Parser()
parser.add_simple_formatter("hr", "<hr />", standalone=True)
parser.add_simple_formatter("sub", "<sub>%(value)s</sub>")
parser.add_simple_formatter("sup", "<sup>%(value)s</sup>")


def render_color(tag_name, value, options, parent, context):
    return '<span style="color:%s;">%s</span>' % (tag_name, value)


# print(os.path.dirname(__file__))
for color in ("red", "blue", "green", "yellow", "black", "white"):
    parser.add_formatter(color, render_color)


# puniverseprims = {
#     couldBePrimeNumber if primCreativity(couldBePrimeNumber) == 1 else None
#     for couldBePrimeNumber in range(2, 1025)
# } - {
#     None,
# }
#


class Program:
    def produceAllSpaltenNumbers(self, neg=""):
        def resultingSpaltenFromTuple(tupl: tuple, neg, paraValue=None) -> tuple:
            for i, eineSpaltenArtmitSpaltenNummern in enumerate(tupl):
                alxp("oo")
                alxp(i)
                if i == 2:
                    self.spaltenArtenKey_SpaltennummernValue[
                        (len(neg), 2)
                    ] |= eineSpaltenArtmitSpaltenNummern[0](paraValue)
                else:
                    self.spaltenArtenKey_SpaltennummernValue[
                        (len(neg), i)
                    ] |= eineSpaltenArtmitSpaltenNummern
            self.spaltenArtenKey_SpaltennummernValue

        def spalten_removeDoublesNthenRemoveOneFromAnother():
            for el2Type in range(
                int(len(self.spaltenArtenKey_SpaltennummernValue) / 2)
            ):
                self.spaltenArtenKey_SpaltennummernValue[(0, el2Type)] -= (
                    self.spaltenArtenKey_SpaltennummernValue[(0, el2Type)]
                    & self.spaltenArtenKey_SpaltennummernValue[(1, el2Type)]
                )
            for el2Type in range(
                int(len(self.spaltenArtenKey_SpaltennummernValue) / 2)
            ):
                self.spaltenArtenKey_SpaltennummernValue[
                    (0, el2Type)
                ] -= self.spaltenArtenKey_SpaltennummernValue[(1, el2Type)]
                self.spaltenArtenKey_SpaltennummernValue.pop((1, el2Type))

        def notNormalParameters(parameter, parametervalue, tables):
            if parameter == "bedeutung" and parametervalue in [
                "gestirn",
                "mond",
                "sonne",
                "planet",
            ]:
                tables.spalteGestirn = True

        # self.intoParameterDatatype
        mainParaCmds: dict = {"zeilen": 0, "spalten": 1, "kombination": 2, "ausgabe": 3}
        # mainParaCmds2: dict = {
        #    0: "zeilen",
        #    1: "spalten",
        #    2: "kombination",
        #    3: "ausgabe",
        # }
        lastMainCmd: int = -1
        # kombiSpalten = set()
        # ordinarySpalten = set()
        for cmd in self.argv[1:]:
            if cmd[0] == "-" and cmd[1] != "-":
                if cmd[1:] in mainParaCmds.keys():
                    lastMainCmd = mainParaCmds[cmd[1:]]
                else:
                    alxp(
                        'Der Haupt-Paramaeter -"'
                        + cmd
                        + '" existiert hier nich als Befehl!'
                    )
            elif cmd[:2] == "--":
                if lastMainCmd == mainParaCmds["spalten"]:
                    cmd = cmd[2:]
                    # alxp(cmd.find("="))
                    # alxp(cmd[cmd.find("=") + 1 :])
                    # alxp(cmd[: cmd.find("=") + 2])
                    eq = cmd.find("=")
                    if eq != -1:
                        for oneOfThingsAfterEqSign in cmd[eq + 1 :].split(","):
                            if (
                                len(oneOfThingsAfterEqSign) > 0
                                and oneOfThingsAfterEqSign[0] == "-"
                            ):
                                oneOfThingsAfterEqSign = oneOfThingsAfterEqSign[1:]
                                yes1 = True if neg == "-" else False
                            else:
                                yes1 = True if len(neg) == 0 else False
                            if yes1:
                                try:
                                    notNormalParameters(
                                        cmd[:eq],
                                        oneOfThingsAfterEqSign,
                                        self.tables,
                                    )
                                    alxp("uuuu")
                                    resultingSpaltenFromTuple(
                                        self.paraDict[
                                            (cmd[:eq], oneOfThingsAfterEqSign)
                                        ],
                                        neg,
                                        oneOfThingsAfterEqSign,
                                    )

                                    # alxp(cmd[:eq] + "=" + oneOfThingsAfterEqSign)
                                except KeyError:
                                    alxp(
                                        'Der Unter-Paramaeter "--'
                                        + cmd[:eq]
                                        + '" mit dem Textwert "'
                                        + oneOfThingsAfterEqSign
                                        + '" existiert hier nicht als Befehl für Haupt-Parameter'
                                        + " -spalten"
                                        + " !"
                                    )

                    else:
                        try:
                            if (cmd[-1] == "-" and neg == "-") != (
                                len(neg) == 0 and cmd[-1] != "-"
                            ):
                                if len(cmd) > 0 and cmd[-1] == "-":
                                    cmd = cmd[:-1]
                                # alxp(self.paraDict[(cmd, "")])
                                resultingSpaltenFromTuple(
                                    self.paraDict[(cmd, neg)], neg
                                )

                                # Nalxp("Befehl: " + cmd)
                        except KeyError:
                            alxp(
                                'Der Unter-Paramaeter "--'
                                + cmd
                                + '" existiert hier nich als Befehl für Haupt-Parameter'
                                + " -spalten"
                                + " !"
                            )

                elif lastMainCmd == mainParaCmds["kombination"]:
                    if cmd[:6] == "--was=":
                        for oneKombiSpalte in cmd[6:].split(","):
                            if len(oneKombiSpalte) > 0 and oneKombiSpalte[0] == "-":
                                oneKombiSpalte = oneKombiSpalte[1:]
                                yes1 = True if neg == "-" else False
                            else:
                                yes1 = True if len(neg) == 0 else False
                            if yes1:
                                try:
                                    resultingSpaltenFromTuple(
                                        (
                                            set(),
                                            set(),
                                            set(),
                                            {
                                                self.kombiReverseDict[oneKombiSpalte],
                                            },
                                        ),
                                        neg,
                                    )
                                    # kombiSpalten |= {self.kombiReverseDict[oneKombiSpalte]}
                                    pass
                                except KeyError:
                                    alxp(
                                        'Die Kombispalte "'
                                        + oneKombiSpalte
                                        + '" existiert so nicht als Befehl.'
                                    )

                    else:
                        alxp(
                            'kein Unter-Parameter "--was=" angegeben für Hauptparameter --kombination'
                        )
                else:
                    alxp(
                        "Es muss ein Hauptparameter, bzw. der richtige, gesetzt sein, damit ein"
                        + ' Nebenparameter, wie möglicherweise: "'
                        + cmd
                        + '" ausgeführt werden kann. Hauptparameter sind: -'
                        + " -".join(mainParaCmds)
                    )
        #                    self.spaltenArtenNameKey_SpaltenArtenTupleVal_4Key4otherDict
        # alxp(ordinarySpalten)
        alxp("einzeln")
        alxp(neg)
        alxp(self.spaltenArtenKey_SpaltennummernValue)
        if len(neg) == 0:
            self.produceAllSpaltenNumbers("-")
            alxp("zusammen")
            alxp(self.spaltenArtenKey_SpaltennummernValue)
            spalten_removeDoublesNthenRemoveOneFromAnother()
            alxp("zusammen2")
            alxp(self.spaltenArtenKey_SpaltennummernValue)

            # self.rowsOfcombi = self.spaltenArtenKey_SpaltennummernValue[
            #     self.spaltenTypeNaming.ordinary
            # ]
            # alxp("hier")
            # alxp(self.rowsOfcombi)

    def storeParamtersForColumns(self):
        # global puniverseprims

        def intoParameterDatatype(
            parameterMainNames: tuple, parameterNames: tuple, datas: tuple
        ) -> tuple:
            """Speichert einen Parameter mit seinem DatenSet
            in 2 Datenstrukturen (die beides kombinieren 2x2)
            Diese werden jedoch nur zurück gegeben und nicht in der Klasse gespeichert.
            @return: alle Hauptparamter| alle Nebenparamter zu nur einem
            Hauptparameter ergibt Mengen an Spalten | enthält alle Haup- und
            Nebenparameter keys sind Spalten der Tabelle
            """
            # alxp(("_", parameterMainNames, parameterNames, datas))
            paraMainDict = {}
            for name in parameterMainNames:
                paraMainDict[name] = parameterNames
            paraDict = {}
            for name1 in parameterMainNames:
                for name2 in parameterNames:
                    paraDict[(name1, name2)] = datas
                if len(parameterNames) == 0:
                    paraDict[(name1, "")] = datas
            dataDicts: tuple = ({}, {}, {})
            for i, d in enumerate(datas):
                for dd in d:
                    for parameterMainName in parameterMainNames:
                        for parameterName in parameterNames:
                            dataDicts[i][dd] = (
                                parameterMainName
                                if len(parameterMainNames) > 0
                                else (),
                                parameterName if len(parameterNames) > 0 else (),
                            )
            # alxp(paraMainDict)
            # alxp(paraDict)
            return paraMainDict, paraDict, dataDicts

        def mergeParameterDicts(
            paraMainDict1: dict,
            paraDict1: dict,
            dataDicts1: tuple,
            paraMainDict2: dict,
            paraDict2: dict,
            dataDicts2: tuple,
        ) -> tuple:
            """Merged die beiden 2x2 Datenstrukturen und speichert diese
            in die Klasse und gibt sie dennoch auch mit return zurück
            @param paraMainDict: Hauptparameter in der Kommandozeile
            hat als Werte die Nebenparameter und keys sind die Hauptparamter
            @param paraDict: Nebenparamteter in der Kommandozeile
            hat als Werte die Spaltennummern dazugehörig
            @param dataDicts: die beiden Parameter sagen welche Spaltennummern es
            sein werden
            @return: Spaltennummer sagt welche Parameter es ingesamt dazu sind | die
            beiden Parameter sagen, welche Spalten es alle sind."""
            # try:
            paraMainDict1 = {**paraMainDict1, **paraMainDict2}
            # except AttributeError:
            #    pass
            # try:
            paraDict1 = {**paraDict1, **paraDict2}
            # except AttributeError:
            #    self.paraDict = paraDict
            for i, dataDict_ in enumerate(dataDicts2):
                for k, v in dataDict_.items():
                    try:
                        dataDicts1[i][k] |= {v}
                    # except AttributeError or UnboundLocalError:
                    #    self.dataDict[i][k] = {v}
                    except KeyError:
                        dataDicts1[i][k] = {v}
            return paraDict1, dataDicts1

        Program.ParametersMain = (
            (
                "religionen",
                "religion",
            ),
            (
                "galaxie",
                "alteschriften",
                "kreis",
                "galaxien",
                "kreise",
            ),
            (
                "groessenordnung",
                "strukturgroesse",
                "groesse",
                "stufe",
            ),
            (
                "universum",
                "transzendentalien",
                "strukturalien",
            ),
            ("wirtschaft",),
            ("menschliches",),
            (
                "procontra",
                "dagegendafuer",
            ),
            ("licht",),
            ("bedeutung",),
            ("symbole",),
            ("primzahlvielfachesuniversum",),
            (
                "konzept",
                "konzepte",
            ),
            ("inkrementieren",),
            ("alles"),
        )
        paraNdataMatrix = (
            (
                Program.ParametersMain[0],
                (
                    "prophet",
                    "archon",
                    "religionsgründertyp",
                    "religionsgruendertyp",
                ),
                {72},
            ),
            (Program.ParametersMain[0], ("sternpolygon",), {0, 6, 36}),
            (
                Program.ParametersMain[0],
                (
                    "babylon",
                    "dertierkreiszeichen",
                ),
                {0, 36},
            ),
            (
                Program.ParametersMain[0],
                (
                    "messias",
                    "heptagramm",
                    "hund",
                    "messiase",
                    "messiasse",
                ),
                {7},
            ),
            (
                Program.ParametersMain[0],
                (
                    "gleichfoermigespolygon",
                    "gleichförmigespolygon",
                    "nichtsternpolygon",
                    "polygon",
                ),
                {16, 37},
            ),
            (
                Program.ParametersMain[0],
                (
                    "vertreterhoehererkonzepte",
                    "galaxien",
                    "galaxie",
                    "schwarzesonne",
                    "schwarzesonnen",
                    "universum",
                    "universen",
                    "kreis",
                    "kreise",
                    "kugel",
                    "kugeln",
                ),
                {24},
            ),
            (
                Program.ParametersMain[1],
                (
                    "babylon",
                    "tierkreiszeichen",
                ),
                {1, 2},
            ),
            (
                Program.ParametersMain[1],
                (
                    "thomas",
                    "thomasevangelium",
                ),
                {0, 3},
            ),
            (Program.ParametersMain[2], (), {4, 21}),
            (
                Program.ParametersMain[3],
                (
                    "transzendentalien",
                    "transzendentalie",
                    "strukturalien",
                    "alien",
                    "existenzialien",
                    "universalien",
                ),
                {5, 54, 55},
            ),
            (
                Program.ParametersMain[3],
                (
                    "komplex",
                    "komplexität",
                    "komplexitaet",
                    "complexity",
                    "model",
                    "abstraktion",
                ),
                {65, 75, 77},
            ),
            (
                Program.ParametersMain[3],
                (
                    "2",
                    "zwei",
                    "gerade",
                    "ungerade",
                    "alternierung",
                    "alternierend",
                    "zweierstruktur",
                ),
                {78, 79, 80},
            ),
            (
                Program.ParametersMain[3],
                ("4", "vier", "viererstruktur", "viererabfolgen"),
                {76, 77, 81},
            ),
            (
                Program.ParametersMain[3],
                (),
                {5, 54, 55, 65, 75, 76, 77, 78, 79, 80, 81},
            ),
            (
                Program.ParametersMain[4],
                ("system",),
                {
                    69,
                },
            ),
            (
                Program.ParametersMain[4],
                (
                    "realistisch",
                    "funktioniert",
                ),
                {70},
            ),
            (
                Program.ParametersMain[4],
                (
                    "erklärung",
                    "erklaerung",
                ),
                {71},
            ),
            (
                Program.ParametersMain[5],
                (
                    "incel",
                    "incels",
                ),
                {68},
            ),
            (
                Program.ParametersMain[5],
                (
                    "irrationalezahlendurchwurzelbildung",
                    "ausgangslage",
                ),
                {73},
            ),
            (
                Program.ParametersMain[5],
                (
                    "dominierendesgeschlecht",
                    "maennlich",
                    "männlich",
                    "weiblich",
                ),
                {51},
            ),
            (
                Program.ParametersMain[5],
                (
                    "liebe",
                    "ethik",
                ),
                {8, 9, 28},
            ),
            (
                Program.ParametersMain[5],
                (
                    "glauben",
                    "erkenntnis",
                    "glaube",
                ),
                {59},
            ),
            (
                Program.ParametersMain[5],
                (
                    "angreifbar",
                    "angreifbarkeit",
                ),
                {58, 57},
            ),
            (
                Program.ParametersMain[5],
                (
                    "motive",
                    "motivation",
                    "motiv",
                ),
                {10, 18, 42},
            ),
            (
                Program.ParametersMain[5],
                (
                    "errungenschaften",
                    "ziele",
                    "erhalten",
                ),
                {11},
            ),
            (
                Program.ParametersMain[5],
                (
                    "erwerben",
                    "erlernen",
                    "lernen",
                    "evolutionaer",
                    "evolutionär",
                    "intelligenz",
                    "kreativität",
                    "kreativitaet",
                    "kreativ",
                ),
                {12, 47, 27, 13, 32},
            ),
            (
                Program.ParametersMain[5],
                (
                    "brauchen",
                    "benoetigen",
                    "benötigen",
                    "notwendig",
                ),
                {13, 14},
            ),
            (
                Program.ParametersMain[5],
                (
                    "krankheit",
                    "krankheiten",
                    "pathologisch",
                    "pathologie",
                    "psychiatrisch",
                ),
                {24},
            ),
            (
                Program.ParametersMain[5],
                (
                    "alpha",
                    "beta",
                    "omega",
                    "sigma",
                ),
                {46},
            ),
            (
                Program.ParametersMain[5],
                (
                    "anfuehrer",
                    "chef",
                ),
                {29},
            ),
            (
                Program.ParametersMain[5],
                (
                    "beruf",
                    "berufe",
                ),
                {30},
            ),
            (
                Program.ParametersMain[5],
                (
                    "loesungen",
                    "loesung",
                    "lösungen",
                    "lösungen",
                ),
                {31},
            ),
            (Program.ParametersMain[5], ("musik",), {33}),
            (
                Program.ParametersMain[6],
                (
                    "pro",
                    "dafür",
                    "dafuer",
                ),
                {17, 48},
            ),
            (
                Program.ParametersMain[6],
                (
                    "contra",
                    "dagegen",
                ),
                {15, 26},
            ),
            (Program.ParametersMain[7], (), {20, 27}),
            (
                Program.ParametersMain[8],
                (
                    "primzahlen",
                    "vielfache",
                    "vielfacher",
                ),
                {19},
            ),
            (
                Program.ParametersMain[8],
                (
                    "anwendungdersonnen",
                    "anwendungenfuermonde",
                ),
                {22},
            ),
            (
                Program.ParametersMain[8],
                (
                    "zaehlung",
                    "zaehlungen",
                    "zählungen",
                    "zählung",
                ),
                {25, 45},
            ),
            (
                Program.ParametersMain[8],
                (
                    "jura",
                    "gesetzeslehre",
                    "recht",
                ),
                {34},
            ),
            (
                Program.ParametersMain[8],
                (
                    "vollkommenheit",
                    "geist",
                ),
                {35},
            ),
            (
                Program.ParametersMain[8],
                (
                    "gestirn",
                    "mond",
                    "sonne",
                    "planet",
                ),
                {64},
            ),
            (Program.ParametersMain[9], (), {36, 37}),
            (
                Program.ParametersMain[10],
                str(
                    set(
                        (
                            num if primCreativity(num) == 1 else None
                            for num in range(2, 24)
                        )
                    )
                    - {None}
                ),
                set(),
                set(),
                (
                    lambda paraValues: {
                        abs(int(chosen))
                        if chosen.isdecimal() and primCreativity(abs(int(chosen))) == 1
                        else None
                        for chosen in [value for value in (paraValues.split(","))]
                    }
                    - {None, 0, 1},
                ),
            ),
            (
                Program.ParametersMain[11],
                (
                    "weisheit",
                    "metaweisheit",
                    "meta-weisheit",
                    "idiot",
                    "weise",
                    "optimal",
                    "optimum",
                ),
                set(),
                {(40, 41)},
            ),
            (
                Program.ParametersMain[11],
                (
                    "gut",
                    "böse",
                    "boese",
                    "lieb",
                    "schlecht",
                ),
                {52, 53},
                {(38, 39)},
            ),
            (
                Program.ParametersMain[11],
                (
                    "zeit",
                    "raum",
                    "zeitlich",
                    "räumlich",
                ),
                set(),
                {(49, 50)},
            ),
            (
                Program.ParametersMain[11],
                (
                    "meinungen",
                    "anderemenschen",
                    "ruf",
                ),
                set(),
                {(60, 61)},
            ),
            (
                Program.ParametersMain[11],
                (
                    "selbstgerechtigkeit",
                    "selbstgerecht",
                ),
                set(),
                {(62, 63)},
            ),
            (
                Program.ParametersMain[11],
                (
                    "egoismus",
                    "altruismus",
                    "egoist",
                    "altruist",
                ),
                set(),
                {(66, 67)},
            ),
            (Program.ParametersMain[12], ("universum",), {43, 54, 74}),
            (
                Program.ParametersMain[13],
                (),
                set(range(82))
                - {67, 66, 63, 62, 61, 60, 56, 44, 49, 50, 41, 40, 39, 38},
                {
                    (40, 41),
                    (38, 39),
                    (49, 50),
                    (60, 61),
                    (62, 63),
                    (66, 67),
                },
                {
                    couldBePrimeNumber
                    if primCreativity(couldBePrimeNumber) == 1
                    else None
                    for couldBePrimeNumber in range(2, 100)
                }
                - {
                    None,
                },
                set(range(10)),
            ),
        )
        # return paraDict1, dataDict1
        self.paraMainDict, self.paraDict = {}, {}
        for parameterEntry in paraNdataMatrix:
            self.paraDict, self.dataDict = mergeParameterDicts(
                self.paraMainDict,
                self.paraDict,
                self.dataDict,
                *intoParameterDatatype(
                    parameterEntry[0],
                    parameterEntry[1],
                    tuple(
                        parameterEntryElement
                        for parameterEntryElement in parameterEntry[2:]
                    ),
                )
            )
        Program.kombiParaNdataMatrix = {
            1: (
                "tiere",
                "tier",
                "lebewesen",
            ),
            2: ("berufe", "beruf"),
            3: (
                "kreativität",
                "intelligenz",
                "kreativitaet",
            ),
            4: ("liebe",),
            5: (
                "transzendenz",
                "transzendentalien",
                "strukturalien",
                "alien",
            ),
            6: ("leibnitz", "primzahlkreuz"),
            7: (
                "männer",
                "maenner",
                "frauen",
            ),
            8: (
                "evolution",
                "erwerben",
                "persoenlichkeit",
                "persönlichkeit",
            ),
            9: (
                "religion",
                "religionen",
            ),
        }
        self.kombiReverseDict: dict = {}
        for key, value in Program.kombiParaNdataMatrix.items():
            for valuesInValuess in value:
                self.kombiReverseDict[valuesInValuess] = key

        # storeParamtersForColumns(
        # alxp((self.paraMainDict))
        # alxp((self.paraDict))
        # alxp((self.dataDict))

    def parametersToCommandsAndNumbers(
        self, argv, neg=""
    ) -> Iterable[Union[set, set, set, list]]:
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
        global infoLog, shellRowsAmount  # , puniverseprims
        if len(argv) == 1 and neg == "":
            cliout("Versuche Parameter -h")
        spaltenreihenfolgeundnurdiese: list = []
        puniverseprims_only: set = set()
        rowsAsNumbers: set = set()
        paramLines: set = set()
        self.bigParamaeter: list = []
        self.__willBeOverwritten_rowsOfcombi: set = set()
        generRows = set()
        for arg in argv[1:]:
            if len(arg) > 0 and arg[0] == "-":
                #                if (
                #                    len(arg) > 1
                #                    and arg[1] == "-"
                #                    and len(self.bigParamaeter) > 0
                #                    and self.bigParamaeter[-1] == "spalten"
                #                ):  # unteres Kommando
                #                    if arg[2:] == "alles" + neg:
                #                        self.allesParameters += 1
                #                        paramLines.add("ka")
                #
                #                        # puniverseprims = {
                #                        #    couldBePrimeNumber
                #                        #    if primCreativity(couldBePrimeNumber) == 1
                #                        #    else None
                #                        #    for couldBePrimeNumber in range(2, 100)
                #                        # } - {
                #                        #    None,
                #                        # }
                #                        self.tables.spalteGestirn = True
                #                        if len(neg) > 0:
                #                            self.tables.spalteGestirn = False
                #                        self.__willBeOverwritten_rowsOfcombi = set(range(10))
                #                        generRows |= {
                #                            (40, 41),
                #                            (38, 39),
                #                            (49, 50),
                #                            (60, 61),
                #                            (62, 63),
                #                            (66, 67),
                #                        }
                #                        rowsAsNumbers |= set(range(82)) - {
                #                            67,
                #                            66,
                #                            63,
                #                            62,
                #                            61,
                #                            60,
                #                            56,
                #                            44,
                #                            49,
                #                            50,
                #                            41,
                #                            40,
                #                            39,
                #                            38,
                #                        }
                #                    elif arg[2:9] == "breite=":
                #                        if arg[9:].isdecimal():
                #                            breite = abs(int(arg[9:]))
                #                            if breite == 0:
                #                                shellRowsAmount = 0
                #                            self.tables.textWidth = breite
                #                    elif arg[2:10] == "breiten=":
                #                        self.tables.breitenn = []
                #                        for breite in arg[10:].split(","):
                #                            if breite.isdecimal():
                #                                self.tables.breitenn += [int(breite)]
                #                    elif arg[2:20] == "keinenummerierung":
                #                        self.tables.nummeriere = False
                #                    elif arg[2:13] == "religionen=" or arg[2:11] == "religion=":
                #                        for religion in (
                #                            arg[13:].split(",")
                #                            if arg[2:13] == "religionen="
                #                            else arg[11:].split(",")
                #                        ):
                #                            if religion == neg + "sternpolygon":
                #                                rowsAsNumbers |= {0, 6, 36}
                #                            elif religion in [
                #                                neg + "prophet",
                #                                neg + "archon",
                #                                neg + "religionsgründertyp",
                #                                neg + "religionsgruendertyp",
                #                            ]:
                #                                rowsAsNumbers |= {72}
                #                            elif religion in [
                #                                neg + "babylon",
                #                                neg + "dertierkreiszeichen",
                #                            ]:
                #                                rowsAsNumbers |= {0, 36}
                #                            elif religion in [
                #                                neg + "messias",
                #                                neg + "heptagramm",
                #                                neg + "hund",
                #                                neg + "messiase",
                #                                neg + "messiasse",
                #                            ]:
                #                                rowsAsNumbers |= {7}
                #                            elif religion in [
                #                                neg + "gleichfoermigespolygon",
                #                                neg + "gleichförmigespolygon",
                #                                neg + "nichtsternpolygon",
                #                                neg + "polygon",
                #                            ]:
                #                                rowsAsNumbers |= {16, 37}
                #                            elif religion in [
                #                                neg + "vertreterhoehererkonzepte",
                #                                neg + "galaxien",
                #                                neg + "galaxie",
                #                                neg + "schwarzesonne",
                #                                neg + "schwarzesonnen",
                #                                neg + "universum",
                #                                neg + "universen",
                #                                neg + "kreis",
                #                                neg + "kreise",
                #                                neg + "kugel",
                #                                neg + "kugeln",
                #                            ]:
                #                                rowsAsNumbers.add(23)
                #                    elif (
                #                        arg[2:10] == "galaxie="
                #                        or arg[2:16] == "alteschriften="
                #                        or arg[2:8] == "kreis="
                #                        or arg[2:11] == "galaxien="
                #                        or arg[2:9] == "kreise="
                #                    ):
                #                        for thing in arg[(arg.find("=") + 1) :].split(","):
                #                            if thing in [neg + "babylon", neg + "tierkreiszeichen"]:
                #                                rowsAsNumbers |= {1, 2}
                #                            elif thing in [neg + "thomas", neg + "thomasevangelium"]:
                #                                rowsAsNumbers |= {0, 3}
                #                    elif arg[2:] in [
                #                        "groessenordnung" + neg,
                #                        "strukturgroesse" + neg,
                #                        "groesse" + neg,
                #                        "stufe" + neg,
                #                    ]:
                #                        rowsAsNumbers |= {4, 21}
                #                    elif arg[2:] in [
                #                        "universum" + neg,
                #                        "transzendentalien" + neg,
                #                        "strukturalien" + neg,
                #                    ]:
                #                        rowsAsNumbers |= {5, 54, 55, 65, 75, 76, 77, 78, 79, 80, 81}
                #                    elif arg[2:13] in ["wirtschaft="]:
                #                        for thing in arg[(arg.find("=") + 1) :].split(","):
                #                            if thing in [
                #                                neg + "system",
                #                            ]:
                #                                rowsAsNumbers |= {69}
                #                            if thing in [
                #                                neg + "realistisch",
                #                                neg + "funktioniert",
                #                            ]:
                #                                rowsAsNumbers |= {70}
                #                            if thing in [
                #                                neg + "erklärung",
                #                                neg + "erklaerung",
                #                            ]:
                #                                rowsAsNumbers |= {71}
                #                    elif arg[2:15] in ["menschliches="]:
                #                        for thing in arg[(arg.find("=") + 1) :].split(","):
                #                            if thing in [
                #                                neg + "incel",
                #                                neg + "incels",
                #                            ]:
                #                                rowsAsNumbers |= {68}
                #                            if thing in [
                #                                neg + "irrationalezahlendurchwurzelbildung",
                #                                neg + "ausgangslage",
                #                            ]:
                #                                rowsAsNumbers |= {73}
                #                            if thing in [
                #                                neg + "dominierendesgeschlecht",
                #                                neg + "maennlich",
                #                                neg + "männlich",
                #                                neg + "weiblich",
                #                            ]:
                #                                rowsAsNumbers |= {51}
                #                            if thing in [neg + "liebe", neg + "ethik"]:
                #                                rowsAsNumbers |= {8, 9, 28}
                #                            if thing in [
                #                                neg + "glauben",
                #                                neg + "erkenntnis",
                #                                neg + "glaube",
                #                            ]:
                #                                rowsAsNumbers |= {59}
                #                            elif thing in [
                #                                neg + "angreifbar",
                #                                neg + "angreifbarkeit",
                #                            ]:
                #                                rowsAsNumbers |= {58, 57}
                #                            elif thing in [
                #                                neg + "motive",
                #                                neg + "motivation",
                #                                neg + "motiv",
                #                            ]:
                #                                rowsAsNumbers |= {10, 18, 42}
                #                            elif thing in [
                #                                neg + "errungenschaften",
                #                                neg + "ziele",
                #                                neg + "erhalten",
                #                            ]:
                #                                rowsAsNumbers.add(11)
                #                            elif thing in [
                #                                neg + "erwerben",
                #                                neg + "erlernen",
                #                                neg + "lernen",
                #                                neg + "evolutionaer",
                #                                neg + "evolutionär",
                #                                neg + "intelligenz",
                #                                neg + "kreativität",
                #                                neg + "kreativitaet",
                #                                neg + "kreativ",
                #                            ]:
                #                                rowsAsNumbers |= {12, 47, 27, 13, 32}
                #                            elif thing in [
                #                                neg + "brauchen",
                #                                neg + "benoetigen",
                #                                neg + "benötigen",
                #                                neg + "notwendig",
                #                            ]:
                #                                rowsAsNumbers |= {13, 14}
                #                            elif thing in [
                #                                neg + "krankheit",
                #                                neg + "krankheiten",
                #                                neg + "pathologisch",
                #                                neg + "pathologie",
                #                                neg + "psychiatrisch",
                #                            ]:
                #                                rowsAsNumbers.add(24)
                #                            elif thing in [
                #                                neg + "alpha",
                #                                neg + "beta",
                #                                neg + "omega",
                #                                neg + "sigma",
                #                            ]:
                #                                rowsAsNumbers.add(46)
                #                            elif thing in [neg + "anfuehrer", neg + "chef"]:
                #                                rowsAsNumbers.add(29)
                #                            elif thing in [neg + "beruf", neg + "berufe"]:
                #                                rowsAsNumbers.add(30)
                #                            elif thing in [
                #                                neg + "loesungen",
                #                                neg + "loesung",
                #                                neg + "lösungen",
                #                                neg + "lösungen",
                #                            ]:
                #                                rowsAsNumbers.add(31)
                #                            elif thing in [neg + "musik"]:
                #                                rowsAsNumbers.add(33)
                #                    elif arg[2:12] == "procontra=" or arg[2:16] == "dagegendafuer=":
                #                        for thing in arg[(arg.find("=") + 1) :].split(","):
                #                            if thing in [neg + "pro", neg + "dafeuer"]:
                #                                rowsAsNumbers |= {17, 48}
                #                            elif thing in [neg + "contra", neg + "dagegen"]:
                #                                rowsAsNumbers |= {15, 26}
                #                    elif arg[2 : 7 + len(neg)] == "licht" + neg:
                #                        rowsAsNumbers |= {20, 27}
                #                    elif arg[2:12] == "bedeutung=":
                #                        for thing in arg[(arg.find("=") + 1) :].split(","):
                #                            if thing in [
                #                                neg + "primzahlen",
                #                                neg + "vielfache",
                #                                neg + "vielfacher",
                #                            ]:
                #                                rowsAsNumbers.add(19)
                #                            elif thing in [
                #                                neg + "anwendungdersonnen",
                #                                neg + "anwendungenfuermonde",
                #                            ]:
                #                                rowsAsNumbers.add(22)
                #                            elif thing in [
                #                                neg + "zaehlung",
                #                                neg + "zaehlungen",
                #                                neg + "zählungen",
                #                                neg + "zählung",
                #                            ]:
                #                                rowsAsNumbers |= {25, 45}
                #                            elif thing in [
                #                                neg + "jura",
                #                                neg + "gesetzeslehre",
                #                                neg + "recht",
                #                            ]:
                #                                rowsAsNumbers.add(34)
                #                            elif thing in [neg + "vollkommenheit", neg + "geist"]:
                #                                rowsAsNumbers.add(35)
                #                            elif thing in [
                #                                neg + "gestirn",
                #                                neg + "mond",
                #                                neg + "sonne",
                #                                neg + "planet",
                #                            ]:
                #                                # self.tables.spalteGestirn = True
                #                                rowsAsNumbers |= {64}
                #                    elif arg[2 : 11 + len(neg)] == "symbole" + neg:
                #                        rowsAsNumbers |= {36, 37}
                #                    elif arg[2:30] == "primzahlvielfachesuniversum=":
                #                        # int(value) if (len(neg) == 0) == (value > 1) and value not in (0,1,2) else None
                #                        puniverseprims_only |= {
                #                            abs(chosen)
                #                            if (len(neg) == 0) == (abs(chosen) == chosen)
                #                            else None
                #                            for chosen in [
                #                                int(value) for value in (arg[30:].split(","))
                #                            ]
                #                        } - {None, 0, 1}
                #                        # self.tables.primUniversePrimsSet.add(int(2))
                #                    elif arg[2:10] == "konzept=" or arg[2:11] == "konzepte=":
                #                        for word in (
                #                            arg[10:].split(",")
                #                            if arg[2:10] == "konzept="
                #                            else arg[11:].split(",")
                #                        ):
                #                            if word in [
                #                                neg + "weisheit",
                #                                neg + "metaweisheit",
                #                                neg + "meta-weisheit",
                #                                neg + "idiot",
                #                                neg + "weise",
                #                                neg + "optimal",
                #                                neg + "optimum",
                #                            ]:
                #                                generRows |= {(40, 41)}
                #                            elif word in [
                #                                neg + "gut",
                #                                neg + "böse",
                #                                neg + "lieb",
                #                                neg + "schlecht",
                #                            ]:
                #                                generRows |= {(38, 39)}
                #                                rowsAsNumbers |= {52, 53}
                #                            elif word in [
                #                                neg + "zeit",
                #                                neg + "raum",
                #                                neg + "zeitlich",
                #                                neg + "räumlich",
                #                            ]:
                #                                generRows |= {(49, 50)}
                #                            elif word in [
                #                                neg + "meinungen",
                #                                neg + "anderemenschen",
                #                                neg + "ruf",
                #                            ]:
                #                                generRows |= {(60, 61)}
                #                            elif word in [
                #                                neg + "selbstgerechtigkeit",
                #                                neg + "selbstgerecht",
                #                            ]:
                #                                generRows |= {(62, 63)}
                #                            elif word in [
                #                                neg + "egoismus",
                #                                neg + "altruismus",
                #                                neg + "egoist",
                #                                neg + "altruist",
                #                            ]:
                #                                generRows |= {(66, 67)}
                #                    elif arg[2:17] == "inkrementieren=":
                #                        for word in arg[17:].split(","):
                #                            if word in [
                #                                neg + "universum",
                #                            ]:
                #                                rowsAsNumbers |= {43, 54, 74}
                #
                if (
                    len(arg) > 1
                    and arg[1] == "-"
                    and len(self.bigParamaeter) > 0
                    and self.bigParamaeter[-1] == "zeilen"
                ):  # unteres Kommando
                    if arg[2:7] == "alles" and len(neg) == 0:
                        paramLines.add("all")
                    elif arg[2:7] == "zeit=":
                        for subpara in arg[7:].split(","):
                            if neg + "=" == subpara:
                                paramLines.add("=")
                            elif neg + "<" == subpara:
                                paramLines.add("<")
                            elif neg + ">" == subpara:
                                paramLines.add(">")
                    elif arg[2:11] == "zaehlung=":
                        paramLines |= (
                            self.tables.getPrepare.parametersCmdWithSomeBereich(
                                arg[11:], "n", neg
                            )
                        )
                        # for word in arg[11:].split(","):
                        #    if (
                        #        word.isdecimal()
                        #        or (word[1:].isdecimal() and word[0] == neg)
                        #    ) and (
                        #        (int(word) > 0 and neg == "")
                        #        or (int(word) < 0 and neg != "")
                        #    ):
                        #        paramLines.add(str(abs(int(word))) + "z")
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
                    elif arg[2 : 2 + len("potenzenvonzahlen=")] == "potenzenvonzahlen=":
                        for word in arg[2 + len("potenzenvonzahlen=") :].split(","):
                            if (
                                word.isdecimal()
                                or (word[1:].isdecimal() and word[0] == neg)
                            ) and (
                                (int(word) > 0 and neg == "")
                                or (int(word) < 0 and neg != "")
                            ):
                                paramLines.add(str(abs(int(word))) + "^")
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
                        paramLines |= (
                            self.tables.getPrepare.parametersCmdWithSomeBereich(
                                arg[22:], "a", neg
                            )
                        )
                    elif arg[2:21] == "nachtraeglichdavon=":
                        paramLines |= (
                            self.tables.getPrepare.parametersCmdWithSomeBereich(
                                arg[21:], "z", neg
                            )
                        )
                #                elif (
                #                    len(arg) > 1
                #                    and arg[1] == "-"
                #                    and len(self.bigParamaeter) > 0
                #                    and self.bigParamaeter[-1] == "kombination"
                #                ):  # unteres Kommando
                #                    """if arg[2:6] == "und=":
                #                        for word in arg[6:].split(","):
                #                            if (
                #                                word.isdecimal()
                #                                or (word[1:].isdecimal() and word[0] == neg)
                #                            ) and (
                #                                (int(word) > 0 and neg == "")
                #                                or (int(word) < 0 and neg != "")
                #                            ):
                #                                paramLines.add(str(abs(int(word))) + "ku")
                #                    elif arg[2:7] == "oder=":
                #                        for word in arg[7:].split(","):
                #                            if (
                #                                word.isdecimal()
                #                                or (word[1:].isdecimal() and word[0] == neg)
                #                            ) and (
                #                                (int(word) > 0 and neg == "")
                #                                or (int(word) < 0 and neg != "")
                #                            ):
                #                                paramLines.add(str(abs(int(word))) + "ko")
                #                    elif arg[2:] == "vonangezeigten" + neg:
                #                        paramLines.add("ka")"""
                #                    if arg[2:6] == "was=":
                #                        if neg == "":
                #                            paramLines.add("ka")
                #                        for thing in arg[(arg.find("=") + 1) :].split(","):
                #                            if thing in [
                #                                neg + "tiere",
                #                                neg + "tier",
                #                                neg + "lebewesen",
                #                            ]:
                #                                self.__willBeOverwritten_rowsOfcombi |= {1}
                #                            elif thing in [neg + "berufe", neg + "beruf"]:
                #                                self.__willBeOverwritten_rowsOfcombi |= {2}
                #                            elif thing in [
                #                                neg + "kreativität",
                #                                neg + "intelligenz",
                #                                neg + "kreativitaet",
                #                            ]:
                #                                self.__willBeOverwritten_rowsOfcombi |= {3}
                #                            elif thing in [neg + "liebe"]:
                #                                self.__willBeOverwritten_rowsOfcombi |= {4}
                #                            elif thing in [
                #                                neg + "transzendenz",
                #                                neg + "transzendentalien",
                #                                neg + "strukturalien",
                #                                neg + "alien",
                #                            ]:
                #                                self.__willBeOverwritten_rowsOfcombi |= {5}
                #                            elif thing in [
                #                                neg + "leibnitz",
                #                                neg + "primzahlkreuz",
                #                            ]:
                #                                self.__willBeOverwritten_rowsOfcombi |= {6}
                #                            elif thing in [
                #                                neg + "männer",
                #                                neg + "maenner",
                #                                neg + "frauen",
                #                            ]:
                #                                self.__willBeOverwritten_rowsOfcombi |= {7}
                #                            elif thing in [
                #                                neg + "evolution",
                #                                neg + "erwerben",
                #                                neg + "persoenlichkeit",
                #                                neg + "persönlichkeit",
                #                            ]:
                #                                self.__willBeOverwritten_rowsOfcombi |= {8}
                #                            elif thing in [
                #                                neg + "religion",
                #                                neg + "religionen",
                #                            ]:
                #                                self.__willBeOverwritten_rowsOfcombi |= {9}
                elif (
                    len(arg) > 1
                    and arg[1] == "-"
                    and len(self.bigParamaeter) > 0
                    and self.bigParamaeter[-1] == "ausgabe"
                ):  # unteres Kommando
                    if (
                        arg[2 : 2 + len("spaltenreihenfolgeundnurdiese=")]
                        == "spaltenreihenfolgeundnurdiese="
                    ):
                        for number in arg[
                            2 + len("spaltenreihenfolgeundnurdiese=") :
                        ].split(","):
                            if str(number).isdecimal():
                                spaltenreihenfolgeundnurdiese += [int(number)]
                    if arg[2:6] == "art=":
                        outputtype = arg[(arg.find("=") + 1) :]
                        if outputtype == "shell":
                            self.tables.outType = OutputSyntax()
                        elif outputtype == "csv":
                            self.tables.outType = csvSyntax()
                        elif outputtype == "bbcode":
                            self.tables.outType = bbCodeSyntax()
                        elif outputtype == "html":
                            self.tables.outType = htmlSyntax()
                        elif outputtype == "markdown":
                            self.tables.outType = markdownSyntax()
                    elif arg[2:] in ["nocolor", "justtext"] and neg == "":
                        self.tables.getOut.color = False
                    elif (
                        arg[2:] in ["endlessscreen", "endless", "dontwrap", "onetable"]
                        and neg == ""
                    ):
                        self.tables.getOut.oneTable = True
                else:  # oberes Kommando
                    if arg[1:] in ["zeilen", "spalten", "kombination", "ausgabe"]:
                        self.bigParamaeter += [arg[1:]]
                    elif arg[1:] in ["debug"]:
                        infoLog = True
                    elif arg[1:] in ["h", "help"] and neg == "":
                        self.helpPage()
        if not self.tables.getOut.oneTable:
            self.tables.textWidth = (
                self.tables.textWidth
                if shellRowsAmount > self.tables.textWidth + 7 or shellRowsAmount <= 0
                else shellRowsAmount - 7
            )
        return (
            paramLines,
            rowsAsNumbers,
            self.__willBeOverwritten_rowsOfcombi,
            spaltenreihenfolgeundnurdiese,
            puniverseprims_only,
            generRows,
        )

    def parameters(self, argv, neg="") -> Iterable[Union[set, set, set, list]]:
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
        global infoLog, shellRowsAmount  # , puniverseprims
        if len(argv) == 1 and neg == "":
            cliout("Versuche Parameter -h")
        spaltenreihenfolgeundnurdiese: list = []
        puniverseprims_only: set = set()
        rowsAsNumbers: set = set()
        paramLines: set = set()
        self.bigParamaeter: list = []
        self.__willBeOverwritten_rowsOfcombi: set = set()
        generRows = set()
        for arg in argv[1:]:
            if len(arg) > 0 and arg[0] == "-":
                if (
                    len(arg) > 1
                    and arg[1] == "-"
                    and len(self.bigParamaeter) > 0
                    and self.bigParamaeter[-1] == "spalten"
                ):  # unteres Kommando
                    if arg[2:] == "alles" + neg:
                        self.allesParameters += 1
                        paramLines.add("ka")

                        # puniverseprims = {
                        #    couldBePrimeNumber
                        #    if primCreativity(couldBePrimeNumber) == 1
                        #    else None
                        #    for couldBePrimeNumber in range(2, 100)
                        # } - {
                        #    None,
                        # }
                        self.tables.spalteGestirn = True
                        if len(neg) > 0:
                            self.tables.spalteGestirn = False
                        self.__willBeOverwritten_rowsOfcombi = set(range(10))
                        generRows |= {
                            (40, 41),
                            (38, 39),
                            (49, 50),
                            (60, 61),
                            (62, 63),
                            (66, 67),
                        }
                        rowsAsNumbers |= set(range(82)) - {
                            67,
                            66,
                            63,
                            62,
                            61,
                            60,
                            56,
                            44,
                            49,
                            50,
                            41,
                            40,
                            39,
                            38,
                        }
                    elif arg[2:9] == "breite=":
                        if arg[9:].isdecimal():
                            breite = abs(int(arg[9:]))
                            if breite == 0:
                                shellRowsAmount = 0
                            self.tables.textWidth = breite
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
                                neg + "prophet",
                                neg + "archon",
                                neg + "religionsgründertyp",
                                neg + "religionsgruendertyp",
                            ]:
                                rowsAsNumbers |= {72}
                            elif religion in [
                                neg + "babylon",
                                neg + "dertierkreiszeichen",
                            ]:
                                rowsAsNumbers |= {0, 36}
                            elif religion in [
                                neg + "messias",
                                neg + "heptagramm",
                                neg + "hund",
                                neg + "messiase",
                                neg + "messiasse",
                            ]:
                                rowsAsNumbers |= {7}
                            elif religion in [
                                neg + "gleichfoermigespolygon",
                                neg + "gleichförmigespolygon",
                                neg + "nichtsternpolygon",
                                neg + "polygon",
                            ]:
                                rowsAsNumbers |= {16, 37}
                            elif religion in [
                                neg + "vertreterhoehererkonzepte",
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
                        arg[2:10] == "galaxie="
                        or arg[2:16] == "alteschriften="
                        or arg[2:8] == "kreis="
                        or arg[2:11] == "galaxien="
                        or arg[2:9] == "kreise="
                    ):
                        for thing in arg[(arg.find("=") + 1) :].split(","):
                            if thing in [neg + "babylon", neg + "tierkreiszeichen"]:
                                rowsAsNumbers |= {1, 2}
                            elif thing in [neg + "thomas", neg + "thomasevangelium"]:
                                rowsAsNumbers |= {0, 3}
                    elif arg[2:] in [
                        "groessenordnung" + neg,
                        "strukturgroesse" + neg,
                        "groesse" + neg,
                        "stufe" + neg,
                    ]:
                        rowsAsNumbers |= {4, 21}
                    elif arg[2:] in [
                        "universum" + neg,
                        "transzendentalien" + neg,
                        "strukturalien" + neg,
                    ]:
                        rowsAsNumbers |= {5, 54, 55, 65, 75, 76, 77, 78, 79, 80, 81}
                    elif arg[2:13] in ["wirtschaft="]:
                        for thing in arg[(arg.find("=") + 1) :].split(","):
                            if thing in [
                                neg + "system",
                            ]:
                                rowsAsNumbers |= {69}
                            if thing in [
                                neg + "realistisch",
                                neg + "funktioniert",
                            ]:
                                rowsAsNumbers |= {70}
                            if thing in [
                                neg + "erklärung",
                                neg + "erklaerung",
                            ]:
                                rowsAsNumbers |= {71}
                    elif arg[2:15] in ["menschliches="]:
                        for thing in arg[(arg.find("=") + 1) :].split(","):
                            if thing in [
                                neg + "incel",
                                neg + "incels",
                            ]:
                                rowsAsNumbers |= {68}
                            if thing in [
                                neg + "irrationalezahlendurchwurzelbildung",
                                neg + "ausgangslage",
                            ]:
                                rowsAsNumbers |= {73}
                            if thing in [
                                neg + "dominierendesgeschlecht",
                                neg + "maennlich",
                                neg + "männlich",
                                neg + "weiblich",
                            ]:
                                rowsAsNumbers |= {51}
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
                                rowsAsNumbers |= {12, 47, 27, 13, 32}
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
                                # self.tables.spalteGestirn = True
                                rowsAsNumbers |= {64}
                    elif arg[2 : 11 + len(neg)] == "symbole" + neg:
                        rowsAsNumbers |= {36, 37}
                    elif arg[2:30] == "primzahlvielfachesuniversum=":
                        # int(value) if (len(neg) == 0) == (value > 1) and value not in (0,1,2) else None
                        puniverseprims_only |= {
                            abs(chosen)
                            if (len(neg) == 0) == (abs(chosen) == chosen)
                            else None
                            for chosen in [
                                int(value) for value in (arg[30:].split(","))
                            ]
                        } - {None, 0, 1}
                        # self.tables.primUniversePrimsSet.add(int(2))
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
                                generRows |= {(40, 41)}
                            elif word in [
                                neg + "gut",
                                neg + "böse",
                                neg + "lieb",
                                neg + "schlecht",
                            ]:
                                generRows |= {(38, 39)}
                                rowsAsNumbers |= {52, 53}
                            elif word in [
                                neg + "zeit",
                                neg + "raum",
                                neg + "zeitlich",
                                neg + "räumlich",
                            ]:
                                generRows |= {(49, 50)}
                            elif word in [
                                neg + "meinungen",
                                neg + "anderemenschen",
                                neg + "ruf",
                            ]:
                                generRows |= {(60, 61)}
                            elif word in [
                                neg + "selbstgerechtigkeit",
                                neg + "selbstgerecht",
                            ]:
                                generRows |= {(62, 63)}
                            elif word in [
                                neg + "egoismus",
                                neg + "altruismus",
                                neg + "egoist",
                                neg + "altruist",
                            ]:
                                generRows |= {(66, 67)}
                    elif arg[2:17] == "inkrementieren=":
                        for word in arg[17:].split(","):
                            if word in [
                                neg + "universum",
                            ]:
                                rowsAsNumbers |= {43, 54, 74}

                elif (
                    len(arg) > 1
                    and arg[1] == "-"
                    and len(self.bigParamaeter) > 0
                    and self.bigParamaeter[-1] == "zeilen"
                ):  # unteres Kommando
                    if arg[2:7] == "alles" and len(neg) == 0:
                        paramLines.add("all")
                    elif arg[2:7] == "zeit=":
                        for subpara in arg[7:].split(","):
                            if neg + "=" == subpara:
                                paramLines.add("=")
                            elif neg + "<" == subpara:
                                paramLines.add("<")
                            elif neg + ">" == subpara:
                                paramLines.add(">")
                    elif arg[2:11] == "zaehlung=":
                        paramLines |= (
                            self.tables.getPrepare.parametersCmdWithSomeBereich(
                                arg[11:], "n", neg
                            )
                        )
                        # for word in arg[11:].split(","):
                        #    if (
                        #        word.isdecimal()
                        #        or (word[1:].isdecimal() and word[0] == neg)
                        #    ) and (
                        #        (int(word) > 0 and neg == "")
                        #        or (int(word) < 0 and neg != "")
                        #    ):
                        #        paramLines.add(str(abs(int(word))) + "z")
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
                    elif arg[2 : 2 + len("potenzenvonzahlen=")] == "potenzenvonzahlen=":
                        for word in arg[2 + len("potenzenvonzahlen=") :].split(","):
                            if (
                                word.isdecimal()
                                or (word[1:].isdecimal() and word[0] == neg)
                            ) and (
                                (int(word) > 0 and neg == "")
                                or (int(word) < 0 and neg != "")
                            ):
                                paramLines.add(str(abs(int(word))) + "^")
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
                        paramLines |= (
                            self.tables.getPrepare.parametersCmdWithSomeBereich(
                                arg[22:], "a", neg
                            )
                        )
                    elif arg[2:21] == "nachtraeglichdavon=":
                        paramLines |= (
                            self.tables.getPrepare.parametersCmdWithSomeBereich(
                                arg[21:], "z", neg
                            )
                        )
                elif (
                    len(arg) > 1
                    and arg[1] == "-"
                    and len(self.bigParamaeter) > 0
                    and self.bigParamaeter[-1] == "kombination"
                ):  # unteres Kommando
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
                                self.__willBeOverwritten_rowsOfcombi |= {1}
                            elif thing in [neg + "berufe", neg + "beruf"]:
                                self.__willBeOverwritten_rowsOfcombi |= {2}
                            elif thing in [
                                neg + "kreativität",
                                neg + "intelligenz",
                                neg + "kreativitaet",
                            ]:
                                self.__willBeOverwritten_rowsOfcombi |= {3}
                            elif thing in [neg + "liebe"]:
                                self.__willBeOverwritten_rowsOfcombi |= {4}
                            elif thing in [
                                neg + "transzendenz",
                                neg + "transzendentalien",
                                neg + "strukturalien",
                                neg + "alien",
                            ]:
                                self.__willBeOverwritten_rowsOfcombi |= {5}
                            elif thing in [
                                neg + "leibnitz",
                                neg + "primzahlkreuz",
                            ]:
                                self.__willBeOverwritten_rowsOfcombi |= {6}
                            elif thing in [
                                neg + "männer",
                                neg + "maenner",
                                neg + "frauen",
                            ]:
                                self.__willBeOverwritten_rowsOfcombi |= {7}
                            elif thing in [
                                neg + "evolution",
                                neg + "erwerben",
                                neg + "persoenlichkeit",
                                neg + "persönlichkeit",
                            ]:
                                self.__willBeOverwritten_rowsOfcombi |= {8}
                            elif thing in [
                                neg + "religion",
                                neg + "religionen",
                            ]:
                                self.__willBeOverwritten_rowsOfcombi |= {9}
                elif (
                    len(arg) > 1
                    and arg[1] == "-"
                    and len(self.bigParamaeter) > 0
                    and self.bigParamaeter[-1] == "ausgabe"
                ):  # unteres Kommando
                    if (
                        arg[2 : 2 + len("spaltenreihenfolgeundnurdiese=")]
                        == "spaltenreihenfolgeundnurdiese="
                    ):
                        for number in arg[
                            2 + len("spaltenreihenfolgeundnurdiese=") :
                        ].split(","):
                            if str(number).isdecimal():
                                spaltenreihenfolgeundnurdiese += [int(number)]
                    if arg[2:6] == "art=":
                        outputtype = arg[(arg.find("=") + 1) :]
                        if outputtype == "shell":
                            self.tables.outType = OutputSyntax()
                        elif outputtype == "csv":
                            self.tables.outType = csvSyntax()
                        elif outputtype == "bbcode":
                            self.tables.outType = bbCodeSyntax()
                        elif outputtype == "html":
                            self.tables.outType = htmlSyntax()
                        elif outputtype == "markdown":
                            self.tables.outType = markdownSyntax()
                    elif arg[2:] in ["nocolor", "justtext"] and neg == "":
                        self.tables.getOut.color = False
                    elif (
                        arg[2:] in ["endlessscreen", "endless", "dontwrap", "onetable"]
                        and neg == ""
                    ):
                        self.tables.getOut.oneTable = True
                else:  # oberes Kommando
                    if arg[1:] in ["zeilen", "spalten", "kombination", "ausgabe"]:
                        self.bigParamaeter += [arg[1:]]
                    elif arg[1:] in ["debug"]:
                        infoLog = True
                    elif arg[1:] in ["h", "help"] and neg == "":
                        self.helpPage()
        if not self.tables.getOut.oneTable:
            self.tables.textWidth = (
                self.tables.textWidth
                if shellRowsAmount > self.tables.textWidth + 7 or shellRowsAmount <= 0
                else shellRowsAmount - 7
            )
        return (
            paramLines,
            rowsAsNumbers,
            self.__willBeOverwritten_rowsOfcombi,
            spaltenreihenfolgeundnurdiese,
            puniverseprims_only,
            generRows,
        )

    def helpPage(self):
        global folder
        if "Brython" not in sys.version.split():
            place = os.path.join(
                os.getcwd(), os.path.dirname(__file__), os.path.basename("./readme.txt")
            )
        else:
            place = "readme.txt"
        with open(place) as f:
            read_data = f.read()
        parser.REPLACE_COSMETIC = ()
        html = parser.format(read_data, replace_cosmetic=False)
        if "Brython" not in sys.version.split():
            h = html2text.HTML2Text()
            h.style = "compact"
            plaintext = h.handle(html)
            plaintext = re.sub(r"\\--", "--", plaintext)
            plaintext = re.sub(r"(\*\s+[^\-])", r"\t\1", plaintext)
            plaintext = re.sub(r" \*\*", r"", plaintext)
            plaintext = re.sub(r"\*\s\*", r"", plaintext)
            plaintext = re.sub(r"(\n)([^\s])", r"\1\t\t\2", plaintext)
            plaintext = re.sub(r".*(\* -spalten)", r" \1", plaintext)
            cliout(plaintext)
        else:
            print(html)

    def bringAllImportantBeginThings(self, argv) -> tuple:
        """Einlesen der ersten Tabelle "religion.csv" zu self.relitable
        aller anderen csv dateien
        Parameter werden in Befehle und Nummernlisten gewandelt
        csv Dateien werden angehangen an self.relitable


        @rtype: tuple(int,set,set,list,set,list,set,list,list)
        @return: Spaltenanzahl, Zeilen Ja, Zeilen Nein, Religionstabelle, Spalten, weitere Tabelle daneben, spalten weitere Tabelle, weitere Tabelle für wie sql-join, deren spalten
        """
        global folder
        alxp("bla")
        if "Brython" not in sys.version.split():
            place = os.path.join(
                os.getcwd(),
                os.path.dirname(__file__),
                os.path.basename("./religion.csv"),
            )
        else:
            place = "religion.csv"
        with open(place, mode="r") as csv_file:
            self.relitable: list = []
            for i, col in enumerate(csv.reader(csv_file, delimiter=";")):
                self.relitable += [col]
                if i == 0:
                    self.RowsLen = len(col)
        (
            paramLines,
            self.rowsAsNumbers,
            self.rowsOfcombi,
            spaltenreihenfolgeundnurdiese,
            self.puniverseprims,
            self.generRows,
        ) = self.parametersToCommandsAndNumbers(argv)
        (
            paramLinesNot,
            self.rowsAsNumbersNot,
            self.rowsOfcombiNot,
            spaltenreihenfolgeundnurdieseNot,
            self.puniverseprimsNot,
            self.generRowsNot,
        ) = self.parametersToCommandsAndNumbers(argv, "-")
        self.dataDict: tuple = ({}, {}, {}, {})
        self.spaltenTypeNaming: namedtuple = namedtuple(
            "SpaltenTyp",
            "ordinary generated1 concat1 kombi1 ordinaryNot generate1dNot concat1Not kombi1Not",
        )
        self.spaltenTypeNaming = self.spaltenTypeNaming(
            (0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)
        )

        # self.spaltenArtenNameKey_SpaltenArtenTupleVal_4Key4otherDict = {
        #    "ordinary": (0, 0),
        #    "generated1": (0, 1),
        #    "concat1": (0, 2),
        #    "kombi1": (0, 3),
        #    "ordinaryNot": (1, 0),
        #    "generate1dNot": (1, 1),
        #    "concat1Not": (1, 2),
        #    "kombi1Not": (1, 3),
        # }
        self.spaltenArtenKey_SpaltennummernValue = {
            (0, 0): set(),
            (0, 1): set(),
            (0, 2): set(),
            (0, 3): set(),
            (1, 0): set(),
            (1, 1): set(),
            (1, 2): set(),
            (1, 3): set(),
        }
        self.storeParamtersForColumns()
        self.produceAllSpaltenNumbers()

        # "generated1": (0, 1),
        # "concat1": (0, 2),
        # "kombi1": (0, 3),
        # alxp("üü")
        # alxp(paramLines)
        # alxp(self.rowsAsNumbers)
        # alxp(self.rowsOfcombi)
        # alxp(spaltenreihenfolgeundnurdiese)
        # alxp(self.puniverseprims)
        # alxp(self.generRows)
        # alxp("üü")
        # alxp(self.rowsOfcombi)
        paramLines, paramLinesNot = self.tables.getPrepare.deleteDoublesInSets(
            paramLines, paramLinesNot
        )
        # self.puniverseprims, self.puniverseprimsNot = self.tables.getPrepare.deleteDoublesInSets(
        #    self.puniverseprims, self.puniverseprimsNot
        # )

        # if self.allesParameters != 2:
        #     self.puniverseprimsNot -= self.puniverseprims
        #     self.generRows -= self.generRowsNot
        # else:
        #     self.puniverseprims = set()
        #     self.generRows = set()
        # for prims in self.puniverseprims - self.puniverseprimsNot:
        #     self.tables.primUniversePrimsSet.add(prims)
        # (
        #    self.rowsAsNumbers,
        #    self.rowsAsNumbersNot,
        # ) = self.tables.getPrepare.deleteDoublesInSets(
        #    self.rowsAsNumbers, self.rowsAsNumbersNot
        # )
        # (
        #    self.rowsOfcombi,
        #    self.rowsOfcombiNot,
        # ) = self.tables.getPrepare.deleteDoublesInSets(
        #    self.rowsOfcombi, self.rowsOfcombiNot
        self.rowsAsNumbers = self.spaltenArtenKey_SpaltennummernValue[
            self.spaltenTypeNaming.ordinary
        ]
        self.generRows = self.spaltenArtenKey_SpaltennummernValue[
            self.spaltenTypeNaming.generated1
        ]
        self.puniverseprims = self.spaltenArtenKey_SpaltennummernValue[
            self.spaltenTypeNaming.concat1
        ]
        self.rowsOfcombi = self.spaltenArtenKey_SpaltennummernValue[
            self.spaltenTypeNaming.kombi1
        ]
        for prims in self.puniverseprims:
            self.tables.primUniversePrimsSet.add(prims)

        alxp("üü")
        alxp(paramLines)
        alxp(self.rowsAsNumbers)
        alxp(self.rowsOfcombi)
        alxp(spaltenreihenfolgeundnurdiese)
        alxp(self.puniverseprims)
        alxp(self.generRows)
        alxp("üü")

        alxp("§")
        alxp(self.puniverseprims)
        if len(self.rowsOfcombi) > 0:
            paramLines.add("ka")
        self.tables.generRows = self.generRows
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
        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.concatLovePolygon(self.relitable, self.rowsAsNumbers)

        if len(self.rowsOfcombi) > 0:
            (
                animalsProfessionsTable,
                self.relitable,
                kombiTable_Kombis,
                maintable2subtable_Relation,
            ) = self.tables.getCombis.readKombiCsv(
                self.relitable, self.rowsAsNumbers, self.rowsOfcombi
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
            self.rowsOfcombi,
            kombiTable_Kombis,
            maintable2subtable_Relation,
            spaltenreihenfolgeundnurdiese,
        )

    def start(self, argv) -> tuple:
        """Einlesen der ersten Tabelle "religion.csv" zu self.relitable
        aller anderen csv dateien
        Parameter werden in Befehle und Nummernlisten gewandelt
        csv Dateien werden angehangen an self.relitable


        @rtype: tuple(int,set,set,list,set,list,set,list,list)
        @return: Spaltenanzahl, Zeilen Ja, Zeilen Nein, Religionstabelle, Spalten, weitere Tabelle daneben, spalten weitere Tabelle, weitere Tabelle für wie sql-join, deren spalten
        """
        global folder

        if "Brython" not in sys.version.split():
            place = os.path.join(
                os.getcwd(),
                os.path.dirname(__file__),
                os.path.basename("./religion.csv"),
            )
        else:
            place = "religion.csv"
        with open(place, mode="r") as csv_file:
            self.relitable: list = []
            for i, col in enumerate(csv.reader(csv_file, delimiter=";")):
                self.relitable += [col]
                if i == 0:
                    self.RowsLen = len(col)
        (
            paramLines,
            self.rowsAsNumbers,
            self.rowsOfcombi,
            spaltenreihenfolgeundnurdiese,
            puniverseprims,
            generRows,
        ) = self.parameters(argv)
        alxp("üü")
        alxp(paramLines)
        alxp(self.rowsAsNumbers)
        alxp(self.rowsOfcombi)
        alxp(spaltenreihenfolgeundnurdiese)
        alxp(puniverseprims)
        alxp(generRows)
        alxp("üü")
        (
            paramLinesNot,
            self.rowsAsNumbersNot,
            self.rowsOfcombiNot,
            spaltenreihenfolgeundnurdieseNot,
            puniverseprimsNot,
            generRowsNot,
        ) = self.parameters(argv, "-")
        paramLines, paramLinesNot = self.tables.getPrepare.deleteDoublesInSets(
            paramLines, paramLinesNot
        )
        # puniverseprims, puniverseprimsNot = self.tables.getPrepare.deleteDoublesInSets(
        #    puniverseprims, puniverseprimsNot
        # )

        if self.allesParameters != 2:
            puniverseprimsNot -= puniverseprims
            generRows -= generRowsNot
        else:
            puniverseprims = set()
            generRows = set()
        for prims in puniverseprims - puniverseprimsNot:
            self.tables.primUniversePrimsSet.add(prims)
        self.tables.generRows = generRows
        (
            self.rowsAsNumbers,
            self.rowsAsNumbersNot,
        ) = self.tables.getPrepare.deleteDoublesInSets(
            self.rowsAsNumbers, self.rowsAsNumbersNot
        )
        (
            self.rowsOfcombi,
            self.rowsOfcombiNot,
        ) = self.tables.getPrepare.deleteDoublesInSets(
            self.rowsOfcombi, self.rowsOfcombiNot
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
        (
            self.relitable,
            self.rowsAsNumbers,
        ) = self.tables.getConcat.concatLovePolygon(self.relitable, self.rowsAsNumbers)

        if len(self.rowsOfcombi) > 0:
            (
                animalsProfessionsTable,
                self.relitable,
                kombiTable_Kombis,
                maintable2subtable_Relation,
            ) = self.tables.getCombis.readKombiCsv(
                self.relitable, self.rowsAsNumbers, self.rowsOfcombi
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
            self.rowsOfcombi,
            kombiTable_Kombis,
            maintable2subtable_Relation,
            spaltenreihenfolgeundnurdiese,
        )

    def __init__(self, argv=[], testing=False):
        global Tables, infoLog
        self.argv = argv
        self.allesParameters = 0
        self.tables = Tables()
        self.workflowEverything(argv, testing)

    def workflowEverything(self, argv, testing):
        global infoLog
        if testing:
            (
                self.RowsLen,
                paramLines,
                paramLinesNot,
                self.relitable,
                self.rowsAsNumbers,
                animalsProfessionsTable,
                self.rowsOfcombi,
                kombiTable_Kombis,
                maintable2subtable_Relation,
                spaltenreihenfolgeundnurdiese,
            ) = self.bringAllImportantBeginThings(argv)
        else:
            (
                self.RowsLen,
                paramLines,
                paramLinesNot,
                self.relitable,
                self.rowsAsNumbers,
                animalsProfessionsTable,
                self.rowsOfcombi,
                kombiTable_Kombis,
                maintable2subtable_Relation,
                spaltenreihenfolgeundnurdiese,
            ) = self.start(argv)
        self.tables.getMainTable.createSpalteGestirn(self.relitable, self.rowsAsNumbers)
        (
            finallyDisplayLines,
            newTable,
            numlen,
            rowsRange,
            old2newTable,
        ) = self.tables.getPrepare.prepare4out(
            paramLines,
            paramLinesNot,
            self.relitable,
            self.rowsAsNumbers,
        )
        if len(self.rowsOfcombi) > 0:
            newTable = self.combiTableWorkflow(
                animalsProfessionsTable,
                finallyDisplayLines,
                kombiTable_Kombis,
                maintable2subtable_Relation,
                newTable,
                old2newTable,
                paramLines,
            )
        # rowAmounts = self.tables.getOut.oneTableToMany(newTable, True, rowsRange)
        # spaltenreihenfolgeundnurdiese
        newTable = self.tables.getOut.onlyThatColumns(
            newTable, spaltenreihenfolgeundnurdiese
        )
        self.tables.getOut.cliOut(finallyDisplayLines, newTable, numlen, rowsRange)
        alxp(
            "1. http://goexchange.de/viewtopic.php?f=13&t=2683#p17239 () \n    9. anderen etwas vormachen können (Bahai)\n    1/9. den anderen Strukturgrößen außer der Einheit (9, 1/9) etwas vormachen können"
        )
        # alxp(
        #    '2. Bei Kombi sollte ich noch programmieren, wegen letzter Spalte "Religionen", dass Klammern und Vorzeichen + - dennoch zu richtigen letztendlichen Zeilen der Endausgabe zugeordnet werden.'
        # )
        alxp(
            """SCHLIMMER BUG: bei kombi Sachen kein Zeilenumbruch mehr!
             BUG zwar jetzt beseitigt, aber ich will doch keine Zeilenumbrüche
             bei kombi.csv Ausgaben! Ich kümmere mich darum, wenn ich
             geistig leistungsfähiger sein werde"""
        )
        alxp(
            """Die Modallogikvielfacher müsste ich noch einprogrammieren
             Wenn ich programmiert habe, wie multipliziert wird, um zu erreichen, dass die Modallogiken umgesetzt werden, werde ich
             programmieren, dass die bisherige Multiplikation, die man kaum verstehen kann, auch besser verständlich gemacht werden kann und sich ggf.
             auf 2 Spalten oder mehr erstrecken wird, statt auf einer, wie bisher. So wird es verständlicher"""
        )
        alxp(
            """Alternative Farbgebung: gerade Zahlen und durch 3 teilbare und dazu welche Zählung es ist. Mod 2 = hell dunkel,
            mod 3 = rot, grün, blau; Zählung: pure Farben oder gebräunte Farben alternierend
            NEIN: Ich mache nur die Zahlen vorn abgwechseln hell dunkel je nach Zählung"""
        )
        alxp(
            "Bei mehreren Spalten beide Farbgebungen automatisch wechseln lassen, cmd cli Parameter gibt jedoch explizit beides an, aber pro Spalte oder für alle oder Alternierungsmodulotyp"
        )
        alxp("vim: iIaAoOjJ mit Registern arbeiten wegen Löschen ohne ausschneiden")
        alxp(
            """Ich könnte einen schnelleren String oder Listen usw. Datentyp erschaffen. \n
             Dazu erbe ich String oder etc. den Addieren oder so Operator schreibe ich um,\n
             dass der sich die Stellen nur merken soll und nicht konkatenieren soll. \n
             Dann gibt es dann am Ende nur noch so einen Extra-Befehl, der das dann erst wirklich konkatenieren soll! \n
            Mit f-string concateniert er am Schnellsten, gut ist auch: building a list of strings, then calling "".join() \n
            plus damit zusammen:  using a list comprehension inline \n
            """
        )
        alxp(
            """ Überlegen wo ich besser Hashmaps statt Listen verwenden sollte oder Tuple"""
        )
        alxp("Die meisten Listen durch Dicts ersetzen: fast immer schneller! ")
        alxp(
            "Die Geschwindigkeitsteigerugnen entstehn meist durch anschließndes Zusammenfügen zu einer dann festen Größe."
        )
        alxp(
            "Ich müsste mal alles durchtesten, und zwar fast alles: ob auch alles richtig angezeigt wird, wenn ich Religion 3-n anzeigen lassen will, bzw. etwas anderes größer als 1, anstell nur zB 3"
        )
        alxp("Ich muss noch --universum aufteilen!")
        alxp(
            "bei html und bbcode und breite nict gestetzt noch breite=0 und bildschirmbreite= unendlich setzen!"
        )
        alxp(
            "alles wahrscheinlich besser durch dicts ersetzen, und zeitmessungen hier und da machen und ausgeben"
        )
        alxp(
            "irgendwann weg machen von mehrfachen einbindungen von libs in mehreren dateien"
        )
        alxp(
            """Ich müsste noch etwas aus der Programm Klasse heraus refactoren,
             in die Tabellen-Klasse - das zu Kombi.csv gehört und überhaupt
             sollte ich das ganze total anders refactoren und archtitektonisch
             deutlich aufbessern!
             """
        )
        alxp(
            "nicht nur nur alle monde anzeigen, auch nur alle sonnen anzeigen, obwohl das schon mit -monde geht!"
        )
        #        alxp(
        #            "Überprüfung aller Funktionen nach Umprogrammierung wegen Brython!kombiTable_Kombis"
        #        )
        # alxp(
        #    "Bug: Es zeigt manchmal nicht alle Spalten an, z.B. wenn ich mehrere Kommaspalten angebe in der CLI"
        # )
        # alxp("kein Wortumbruch funktioniert nicht bei Kombinationen")
        #        alxp(
        #            "Es muss mein Programm sein, dass die Zeichen beim Zeilenumbruch verschluckt, da es bei beiden pyphen und pyhyphen passiert: Bereichsangabe"
        #        )
        #        alxp(
        #            "Die super hohen Monde aus der Kugel müsste ich noch eintragen in die Tabelle"
        #        )
        # alxp("die 0 weg machen bei der ersten Zeile immer")
        # alxp("Zeilen Option machen: nicht nur vielfache, sondern auch Potenzen")
        # alxp(
        #    "Leere Zeilen bei Kombis einer Tabelle auf mehrere wegen Bildschirmbreite: löschen bei Ausgabe!"
        # )
        #        alxp("1. Geschwindigkeitsoptimierungen, Pythonspezifisches)
        # alxp(
        #    "2. Audit, ob Doku = Befehle = Tabelleninhalte\n3. Überlegen, was noch rein in die Tabelle\n4. Debugging und ggf. Unit-Tests"
        # )
        # alxp("1. Clean Code\n2. Vollständigkeit der Befehle auch")
        # alxp(
        #    "1. Ich muss noch Tabelleninhalte ins Programm bringen, die schon in der Tabelle stecken"
        # )

    def combiTableWorkflow(
        self,
        animalsProfessionsTable,
        finallyDisplayLines,
        kombiTable_Kombis,
        maintable2subtable_Relation,
        newTable,
        old2newTable,
        paramLines,
    ):
        """alle  Schritte für kombi:
        1. lesen: KombiTable und relation, was von kombitable zu haupt gehört
                  und matrix mit zellen sind zahlen der kombinationen
                  d.h. 3 Sachen sind das Ergebnis
        2. prepare: die Zeilen, die infrage kommen für Kombi, d.h.:
                                key = haupttabellenzeilennummer
                                value = kombitabellenzeilennummer
        3. Zeilenumbruch machen, wie es bei der Haupt+Anzeige-Tabelle auch gemacht wurde
           prepare4out
        4. Vorbereiten des Joinens beider Tabellen direkt hier rein programmiert
           (Müsste ich unbedingt mal refactoren!)
        5. joinen
           Wenn ich hier jetzt alles joine, und aber nicht mehrere Zellen mache pro Kombitablezeile,
           d.h. nicht genauso viele Zeilen wie es der Kombitablezeilen entspricht,
           d.h. ich mache nur eine Zeile, in der ich alle kombitableteilen nur konkatteniere,
           dann ist das Ergebnis Mist in der Ausagbe, weil der Zeilenumbruch noch mal gemacht werden müsste,
           der jedoch bereits schon gemacht wurde.
           Der musste aber vorher gemacht werden, denn wenn man ihn jetzt machen würde,
           dann müsste man das eigentlich WIEDER mit der ganzen Tabelle tun!
           Also etwa alles völlig umprogrammieren?
        6. noch mal nur das ausgeben lassen, das nur ausgegeben werden soll
        7. letztendliche Ausagebe von allem!!
        """
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
            animalsProfessionsTable,
            old2newTableAnimalsProfessions,
        ) = self.tables.getPrepare.prepare4out(
            set(),
            set(),
            animalsProfessionsTable,
            self.rowsOfcombi,
            self.tables.getCombis.sumOfAllCombiRowsAmount,
        )
        KombiTables = self.tables.getCombis.prepareTableJoin(
            ChosenKombiLines, newTable_kombi_1
        )
        newTable = self.tables.getCombis.tableJoin(
            newTable,
            KombiTables,
            maintable2subtable_Relation,
            old2newTable,
            self.rowsOfcombi,
        )
        return newTable


#        alxp(
#            "Wie erreiche ich das?: Ich mache erst Geschwindigkeitsoptimierungen. Welche Sachen kann ich optimieren?"
#        )
#        alxp(
#            "Concattenieren von allen Strings, listen appenden bei vorhandener veränderung lieber durch funktionale programmierung "
#        )
#        alxp(
#            "In Schleifen lieber lokale Variablen, KeyError catchen anstatt if machen für Erstinitialisierung eines dicts"
#        )
#        alxp(
#            "imports besser erst bedingt rein holen, ggf. in funktionen, Häufungen von Funktionsaufrufen minimieren, z.B. bei Rekursionen"
#        )
#        alxp(
#            "Fkt mit if drin, das irgendwann für immer gilt: besser bei Gegelenheit die funktion wie funktionszeiger überschreiben, so dass man in Schleife kein if braucht"
#        )

if __name__ == "__main__":
    Program(sys.argv)
# inverted:
# \e[7mi


# Wie könnte ich Unit-Tests realisieren?
# Ich müsste erst alles jeweilige instantiieren
# Erst müsste ich die einfachen Funktionen durchprobieren
# und dann die darauf aufbauenden
# Ich sollte mich wohl auch im Netz schlau machen, wie man mit Python am Besten
# Unit-Tests schreibt

# Durch Unit-Tests lässt sich das Testen automatisieren
# import unittest
# from tribool import Tribool libs: nose und pytest


"""
Irgendwie muss ich mir jetzt überlegen, wie ich das jetzt alles umgestalte und
architektonisch schöner mache
Ganze klar, die eine Stelle gehört in die ganz andere Klasse.
Aber auch so müsste ich es mal anders umbauen.

Ich bilde den Ablauf wider:
    1. init
        da rasselt alles durch bis alles ausgegeben wird
            dieses durchrasseln sollte ich in eine Extra Methode verlagern
            bringAllImportantBeginThings() bzw. start() sollte ich adäquat umbenenenn.
                das durchrasselnde sollte ich aufplitten in module
        das ganze refactoring mache ich mit pycharm
        was ich für Parameter programmiert habe, müsste ich auch ins Richtige
        rein verschieben mit pycharm
"""
