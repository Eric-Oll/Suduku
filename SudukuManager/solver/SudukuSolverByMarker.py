# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 10:26:27 2019

@author: Eric
"""
import itertools

import logging as log
log.basicConfig(level=log.DEBUG)
print('Log level :', log.getLevelName(log.getLogger().getEffectiveLevel()))

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

    def print_markers(self):
        for i, line in enumerate(self.grid.iter_lines()):
            if i%3 == 0:
                print("-"*(3*65))
            for j, case in enumerate(line.get_cases()):
                if j%3 == 0 and j!=0:
                    print(" - ", end="")
                if not case.is_empty():
                    print(f"*{case.get_value():^19}*", end="")
                else:
                    print(f"[{','.join(map(str, case.get_marks())):^19}]", end="")

            print()
        print("-"*(3*65)+"\n")

    def updateMarkers(self):
        list_cases = [case for case in self.grid.get_cases() if case.is_empty()]

        while len(list_cases) > 0:
            cur_case = list_cases.pop(0)

            # ligne
            finded_flag = cur_case.remove_mark(self.grid.get_line(cur_case.get_line()).get_values())

            # Colonne
            if not finded_flag:
                finded_flag = cur_case.remove_mark(self.grid.get_column(cur_case.get_column()).get_values())

            # Carré
            if not finded_flag:
                finded_flag = cur_case.remove_mark(self.grid.get_square(cur_case.get_square()).get_values())

            if finded_flag:
                # On ajoute les cases non trouvées des sous-grilles où se trouve cur_case
                for case in itertools.chain(
                        self.grid.get_line(cur_case.get_line()).iter_empty_cases(),
                        self.grid.get_column(cur_case.get_column()).iter_empty_cases(),
                        self.grid.get_square((cur_case.get_line()//3, cur_case.get_column()//3)).iter_empty_cases()
                        ):
                    if case not in list_cases:
                        list_cases.append(case)

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
        self.updateMarkers()

        if self.grid.is_completed():
            return SudukuSolverByMarker.COMPLETED
        elif self.grid.is_invalid():
            return SudukuSolverByMarker.INVALID_GRID

        case = self.get_any_empty_case()
        for value in case.get_marks():
            new_grid = self.copy()
            new_grid.grid[case.get_position()] = value
            if new_grid.solve() == SudukuSolverByMarker.COMPLETED:
                # On remplit les cases vides
                for case in self.grid.get_empty_cases():
                    self.grid[case.get_position()] = new_grid.grid[case.get_position()].get_value()
                return SudukuSolverByMarker.COMPLETED

        # Cas invalide
        return SudukuSolverByMarker.INVALID_GRID

# EOF SudukuSolverByMarker.py