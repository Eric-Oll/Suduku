# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 23:29:38 2019

@author: Eric
"""

class BaseCase:
    """
    Classe de base pour les case du Suduku
    """
    def __init__(self, line_index=0, column_index=0, value=None):
        self.line = line_index
        self.column = column_index
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def is_empty(self):
        return self.value is None

    def get_position(self):
        return self.line, self.column

    def get_line(self):
        return self.line

    def get_column(self):
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
        return str(self.get_value())

    def __repr__(self):
        return f"<BaseCase : value={self.value}, position=[{self.line},{self.column}]>"