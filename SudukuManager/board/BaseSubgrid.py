# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 09:09:39 2019

@author: Eric
"""
from SudukuManager.board.SudukuAlphabet import SudukuAlphabet
from SudukuManager.board.BaseCase import BaseCase

class BaseSubgrid:
    def __init__(self, case_list=[]):
        self.values = case_list

    def getCase(self, index):
        if index<len(self.values):
            return self.values[index]

    def setCase(self, index, value):
        if index < len(self.values):
            if isinstance(value, BaseCase):
                self.values[index] = value
            elif isinstance(value, int) or value is None:
                self.values[index].setValue(value)
            else:
                raise ValueError(f"<{self.__class__}.setCase : Type de valeur non reconnu : {type(value)}")

    def getCases(self):
        return self.values

    def is_completed(self):
        """
        Return :
            - True : si la ligne est complète et valide
            - False sinon
        """
        values = [x.getValue() for x in self.values if x.getValue() is not None]
        if len(values) != len(SudukuAlphabet.VALUES):
            return False
        for i, item in  enumerate(sorted(values)):
            if item != SudukuAlphabet.VALUES[i]:
                return False
        return True

    def __getitem__(self, index):
        return self.getCase(index)

    def __setitem__(self, index, value):
        self.setCase(index, value)
