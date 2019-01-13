# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 19:33:56 2019

@author: Eric
"""
from SudukuManager.board.BaseCase import BaseCase
from SudukuManager.board.SudukuAlphabet import SudukuAlphabet

class MarkedCase(BaseCase):
    def __init__(self, line_index=0, column_index=0, value=None,):
        BaseCase.__init__(self, line_index=line_index, column_index=column_index, value=value)

        if value is None:
            self.marks = SudukuAlphabet.VALUES.copy()
        else:
            self.marks = []

    def set_value(self, value):
        super().set_value(value)
        if not self.is_empty():
            self.remove_all_marks()

    def add_mark(self, value):
        if not self.is_marked(value):
            self.marks.append(value)

    def get_marks(self):
        return self.marks

    def is_marked(self, value):
        return value in self.marks

    def remove_mark(self, values):
        """
        Supprime le marquage de la valeur ou de la liste des valeurs
        et s'il reste un seul élément marqué alors il l'affecte comme valeur trouvé
        Return :
            True : Si une mofication a été trouvé
            False : sinon
        """
        if not self.is_empty():
            return False

        if isinstance(values, int):
            values = [values]

        for value in values:
            if self.is_marked(value):
                self.marks.remove(value)

        if len(self.marks) == 1:
            self.set_value(self.marks.pop())
            return True
        else:
            return False

    def remove_all_marks(self):
        self.marks = []

# EOF MarkCase.py