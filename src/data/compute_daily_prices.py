"""Realizamos el promedio de los precios de manera mensual

"""

import pandas as pd
import numpy as np

def compute_daily_prices():
    df=pd.read_csv('data_lake/cleansed/precios-horarios.csv',index_col=None, parse_dates=['fecha'])
    media=df.groupby(['fecha'])['precio'].mean()
    media.to_csv('data_lake/business/precios-diarios.csv')


if __name__ == "__main__":
    import doctest
    compute_daily_prices()
    doctest.testmod()
