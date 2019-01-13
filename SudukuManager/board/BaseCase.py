# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 23:29:38 2019

@author: Eric
"""

class BaseCase:
    """
    Classe de base pour les case du Suduku
    """
    def __init__(self, value=None, line_index=0, column_index=0):
        self.line = line_index
        self.column = column_index
        self.value = value

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def is_empty(self):
        return self.value is None

    def getPosition(self):
        return self.line, self.column

    def getLine(self):
        return self.line

    def getColumn(self):
        return self.column

    def __eq__(self, other):
        if isinstance(other, BaseCase):
            return self.value == other.value \
               and self.line == other.line \
               and self.column == other.column
        elif isinstance(other, int):
            return self.value == other
        else:
            return False

    def __str__(self):
        return str(self.getValue())

    def __repr__(self):
        return f"<BaseCase : value={self.value}, position=[{self.line},{self.column}]>"