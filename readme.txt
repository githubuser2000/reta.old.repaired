Bedienungsanleitung:
Es gibt 4 Hauptparameter.
[b]Wichtig: die Nebenparameter müssen direkt hinter dem richtigen Hauptparamter stehen, sonst wirken sie nicht und dazwischen darf kein anderer Hauptparameter stehen![/b]
Hauptparameter beginnen mit einem Minus -.
Nebenparameter beginnen mit 2 Minus --.

Hauptparameter:
[list][*]-debug
hat keine Nebenparameter, ist nur für mich als Programmierer relevant und interesssant
[*]-zeilen
[list]
[*]--alles
[*]--zeit=[list][*]<
bedeutet Religionen 1-9[*]=
bedeutet nur Religion 10[*]>
bedeutet Religionen >10
[*]<,=,>
bedeutet Religion 1-10 und höher als 10
Anmerkenung: Anführungszeichen setzen, weil < > sind in Unix Steuersymbole![/list]
[*]--zaehlung=
[list][*]1,2,3,4,5,...[/list]
[*]--typ=[list][*]sonne,mond,planet,schwarzesonne[/list]
[*]--vielfachevonzahlen=[list][*]1,2,3,4,5,...[/list]
[*]--primzahlvielfache=[list][*]1,2,3,4,5,...[/list]
[*]--vorhervonausschnitt=[list=][*]1-5,7-10,14,20[/list]
[*]--nachtraeglichdavon=[list][*]3-6,8[/list]
[*]--potenzenvonzahlen=[list][*]2,3[/list]
[*][/list]
[*]-spalten
[list]
[*]--alles
[*]--breite=[list][*]40[*]70[/list]
[*]--breiten=[list][*]20,50,10,70[*]30,100,20[/list]
[*]--keinenummerierung
[*]--religionen=[list][*]sternpolygon,dertierkreiszeichen,gleichfoermigespolygon,vertreterhoehererkonzepte,messias,religionsgründertyp[/list]
[*]--galaxie= oder --kreis=[list][*]tierkreiszeichen,thomasevangelium[/list]
[*]--strukturgroesse
[*]--universum
[*]--menschliches=[list][*]liebe,ethik,angreifbarkeit,motivation,erhalten,erwerben,benoetigen,krankheit,alpha,kreativ,chef,beruf,loesungen,musik,glaube,erkenntnis,dominierendesgeschlecht,incel,ausgangslage[/list]
[*]--procontra=[list][*]pro,contra[/list]
[*]--wirtschaft=[list][*]system,realistisch,funktioniert,erklaerung[/list]
[*]--licht
[*]--bedeutung=[list][*]primzahlen,anwendungdersonnen,zaehlungen,jura,geist,gestirn[/list]
[*]--symbole
[*]--primzahlvielfachesuniversum=[list][*]2,3,5,7,11
also Primzahlen[/list]
[*]--konzept=[list][*]weisheit,gut,zeit,ruf,selbstgerecht,egoismus[/list]
[*]--inkrementieren=[list][*]universum[/list]
[/list]
[*]-kombination
[list][*]--was[list][*]tiere,berufe,intelligenz,liebe,transzendentalien,strukturalien,primzahlkreuz,frauen,maenner,persoenlichkeit,religionen[/list][/list]
[*]-ausgabe
[list][*]--nocolor
[*]--art=
(nur eins erlaubt)
[list][*]shell,html,csv,markdown,bbcode[/list]
[*]--onetable
[*]--spaltenreihenfolgeundnurdiese=[list][*]3,5,1
d.h. von z.B. 5 Spalten soll zuerst die 3., dann 5. und 1. angezeigt werden und die anderen nicht![/list]
[/list]
[/list]

Umkehrungen:
[list][*]statt 2-11
-2-11
[*]statt 7
-7
[*]statt --symbole
--symbole-
[*]statt --religionen=sternpolygon
--religionen=-sternpolygon[/list]

Beispiel (eine Zeile, nicht mehrere):
[code]reta -zeilen --vorhervonausschnitt=1-9 -spalten --religionen=sternpolygon,gleichfoermigespolygon --galaxie=babylon --breite=50[/code]
