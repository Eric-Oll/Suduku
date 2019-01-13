# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 23:24:40 2019

@author: Eric

Ce module contient :
    - SudukuGrid : Classe représentant une grille de Suduku
"""
__version__ = 0.1
import re
import itertools

from SudukuManager.board.BaseCase import BaseCase
from SudukuManager.board.SudukuLine import SudukuLine
from SudukuManager.board.SudukuColumn import SudukuColumn
from SudukuManager.board.SudukuSquare import SudukuSquare

import logging as log
#log.basicConfig(level=log.DEBUG)

class SudukuGrid:
    NB_LINES = 9
    NB_COLS = 9

    def __init__(self, type_case=BaseCase):
        self.grid = []
        for i in range(SudukuGrid.NB_LINES):
            column = []
            for j in range(SudukuGrid.NB_COLS):
                column.append(type_case(line_index=i, column_index=j))
            self.grid.append(column)

    def print_grid(self):
        for i, line in enumerate(self.grid):
            if i%3 == 0:
                print("-"*(3*10))
            for j, case in enumerate(line):
                if j%3 == 0:
                    print("|", end="")
                if case.is_empty():
                    print(" . ", end="")
                else:
                    print(" {} ".format(case), end="")
            print()

    def getCase(self, line, column):
        if line < SudukuGrid.NB_LINES and column < SudukuGrid.NB_COLS:
            return self.grid[line][column]
        else:
            return None

    def getLine(self, line):
        if line < SudukuGrid.NB_LINES:
            return SudukuLine(self.grid[line])
        else:
            return None

    def getColumn(self, column):
        if column < SudukuGrid.NB_COLS:
            return SudukuColumn([self[i, column] for i in range(SudukuGrid.NB_LINES)])

    def getSquare(self, square):
        """
        Retourne le carré correspondant au square
        - soit via le n° de de carré
            ------------------------------
            |         |         |        |
            |    0    |    1    |    2   |
            |         |         |        |
            ------------------------------
            |         |         |        |
            |    3    |    4    |    5   |
            |         |         |        |
            ------------------------------
            |         |         |        |
            |    6    |    7    |    8   |
            |         |         |        |
            ------------------------------
        - soit ses coordonnées
            ------------------------------
            |         |         |        |
            |  [0,0]  |  [0,1]  |  [0,2] |
            |         |         |        |
            ------------------------------
            |         |         |        |
            |  [1,0]  |  [1,1]  |  [1,2] |
            |         |         |        |
            ------------------------------
            |         |         |        |
            |  [2,0]  |  [2,1]  |  [2,2] |
            |         |         |        |
            ------------------------------

       """
        # TODO : getSquare() à faire
        if isinstance(square, tuple):
            # Cas des coordonnées
            lig, col = square
        elif isinstance(square, int):
            # Cas d'index
            lig = square // 3
            col = square % 3
        else:
            raise TypeError(f"Type de référence au carré incorrect. Valeur passée = {type(square)}")

        return SudukuSquare([self[i, j]
                             for i in range(lig*3, (lig+1)*3)
                             for j in range(col*3, (col+1)*3)
                             ])

    def get_subgrids(self):
        return itertools.chains(
                (self.getLine(i) for i in range(SudukuGrid.NB_LINES)),
                (self.getColumn(i) for i in range(SudukuGrid.NB_COLS)),
                (self.getSquare(i) for i in range(SudukuGrid.NB_LINES))
                )

    def is_completed(self):
        """
        Controle si la grille est complète et valide
        """
        # Controle des lignes
        control_line =  [self.getLine(i).is_completed() for i in range(SudukuGrid.NB_LINES)]
        if not all(control_line):
            log.debug("Lignes : "+str(control_line))

        # Controle des colonnes
        control_column = [self.getColumn(i).is_completed() for i in range(SudukuGrid.NB_COLS)]
        if not all(control_column):
            log.debug("Colonnes : "+str(control_column))

        # Controle des carrés
        control_square = [self.getSquare(i).is_completed() for i in range(SudukuGrid.NB_LINES)]
        if not all(control_square):
            log.debug("Carres : "+str(control_square))

        return all(control_line) and all(control_column) and all(control_square)

    def __getitem__(self, index):
        """
        Retour la case de la grille en position [i,j]
        exemple : Suduku[i,j]
        """
        if isinstance(index, tuple) and len(index)==2:
            return self.getCase(line=index[0], column=index[1])

    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            lig, col = index
        elif isinstance(index, int):
            lig = index // SudukuGrid.NB_COLS
            col = index % SudukuGrid.NB_COLS

        if isinstance(value, BaseCase):
            self.grid[lig][col] = value
        elif isinstance(value, int) or value is None:
            self.grid[lig][col].setValue(value)
        else:
            raise ValueError(f"Type de valeur non reconnu : {type(value)}")


    def load_grid(self, filename):
        """
        Charge une grille de Suduku à partir du fichier 'filename' (doit inclure le chemin).
        Format du fichier :
            <fichier> ::= <ligne>\n<ligne>\<ligne>
            <ligne> ::= <carre>\t<carre>\t<carre>
            <carre> ::= <valeur> <valeur> <valeur>
            <valeur> :: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
            0 représente une case vide
        """
        lig = 0
        with open(filename, 'r') as file:
            line = file.readline()
            while line is not None and lig<SudukuGrid.NB_LINES:
                for j, value in enumerate(re.split("[ \t]", line.strip())):
                    self[lig, j] = int(value) if value != '0' else None
                line = file.readline()
                lig += 1
        self.print_grid()


# EOF SudukuGrid.py
