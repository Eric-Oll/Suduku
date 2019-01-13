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
                                                     key=lambda x:x.get_column()))
