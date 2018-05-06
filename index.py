#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01, 02, 03"""
import csv
import json


grade_chart = {
    'A': float(1),
    'B': float(.9),
    'C': float(.8),
    'D': float(.7),
    'F': float(.6),
}

def get_score_summary(passfile):

    fhandler = open(passfile, 'r')
    readscore = csv.reader(fhandler, delimiter=',')
    simple_dict = {}

    for row in readscore:
        boro = row[1]
        grade = row[10]
        camisid = row[0]

        if camisid not in simple_dict and grade in grade_chart:
            simple_dict[camisid] = [grade, boro]
    fhandler.close()

    deduplicated = {}
    for grade in simple_dict.values():
        letter = grade[0]
        borough = grade[1]

        if borough in deduplicated:
            deduplicated[borough][1] += grade_chart[letter]
            deduplicated[borough][0] += 1
        else:
            deduplicated[borough] = [1, grade_chart[letter]]

    final_score = {}
    for boro, grade in deduplicated.iteritems():
        final_score[boro] = grade[0], grade[1]/grade[0]
    return final_score


def get_market_density(passfile):

    fhandler = open(passfile, 'r')
    marketload = json.load(fhandler)
    mdata = {}

    for values in marketload['data']:
        boro = values[8].strip()

        if boro in mdata:
            mdata[boro] += 1
        else:
            mdata[boro] = 1
    return mdata


def correlate_data(restaurants, markets, outfile):

    fhandler = open(outfile, 'w')
    restaurants = get_score_summary(restaurants)
    markets = get_market_density(markets)
    final_result = {}

    for key, value in markets.iteritems():
        boro = key.upper()
        num_markets = float(value)
        num_resturants = float(restaurants[boro][0])

        if boro in restaurants:
            final_result[boro] = restaurants[boro][1], num_markets/num_resturants

    json.dump(final_result, fhandler)
