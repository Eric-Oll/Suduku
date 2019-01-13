# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:43:17 2019

@author: Eric
"""

import unittest
from SudukuManager.board.SudukuGrid import SudukuGrid
from SudukuManager.board.BaseCase import BaseCase
from SudukuManager.board.SudukuAlphabet import SudukuAlphabet

class TestSudukuGrid(unittest.TestCase):

    def setUp(self):
        self.grid = SudukuGrid(BaseCase)
        for i in range(81):
            self.grid[i] = SudukuAlphabet.VALUES[(i+(i//9)*3+i//27)%9]
#        self.grid.print_grid()

    def test_getSquare(self):
        square = self.grid.getSquare(0)
        for i in range(3):
            for j in range(3):
#                print("[{},{}] = {} ; computed = {}".format(i, j, square[i,j].getValue(), i*3+j+1))
                self.assertEqual(i*3+j+1, square[i,j].getValue())


    def test_is_completed(self):
        # Controle de grille valide
        self.assertTrue(self.grid.is_completed())

        # Controle de grille incomplète
        self.grid[2,1] = None
        self.assertFalse(self.grid.is_completed())


        # Controle de grille invalide
        self.grid[2,1] = 7
        self.assertFalse(self.grid.is_completed())



if __name__ == "__main__":
    unittest.main()