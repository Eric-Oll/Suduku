# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 09:09:39 2019

@author: Eric
"""
from SudukuManager.board.SudukuAlphabet import SudukuAlphabet
from SudukuManager.board.BaseCase import BaseCase

class BaseSubgrid:
    def __init__(self, case_list=[]):
        self.cases = case_list

    def get_case(self, index):
        if index<len(self.cases):
            return self.cases[index]

    def set_case(self, index, value):
        if index < len(self.cases):
            if isinstance(value, BaseCase):
                self.values[index] = value
            elif isinstance(value, int) or value is None:
                self.cases[index].set_value(value)
            else:
                raise ValueError(f"<{self.__class__}.setCase : Type de valeur non reconnu : {type(value)}")

    def get_values(self):
        return [case.get_value() for case in self.get_cases() if not case.is_empty()]

    def get_cases(self):
        return self.cases

    def is_completed(self):
        """
        Return :
            - True : si la ligne est complète et valide
            - False sinon
        """
        values = [x.get_value() for x in self.cases if not x.is_empty()]
        if len(values) != len(SudukuAlphabet.VALUES):
            return False
        for i, item in  enumerate(sorted(values)):
            if item != SudukuAlphabet.VALUES[i]:
                return False
        return True

    def __getitem__(self, index):
        return self.get_case(index)

    def __setitem__(self, index, value):
        self.set_case(index, value)
