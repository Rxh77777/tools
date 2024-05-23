# -*- encoding: utf-8 -*-
'''
@Project:tools
@File  : dateTimeChange.py
@Author: rxh
@Desc :
@Date  :  2024/05/23 09:45
'''
from datetime import date
import pandas as pd


def date_conversion(target_date,conversion_type):
    """
    Args:
        target_date (_type_): int/str/date/pd.Timestamp
        type (_type_): 'int'/'str'/'date'/'timestamp'
    """
    if type(target_date) is int:
        year = f'{target_date}'[:4]
        month = f'{target_date}'[4:6]
        day = f'{target_date}'[6:]
    elif type(target_date) is str:
        year = target_date.split('-')[0]
        month = target_date.split('-')[1]
        day = target_date.split('-')[2]
    elif type(target_date) in [date, pd.Timestamp]:
        year = f'{target_date.year}'
        month = f'{target_date.month}'
        day = f'{target_date.day}'
    if conversion_type == 'int':
        return int(year)*10000+int(month)*100+int(day)
    elif conversion_type == 'str':
        return f'{year}-{month}-{day}'
    elif conversion_type == 'date':
        return date(year = int(year), month = int(month), day = int(day))
    elif conversion_type == 'timestamp':
        return pd.Timestamp(year = int(year), month = int(month), day = int(day))
    else:
        return year,month,day
