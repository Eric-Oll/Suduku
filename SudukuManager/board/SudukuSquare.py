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
                                                     .format(x.get_line(),
                                                             x.get_column())))


    def print(self):
        for i, item in enumerate(self.get_cases()):
            if (i+1) % self.line_size == 0:
                print()
            print(item.get_value(), end="")

    def __getitem__(self, index):
        if isinstance(index, tuple):
            return self.get_case(index[0]*self.line_size+index[1])
        elif isinstance(index, int):
            return self.get_case(index)

    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            self.set_case(index[0]*self.line_size+index[1], value)
        elif isinstance(index, int):
            self.set_case(index, value)



