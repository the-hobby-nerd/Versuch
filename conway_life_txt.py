# -*- coding: utf-8 -*-
"""
Life - zellulärer Automat von John H. Conway
Gitterausschnitt
Wir untersuchen die Umgebung einer Gitterzelle
'sp' ist die Spalte, 0....n, der 'x-Wert'
Zeile ist der y-Wert
x,p sind die absoluten Zellen-Koordinaten
Die benachbarten Wertepare geben delta_x und delta_y an (dx,dy)

              sp0 sp1 sp2 sp3
             -----------------
Zeile 0     |     |    |    |   |  .....
             -----------------
Zeile 1     |-1,-1|0,-1|1,-1|...|  .....
            -----------------
Zeile 2     |-1,0 | x,y |1,0|...|  .....
            -----------------
Zeile 3     |-1,1 | 0,1 |1,1|...|  ......
            -----------------

Zeile n      |   |   |   |   |  .....
             -----------------


@author:
"""

from collections import Counter
import random as rnd 
import numpy as np  # numerische Bibliothek für Arrays
import matplotlib.pyplot as plt # Grafische Darstellung der Figuren (langsam)

def nachbarn(zelle): # pos enthält (x,y) für die aktuelle Zelle
    # Alle möglichen Delta-Positionen um einen Punkt herum  
    # werden in ein Array geschrieben
    x = zelle[0]
    y = zelle[1]
    for dx, dy in [(-1,-1), (0,-1), (1,-1),
                 (-1, 0),         (1, 0),
                 (-1, 1), (0, 1), (1, 1)]:
        # wert = x + dx, y + dy
        # print(wert)
        yield x + dx, y + dy # liefert ein "Generatorobjekt" zurück, also eine abzählbare Menge


def nächsteGeneration(spielfeld):
    # Der Counter zählt die Anzahl der identischen Elemente in einer Liste
    elemente = []  # Leer Liste vorbereiten
    for zelle in spielfeld:  # Über das Spielfeld iterieren
        for nachbar in nachbarn(zelle):  # Für eine Spielfeldposition die Nachbarn ermitteln
            elemente.append(nachbar)
    nachb = Counter(elemente)
    # print("nachb:\n", nachb)
    # Der Counter liefert ein Dictionary zurück Format: {position1: anzahl1, position2: anzahl2, ....}
    # Dictionary {'keyword': value}
    # Beispie:  {(11, 13): 3, (12, 14): 4}
    # Das  
    # print(nachb)
    # Anstatt der vorhergehenden 5 Zeilen kann auch die folgende Zeile benutzz werden
    # Allerdings am Anfang schwerer zu verstehen
    # nachb = Counter([pos for zelle in spielfeld for pos in nachbarn(zelle)]) 
    """ Jetzt die Logik:
      1. Weniger als zwei Nachbarn: lebende Zelle stirbt ab
      2. Mehr als 3 lebende Nachbarn: lebende Zelle stirbt ab
      3. 2 lebende Nachbarn: lebende zelle bleit lebendig --> (anz==2 and pos in spielfeld)
      4. 3 lebende Nachbarn: lebende zelle bleibt, oder tote Zelle wird lebendig ---> anz == 3
    """
    spielfeld_neu = []
    for pos, anz in nachb.items():  # Über die Nachbarn-Liste iterieren
        if (anz == 2 and pos in spielfeld) or anz == 3:
            spielfeld_neu.append(pos)
            # print(pos)
            pass
    return spielfeld_neu
    # Die vorhergehenden 6 Zeilen können in einer Zeile zusamengefaßt werden 
    # return {pos for pos,anz in nachb.items() if anz == 3 or (anz==2 and pos in spielfeld)}
    '''
    "Any fool can write code that a computer can understand. 
    Good programmers write code that humans can understand." - Martin Fowler

    "Jeder Dummkopf kann Code schreiben, den ein Computer verstehen kann. 
    Gute Programmierer schreiben Code, den Menschen verstehen können." -Martin Fowler
    
    Anmerkung: statt "Dumkmopf" könnten wir auch "Angeber" sagen
    '''

# Ein Spielfeld mit vorgegebene exakt definierter Anfangsstruktur erzeugen
# z.B. 3 Zellen in einer Zeile 'leben'

# spielfeld = {(3,3),(4,3),(5,3)} # Blinker

# spielfeld = {(6,8),(7,8),(8,8),
#               (5,7),(7,7),(8,7),
#               (5,6),(9,6),
#               (6,5),(7,5),(9,5),
#               (6,4),(7,4),(8,4)}

# (kleiner) Glider
# spielfeld = {(7,18),
#               (5,17),(7,17),
#               (6,16),(7,16)}

spielfeld = {(9,10),(10,10),(11,10),
              (9,9),(11,9),
              (9,8),(11,8),
              (10,7),
              (7,6),(9,6),(10,6),(11,6),
              (8,5),(10,5),(12,5),
              (10,4),(13,4),
              (9,3),(11,3),
              (9,2),(11,2)}


# Optische darstellung des Soielfeldes
for item in spielfeld:
    plt.scatter(item[0],item[1],c='r')
plt.yticks(np.arange(0, 21, 1))  
plt.xticks(np.arange(0, 21, 1))   
plt.show()


#print((spielfeld))
for i in range(50): #  Wir betrachten 50 Generationen
    print('Schritt: ', i)
    spielfeld = nächsteGeneration(spielfeld)
    # print((spielfeld))
    for item in spielfeld:
        plt.scatter(item[0],item[1], c='orange')
    plt.yticks(np.arange(0, 21, 1))  
    plt.xticks(np.arange(0, 21, 1))   
    plt.show()   

