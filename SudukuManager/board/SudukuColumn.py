# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 10:09:54 2019

@author: Eric
"""

from SudukuManager.board.BaseSubgrid import BaseSubgrid

class SudukuColumn(BaseSubgrid):
    """Représente une colonne d'une grille de Suduku"""
    def __init__(self, data_column=[]):
        BaseSubgrid.__init__(self, case_list= sorted(data_column,
                                                     key=lambda x:x.get_line()))
        self.column = self.cases[0].get_column()
        # TODO : Controle de cohérence du n° de colonne de toutes les cases


    def __str__(self):
        return "column {} : ({})".format(
                self.column,
                ",".join((str(val) for val in self.get_values())))


    def __eq__(self, other):
        # Controle du type d'objet 'other'
        if not isinstance(other, SudukuColumn):
            return False

        # Controle du nombre de cases
        if len(self.cases) != len(other.cases):
            return False

        # Controle des cases
        for i, case in enumerate(self.cases):
            if case != other[i]:
                return False

        return True