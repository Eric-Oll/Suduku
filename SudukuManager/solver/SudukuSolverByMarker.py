# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 10:26:27 2019

@author: Eric
"""

from SudukuManager.board.SudukuGrid import SudukuGrid
from SudukuManager.board.MarkCase import MarkedCase

class SudukuSolverByMarker:
    NO_SOLUTION = 0
    INVALID_GRID = -1
    COMPLETED = 1

    def __init__(self, filename=None):
        self.grid = SudukuGrid(MarkedCase)

        # Chargement de la grille
        if filename is not None:
            self.grid.load_grid(filename)
            self.grid.print_grid()

    def copy(self):
        """Retourne une copie de l'objet"""
        newGridSolver = SudukuSolverByMarker()
        for case in self.grid.get_cases():
            new_case = newGridSolver.grid.get_case(case.get_line(), case.get_column())
            new_case.set_value(case.get_value())
            for mark in case.get_marks():
                new_case.add_mark(mark)
        return newGridSolver

    def updateMarkers(self):
        list_cases = [case for case in self.grid.get_cases() if case.is_empty()]

        while len(list_cases) > 0:
            cur_case = list_cases.pop()
            # ligne
            finded_flag = cur_case.remove_mark([case.get_value() \
                                 for case in self.grid.get_line(cur_case.get_line()).get_cases() \
                                 if not case.is_empty()])
            # Colonne
            if not finded_flag:
                finded_flag = cur_case.remove_mark([case.get_value() \
                                 for case in self.grid.get_column(cur_case.get_column()).get_cases() \
                                 if not case.is_empty()])
            # Carré
            if not finded_flag:
                finded_flag = cur_case.remove_mark([case.get_value() \
                                 for case in self.grid.get_square((cur_case.get_line()//3, cur_case.get_column()//3)).get_cases() \
                                 if not case.is_empty()])

            if finded_flag:
                # On ajoute les cases non trouvées des sous-grilles où se trouve cur_case
                # ... ligne
                list_cases.extend([case \
                                 for case in self.grid.get_line(cur_case.get_line()).get_cases() \
                                 if case.is_empty()])
                # ... colonne
                list_cases.extend([case \
                                 for case in self.grid.get_column(cur_case.get_column()).get_cases() \
                                 if case.is_empty()])
                # ... carré
                list_cases.extend([case \
                                 for case in self.grid.get_square((cur_case.get_line()//3, cur_case.get_column()//3)).get_cases() \
                                 if case.is_empty()])

            # colonne
        for subgrid in self.grid.get_subgrids():
            for case in subgrid.get_cases():
                if case.is_empty():
                    if case.remove_mark(subgrid.get_values()):
                        finded_flag = True

    def get_any_empty_case(self):
        for case in self.grid.get_empty_cases():
            return case

    def solve(self):
        """
        Tente de résoudre la grille avec l'hypothèse 'assumption_case'
        Return :
            - COMPLETED : si une solution est trouvée
            - INVALID_GRID : si l'on arrive à une incohérence
        """
        print('*****************')
        self.grid.print_grid()

        self.updateMarkers()

        if self.grid.is_completed():
            print('--> comleted :')
            self.grid.print_grid()
            return SudukuSolverByMarker.COMPLETED
        elif self.grid.is_invalid():
            print('--> invalid :')
            self.grid.print_grid()
            return SudukuSolverByMarker.INVALID_GRID

        new_grid = self.copy()
        case = self.get_any_empty_case()
        for value in case.get_marks():
            print('--------------')
            print('Case : ', repr(case), 'Value = ',value)
            new_grid.grid[case.get_position()] = value
            if new_grid.solve() == SudukuSolverByMarker.COMPLETED:
                print('--> comleted : Case : ', repr(case), 'Value = ',value)
                self.grid.print_grid()
                # On remplit les cases vides
                for case in self.grid.get_empty_cases():
                    self.grid[case.get_position()] = new_grid.grid[case.get_position()].get_value()
                return SudukuSolverByMarker.COMPLETED
            else:
                print('--> invalid : Case : ', repr(case), 'Value = ',value)
                self.grid.print_grid()


        # Cas invalide
        return SudukuSolverByMarker.INVALID_GRID

# EOF SudukuSolverByMarker.py