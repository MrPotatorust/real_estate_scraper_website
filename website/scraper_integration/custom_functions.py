import pandas as pd


def meanD(lst):
    df = pd.Series(lst)
    return round(df.mean(), 2)


def maxD(lst):
    df = pd.Series(lst)
    return round(df.max(), 2)


def minD(lst):
    df = pd.Series(lst)
    return round(df.min(), 2)


def medianD(lst):
    df = pd.Series(lst)
    return round(df.median(), 2)