'''
Created by Sami Turbeville
Updated Nov 5, 2019

Homework 4 for CSE D 583
Testing dataframes for certain traits
as specified by homework with proper documentation
'''

import math
import pandas as pd


URL = "https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD"
URL1 = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
DF = pd.read_csv(URL1)
# COL_LIST = ['trip_id', 'starttime', 'stoptime', 'bikeid', 'tripduration',
#             'to_station_name', 'from_station_name', 'from_station_id',
#             'to_station_id', 'usertype', 'gender', 'birthyear']
COL_LIST = ['Date', 'Fremont Bridge East Sidewalk', 'Fremont Bridge West Sidewalk']
COL_TYPES = DF.dtypes

def test_colnames():
    '''
    Passes pytest if all the column names match those
    given in COL_LIST
    '''
    col_num_match = True
    col_names_match = True
    col_names = DF.columns
    if len(col_names) != len(COL_LIST):
        col_num_match = False
    else:
        for item in col_names:
            if item not in COL_LIST:
                col_names_match = False
                break
    assert col_num_match and col_names_match

def test_columntype():
    '''Passes pytest if each column entry is of the same type'''
    column_type_match = True
    for i in COL_LIST:
        column_values = DF[i].to_list()
        column_types = [type(item) for item in column_values]
        num_types = len(set(column_types))
        if num_types > 1:
            column_type_match = False
    assert column_type_match

def test_rownum_10():
    '''Passes if there are more than 10 rows in the dataframe'''
    nrows, _ = DF.shape
    if nrows < 10:
        assert False
    assert True

def test_rownum_1():
    '''Passes if there is at least one row of data in dataframe'''
    row_num, _ = DF.shape
    row_num_pass = bool(row_num > 1)
    assert row_num_pass

def test_nan():
    '''Fails pytest if NaN values are present in the dataframe values'''
    no_nans = True
    for i in COL_LIST:
        col_vals = DF[i].to_list()
        col_types = [type(item) for item in col_vals]
        col_set = set(col_types)
        if len(col_set) > 1 and any(col_set) == float:
            for item in col_vals:
                if math.isnan(item):
                    no_nans = False
    assert no_nans

def test_columtypesmatch():
    '''
    Passes if the types of each column in the dataframe
    matches given column types, COL_TYPES
    '''
    col_types = DF.dtypes
    print(col_types)
    print(COL_TYPES)
    for i, item in enumerate(col_types):
        print(item, COL_TYPES[i])
        print()
        if item != COL_TYPES[i]:
            assert False
    assert True
