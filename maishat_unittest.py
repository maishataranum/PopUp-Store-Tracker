"""
Maisha Taranum
Class: CS 521 - Summer 2
Date: 08/15/2023
Final Project Unit Test
"""

import unittest
from shop_class import Shop
from maishat_finalproject import summarize_by_area, summarize_by_date

class TestShopMethods(unittest.TestCase):

    def setUp(self):
        self.shops = shops = [Shop('shoes', 'downtown', '2023-06-25',\
                                   [50, 60, 70],'10:00 AM - 8:00 PM'),
          Shop('shirts', 'outletmall', '2023-06-27', [25, 30],\
               '9:00 AM - 9:00 PM'),
          Shop('pants', 'downtown', '2023-06-27', [40, 45],\
               '10:30 AM - 7:30 PM'),
          Shop('coats', 'outletmall', '2023-06-28', [80],\
               '9:30 AM - 8:30 PM'),
          Shop('shirts', 'downtown', '2023-06-29', [20, 22],\
               '11:00 AM - 6:00 PM'),
          Shop('shoes', 'outletmall', '2023-06-30', [55, 65],\
               '10:00 AM - 9:00 PM'),
          Shop('pants', 'downtown', '2023-06-30', [50, 55, 60],\
               '11:00 AM - 8:00 PM'),
          Shop('coats', 'outletmall', '2023-05-01', [90, 95],\
               '10:00 AM - 7:00 PM'),
          Shop('shirts', 'downtown', '2023-05-01', [18, 20],\
               '12:00 PM - 5:00 PM')]

    def test_summarize_by_area(self):
        area = 'downtown'
        count = summarize_by_area(self.shops, area)
        self.assertEqual(count, 3)  # Expected count for 'downtown'

    def test_summarize_by_date(self):
        date = '2023-06-27'
        count = summarize_by_date(self.shops, date)
        self.assertEqual(count, 2)  # Expected count for '2023-06-27'

if __name__ == '__main__':
    unittest.main()
