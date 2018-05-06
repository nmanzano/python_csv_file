# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""

import csv

grades = {
    'A': float(1),
    'B': float(.9),
    'C': float(.8),
    'D': float(.7),
    'F': float(.6),
    }

def get_score_summary(string):
    simple_dict = {}
    num_resturants = {}
    final_score = {}

    csvfile = open('inspection_results.csv', 'r')
    reader = csv.DictReader(csvfile, delimiter=',')

    for row in reader:
        camisid = row['CAMIS']
        grade = row['GRADE']
        boro = row['BORO']


        if camisid not in simple_dict and grade in grades:
            simple_dict[camisid] = [grade, boro]

    csvfile.close()

    for resturants in simple_dict.values():

        boro = resturants[1]
        grade = resturants[0]

        if boro in num_resturants:
            num_resturants[boro][1] += grades[grade]
            num_resturants[boro][0] += 1
        else:
            num_resturants[boro] = [1, grades[grade]]

    for boro, grade in num_resturants.iteritems():
        final_score[boro] = grade[0], grade[1]/grade[0]

    return final_score

get_score_summary('inspection_results.csv')
