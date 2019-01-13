# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 19:33:56 2019

@author: Eric
"""
from SudukuManager.board.BaseCase import BaseCase
from SudukuManager.board.SudukuAlphabet import SudukuAlphabet

class MarkedCase(BaseCase):
    def __init__(self, value=None, line_index=0, column_index=0):
        BaseCase.__init__(value=value, line_index=line_index, column_index=column_index)

        if value is None:
            self.marks = SudukuAlphabet.VALUES.copy()
        else:
            self.marks = []

    def add_mark_value(self, value):
        if not self.is_marked(value):
            self.marks.append(value)

    def get_mark_values(self):
        return self.marks

    def is_marked(self, value):
        return value in self.marks

    def remove_mark_value(self, values):
        """
        Supprime le marquage de la valeur ou de la liste des valeurs
        et s'il reste un seul élément marqué alors il l'affecte comme valeur trouvé
        Return :
            La valeur trouvée si une valeur est trouvé
            None : sinon
        """
        if isinstance(values, int):
            values = [values]

        for value in values:
            if self.is_marked(value):
                self.marks.remove(value)

        if len(self.marks) == 1:
            self.setValue(self.marks.pop())

        return self.getValue()



# EOF MarkCase.py