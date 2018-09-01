# -*- coding: utf-8 -*-
# Author  : zhj
# File    : athletemodel
# DATE    : 2018/8/9 
# Python Version ：3.6.2
"""

"""
import pickle
from .athletelist import AthleteList, get_coach_data


def put_to_store(file_list):
    """
    put athlete store
    """
    all_athletes = {}
    for each_fine in file_list:
        ath = get_coach_data(each_fine)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dumps(all_athletes, athf)
    except  IOError as ioerr:
        print('File error(put_and_store):' + str(ioerr))
    return (all_athletes)


def get_from_store():
    """
    get athlete store
    """
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_from_store):' + str(ioerr))
    return (all_athletes)


this_files = ['sarah.txt', 'james.txt', 'mikey.txt', 'julie.txt']

data = put_to_store(this_files)













































aaaasssssssssssssssssssssssssssssssssssssss