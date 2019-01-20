# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:22:53 2019

@author: Eric
"""

import unittest
from SudukuManager.board.SudukuSquare import SudukuSquare
from SudukuManager.board.BaseCase import BaseCase

class TestSudukuSquare(unittest.TestCase):

    def test_is_completed(self):
        # Création d'un ligne complète
        square_test = SudukuSquare([BaseCase(value=i+1, line_index=i, column_index=1) for i in range(9)])
        self.assertTrue(square_test.is_completed())

        # Création d'une ligne incomplète
        square_test[5] = None
        self.assertFalse(square_test.is_completed())

        square_test[5] = 1
        square_test[1,1] = 5
        self.assertFalse(square_test.is_completed())


if __name__ == "__main__":
    unittest.main()