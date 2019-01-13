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
                                                     key=lambda x: x.get_line()))

