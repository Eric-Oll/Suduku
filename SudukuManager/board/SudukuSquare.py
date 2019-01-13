# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 10:15:03 2019

@author: Eric
"""
from SudukuManager.board.BaseSubgrid import BaseSubgrid

class SudukuSquare(BaseSubgrid):
    def __init__(self, data_square=[], line_size=3):
        """
        data_square doit etre une flatten-list
        """
        self.line_size = line_size
        BaseSubgrid.__init__(self, case_list= sorted(data_square,
                                                     key=lambda x: "{}_{}"
                                                     .format(x.getLine(),
                                                             x.getColumn())))


    def print(self):
        for i, item in enumerate(self.getCases()):
            if (i+1) % self.line_size == 0:
                print()
            print(item.getValue(), end="")

    def __getitem__(self, index):
        if isinstance(index, tuple):
            return self.getCase(index[0]*self.line_size+index[1])
        elif isinstance(index, int):
            return self.getCase(index)

    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            self.setCase(index[0]*self.line_size+index[1], value)
        elif isinstance(index, int):
            self.setCase(index, value)



