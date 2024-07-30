from django import template
import pandas as pd

register = template.Library()

@register.filter
def get_item(lst, key):
    return lst[key]


@register.filter
def avg(lst):
    df = pd.Series(lst)
    return round(df.mean(), 2)

@register.filter
def max(lst):
    df = pd.Series(lst)
    return round(df.max(), 2)

@register.filter
def min(lst):
    df = pd.Series(lst)
    return round(df.min(), 2)

@register.filter
def median(lst):
    df = pd.Series(lst)
    return round(df.median(), 2)