# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:43:17 2019

@author: Eric
"""

import unittest
from SudukuManager.board.SudukuGrid import SudukuGrid
from SudukuManager.board.SudukuLine import SudukuLine
from SudukuManager.board.SudukuColumn import SudukuColumn
from SudukuManager.board.BaseCase import BaseCase
from SudukuManager.board.SudukuAlphabet import SudukuAlphabet

class TestSudukuGrid(unittest.TestCase):

    def setUp(self):
        """ Grille de test
        ------------------------------
        | 1  2  3 | 4  5  6 | 7  8  9
        | 4  5  6 | 7  8  9 | 1  2  3
        | 7  8  9 | 1  2  3 | 4  5  6
        ------------------------------
        | 2  3  4 | 5  6  7 | 8  9  1
        | 5  6  7 | 8  9  1 | 2  3  4
        | 8  9  1 | 2  3  4 | 5  6  7
        ------------------------------
        | 3  4  5 | 6  7  8 | 9  1  2
        | 6  7  8 | 9  1  2 | 3  4  5
        | 9  1  2 | 3  4  5 | 6  7  8
        ------------------------------
        """
        self.grid = SudukuGrid(BaseCase)
        for i in range(81):
            self.grid[i] = SudukuAlphabet.VALUES[(i+(i//9)*3+i//27)%9]
#        self.grid.print_grid()

    def test_get_square(self):
        square = self.grid.get_square(0)
        for i in range(3):
            for j in range(3):
                self.assertEqual(i*3+j+1, square[i,j].get_value())


    def test_is_completed(self):
        # Controle de grille valide
        self.assertTrue(self.grid.is_completed())

        # Controle de grille incomplète
        self.grid[2,1] = None
        self.assertFalse(self.grid.is_completed())


        # Controle de grille invalide
        self.grid[2,1] = 7
        self.assertFalse(self.grid.is_completed())

    def test_get_line(self):
        # Controle de la 1ère ligne
        model_line  = SudukuLine(
                [BaseCase(line_index=0, column_index=i, value=val)
                 for i, val in enumerate((1, 2, 3, 4, 5, 6, 7, 8, 9))])
        self.assertEqual(self.grid.get_line(0), model_line,
                        "\nErreur dans la comparaison de la 1ère ligne : "
                        + "\n\tLigne test : " +str(self.grid.get_line(0))
                        + "\n\tOracle : " + str(model_line))

        # Controle de la dernière ligne
        model_line  = SudukuLine(
                [BaseCase(line_index=8, column_index=i, value=val)
                 for i, val in enumerate((9, 1, 2, 3, 4, 5, 6, 7, 8))])
        self.assertEqual(self.grid.get_line(8), model_line,
                        "\nErreur dans la comparaison de la dernière ligne"
                        + "\n\tOracle : " + str(model_line)
                        + "\n\tLigne test : " +str(self.grid.get_line(0))
                        )

        # Controle d'une ligne intermédiaire
        model_line  = SudukuLine(
                [BaseCase(line_index=4, column_index=i, value=val)
                 for i, val in enumerate((5, 6, 7, 8, 9, 1, 2, 3, 4))])
        self.assertEqual(self.grid.get_line(4), model_line,
                        "\nErreur dans la comparaison de la 5ère ligne"
                        + "\n\tLigne test : " +str(self.grid.get_line(0))
                        + "\n\tOracle : " + str(model_line))

    def test_get_column(self):
        # Controle de la 1ère colonne
        model_column  = SudukuColumn(
                [BaseCase(line_index=i, column_index=0, value=val)
                 for i, val in enumerate((1, 4, 7, 2, 5, 8, 3, 6, 9))])
        self.assertEqual(self.grid.get_column(0), model_column,
                        "\nErreur dans la comparaison de la 1ère colonne : "
                        + "\n\tColonne test : " +str(self.grid.get_column(0))
                        + "\n\tOracle : " + str(model_column))

        # Controle de la dernière colonne
        model_column  = SudukuColumn(
                [BaseCase(line_index=i, column_index=8, value=val)
                 for i, val in enumerate((9, 3, 6, 1, 4, 7, 2, 5, 8))])
        self.assertEqual(self.grid.get_column(8), model_column,
                        "\nErreur dans la comparaison de la dernière colonne"
                        + "\n\tOracle : " + str(model_column)
                        + "\n\tColonne test : " +str(self.grid.get_column(0))
                        )

        # Controle d'une ligne intermédiaire
        model_column  = SudukuColumn(
                [BaseCase(line_index=i, column_index=4, value=val)
                 for i, val in enumerate((5, 8, 2, 6, 9, 3, 7, 1, 4))])
        self.assertEqual(self.grid.get_column(4), model_column,
                        "\nErreur dans la comparaison de la 5ère colonne"
                        + "\n\tColonne test : " +str(self.grid.get_column(0))
                        + "\n\tOracle : " + str(model_column))


if __name__ == "__main__":
    unittest.main()