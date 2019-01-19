# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 00:01:59 2019

@author: Eric
"""

from SudukuManager.board.BaseSubgrid import BaseSubgrid

class SudukuLine(BaseSubgrid):
    """Représente une ligne d'une grille de Suduku"""
    def __init__(self, data_line=[]):
        BaseSubgrid.__init__(self, case_list= sorted(data_line,
                                                     key=lambda x: x.get_column()))
        self.line = self.cases[0].get_line()
        # TODO : Controle de cohérence du n° de ligne de toutes les cases

    def __str__(self):
        return "line {} : ({})".format(
                self.line,
                ",".join((str(val) for val in self.get_values())))

    def __eq__(self, other):
        # Controle du type d'objet 'other'
        if not isinstance(other, SudukuLine):
            return False

        # Controle du nombre de cases
        if len(self.cases) != len(other.cases):
            return False

        # Controle des cases
        for i, case in enumerate(self.cases):
            if case != other[i]:
                return False

        return True