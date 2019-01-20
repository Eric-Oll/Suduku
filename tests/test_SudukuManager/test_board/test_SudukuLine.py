# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 10:56:21 2019

@author: Eric
"""

import unittest
from SudukuManager.board.SudukuLine import SudukuLine
from SudukuManager.board.BaseCase import BaseCase

class TestSudukuLine(unittest.TestCase):

    def test_is_completed(self):
        # Création d'un ligne complète
        line_test = SudukuLine([BaseCase(value=i+1, line_index=0, column_index=i) for i in range(9)])
        self.assertTrue(line_test.is_completed())

        # Création d'une ligne incomplète
        line_test = SudukuLine([BaseCase(value=i, line_index=0, column_index=i) for i in range(9)])
        line_test[5] = None
        self.assertFalse(line_test.is_completed())

        line_test[5] = 1
        self.assertFalse(line_test.is_completed())


if __name__ == "__main__":
    unittest.main()
