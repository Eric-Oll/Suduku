# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 14:39:54 2019

@author: Eric
"""

import unittest
from SudukuManager.board.SudukuColumn import SudukuColumn
from SudukuManager.board.BaseCase import BaseCase

class TestSudukuColumn(unittest.TestCase):
    def test_is_completed(self):
        # Création d'un ligne complète
        column_test = SudukuColumn([BaseCase(value=i+1, line_index=i, column_index=1) for i in range(9)])
        self.assertTrue(column_test.is_completed())

        # Création d'une ligne incomplète
        column_test[5] = None
        self.assertFalse(column_test.is_completed())

        column_test[5] = 1
        self.assertFalse(column_test.is_completed())


if __name__ == "__main__":
    unittest.main()