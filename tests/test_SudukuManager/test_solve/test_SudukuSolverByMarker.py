# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 13:50:25 2019

@author: Eric
"""
import unittest
from tests import GRILLES_PATH
from SudukuManager.solver.SudukuSolverByMarker import SudukuSolverByMarker

class TestSudukuSolverByMarker(unittest.TestCase):

    def setUp(self):
        self.suduku = SudukuSolverByMarker(GRILLES_PATH+'Grille_veryhard1.sku')

    def test_solve(self):
        self.assertEqual(self.suduku.solve(), SudukuSolverByMarker.COMPLETED)
        self.assertEqual(str(self.suduku.grid),
                         "-------------------------------\n"
                        +"| 1  8  6 | 2  5  9 | 7  4  3 |\n"
                        +"| 9  4  3 | 6  7  1 | 2  8  5 |\n"
                        +"| 5  2  7 | 8  3  4 | 6  1  9 |\n"
                        +"-------------------------------\n"
                        +"| 4  9  2 | 7  1  5 | 8  3  6 |\n"
                        +"| 3  6  8 | 4  9  2 | 1  5  7 |\n"
                        +"| 7  1  5 | 3  6  8 | 4  9  2 |\n"
                        +"-------------------------------\n"
                        +"| 2  5  9 | 1  4  7 | 3  6  8 |\n"
                        +"| 6  7  1 | 5  8  3 | 9  2  4 |\n"
                        +"| 8  3  4 | 9  2  6 | 5  7  1 |\n"
                        +"-------------------------------\n")


if __name__ == "__main__":
    unittest.main()