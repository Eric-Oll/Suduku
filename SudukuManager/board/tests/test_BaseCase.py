# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 17:53:53 2019

@author: Eric
"""

import unittest

from SudukuManager.board.BaseCase import BaseCase

class BaseCaseTest(unittest.TestCase):

    def test_get_square(self):

        self.assertEqual(BaseCase(0,0).get_square(),0)
        self.assertEqual(BaseCase(0,1).get_square(),0)
        self.assertEqual(BaseCase(0,2).get_square(),0)

        self.assertEqual(BaseCase(1,0).get_square(),0)
        self.assertEqual(BaseCase(1,1).get_square(),0)
        self.assertEqual(BaseCase(1,2).get_square(),0)

        self.assertEqual(BaseCase(2,0).get_square(),0)
        self.assertEqual(BaseCase(2,1).get_square(),0)
        self.assertEqual(BaseCase(2,2).get_square(),0)

        self.assertEqual(BaseCase(0,3).get_square(),1)
        self.assertEqual(BaseCase(0,4).get_square(),1)
        self.assertEqual(BaseCase(0,5).get_square(),1)

        self.assertEqual(BaseCase(1,3).get_square(),1)
        self.assertEqual(BaseCase(1,4).get_square(),1)
        self.assertEqual(BaseCase(1,5).get_square(),1)

        self.assertEqual(BaseCase(2,3).get_square(),1)
        self.assertEqual(BaseCase(2,4).get_square(),1)
        self.assertEqual(BaseCase(2,5).get_square(),1)

        self.assertEqual(BaseCase(0,6).get_square(),2)
        self.assertEqual(BaseCase(0,7).get_square(),2)
        self.assertEqual(BaseCase(0,8).get_square(),2)

        self.assertEqual(BaseCase(1,6).get_square(),2)
        self.assertEqual(BaseCase(1,7).get_square(),2)
        self.assertEqual(BaseCase(1,8).get_square(),2)

        self.assertEqual(BaseCase(2,6).get_square(),2)
        self.assertEqual(BaseCase(2,7).get_square(),2)
        self.assertEqual(BaseCase(2,8).get_square(),2)
#
        self.assertEqual(BaseCase(3,0).get_square(),3)
        self.assertEqual(BaseCase(3,1).get_square(),3)
        self.assertEqual(BaseCase(3,2).get_square(),3)

        self.assertEqual(BaseCase(4,0).get_square(),3)
        self.assertEqual(BaseCase(4,1).get_square(),3)
        self.assertEqual(BaseCase(4,2).get_square(),3)

        self.assertEqual(BaseCase(5,0).get_square(),3)
        self.assertEqual(BaseCase(5,1).get_square(),3)
        self.assertEqual(BaseCase(5,2).get_square(),3)

        self.assertEqual(BaseCase(3,3).get_square(),4)
        self.assertEqual(BaseCase(3,4).get_square(),4)
        self.assertEqual(BaseCase(3,5).get_square(),4)

        self.assertEqual(BaseCase(4,3).get_square(),4)
        self.assertEqual(BaseCase(4,4).get_square(),4)
        self.assertEqual(BaseCase(4,5).get_square(),4)

        self.assertEqual(BaseCase(5,3).get_square(),4)
        self.assertEqual(BaseCase(5,4).get_square(),4)
        self.assertEqual(BaseCase(5,5).get_square(),4)

        self.assertEqual(BaseCase(3,6).get_square(),5)
        self.assertEqual(BaseCase(3,7).get_square(),5)
        self.assertEqual(BaseCase(3,8).get_square(),5)

        self.assertEqual(BaseCase(4,6).get_square(),5)
        self.assertEqual(BaseCase(4,7).get_square(),5)
        self.assertEqual(BaseCase(4,8).get_square(),5)

        self.assertEqual(BaseCase(5,6).get_square(),5)
        self.assertEqual(BaseCase(5,7).get_square(),5)
        self.assertEqual(BaseCase(5,8).get_square(),5)
#
        self.assertEqual(BaseCase(6,0).get_square(),6)
        self.assertEqual(BaseCase(6,1).get_square(),6)
        self.assertEqual(BaseCase(6,2).get_square(),6)

        self.assertEqual(BaseCase(7,0).get_square(),6)
        self.assertEqual(BaseCase(7,1).get_square(),6)
        self.assertEqual(BaseCase(7,2).get_square(),6)

        self.assertEqual(BaseCase(8,0).get_square(),6)
        self.assertEqual(BaseCase(8,1).get_square(),6)
        self.assertEqual(BaseCase(8,2).get_square(),6)

        self.assertEqual(BaseCase(6,3).get_square(),7)
        self.assertEqual(BaseCase(6,4).get_square(),7)
        self.assertEqual(BaseCase(6,5).get_square(),7)

        self.assertEqual(BaseCase(7,3).get_square(),7)
        self.assertEqual(BaseCase(7,4).get_square(),7)
        self.assertEqual(BaseCase(7,5).get_square(),7)

        self.assertEqual(BaseCase(8,3).get_square(),7)
        self.assertEqual(BaseCase(8,4).get_square(),7)
        self.assertEqual(BaseCase(8,5).get_square(),7)

        self.assertEqual(BaseCase(6,6).get_square(),8)
        self.assertEqual(BaseCase(6,7).get_square(),8)
        self.assertEqual(BaseCase(6,8).get_square(),8)

        self.assertEqual(BaseCase(7,6).get_square(),8)
        self.assertEqual(BaseCase(7,7).get_square(),8)
        self.assertEqual(BaseCase(7,8).get_square(),8)

        self.assertEqual(BaseCase(8,6).get_square(),8)
        self.assertEqual(BaseCase(8,7).get_square(),8)
        self.assertEqual(BaseCase(8,8).get_square(),8)

