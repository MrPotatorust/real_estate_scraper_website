import pandas as pd
from django.contrib.auth.models import Group


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


def MaxUserTables(user):

    group = user.groups.first()

    free = Group.objects.get(name='Free')
    basic = Group.objects.get(name='Basic')
    plus = Group.objects.get(name='Plus')
    premium = Group.objects.get(name='Premium')

    if group == free:
        limit = 5
    elif group == basic:
        limit = 10
    elif group == plus:
        limit = 20
    elif group == premium:
        limit = 50
    return limit