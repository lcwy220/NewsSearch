# -*- coding: utf-8 -*-

import time

def unix2hadoop_date(ts):
    return time.strftime('%Y_%m_%d', time.localtime(ts))

def ts2datetime(ts):
    return time.strftime('%Y-%m-%d', time.localtime(ts))

def ts2date(ts):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))

def ts2datehour(ts):
    return time.strftime('%Y-%m-%d %H:%M', time.localtime(ts))

def datehour2ts(date):
    return int(time.mktime(time.strptime(date, '%Y-%m-%d %H')))


def ts2hour(ts):
    return int(time.strftime('%H', time.localtime(ts)))

def datetime2ts(date):
    return int(time.mktime(time.strptime(date, '%Y-%m-%d')))

def window2time(window, size=24*60*60):
    return window*size

def datetimestr2ts(date):
    return time.mktime(time.strptime(date, '%Y%m%d'))

def ts2datetimestr(ts):
    return time.strftime('%Y%m%d', time.localtime(ts))

def ts2HourlyTime(ts, interval):
    # interval 取 Minite、Hour
    ts = ts - ts % interval
    return ts

def ts2datetime_full(ts):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(ts))

if __name__=='__main__':
    result = datetime2ts('2013-09-02')
    #result = ts2date(1377993600)
    print 'result:', result
