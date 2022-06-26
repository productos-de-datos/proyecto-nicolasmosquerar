"""Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
import pandas as pd
def compute_monthly_prices():
   
    df=pd.read_csv('data_lake/cleansed/precios-horarios.csv',index_col=None, parse_dates=['fecha'])
    media=df.groupby(pd.Grouper(freq='1M', key='fecha'))['precio'].mean().dropna()
    #print(media)
    media.to_csv('data_lake/business/precios-mensuales.csv')


if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
