#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""

Grades = {
    'A': '100%',
    'B': '90%',
    'C': '80%',
    'D': '70%',
    'F': '60%'
    }

def get_score_summary(string):
    fhandler = open('inspection_results.csv', 'r')
    for row in fhandler:
        for column in row:
            print column
    fhandler.close()

get_score_summary('string')
