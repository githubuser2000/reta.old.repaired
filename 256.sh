
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
            self.relitable = relitable
            headingsAmount = len(self.relitable[0])
            alxp(self.puniverseprims)
            if True or len(self.puniverseprims) > 0:
                with open("primenumbers.csv", mode="r") as csv_file:
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
                alxp(self.relitable)
            return self.relitable
