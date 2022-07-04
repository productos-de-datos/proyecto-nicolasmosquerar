"""Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
import pandas as pd

def compute_monthly_prices():
   
    df = pd.read_csv("data_lake/cleansed/precios-horarios.csv",index_col=None,header=0)
    
    df["anio-mes"]=pd.to_datetime(df["fecha"]).dt.strftime('%Y-%m')
    
    preciosmensuales =  df[["anio-mes", "precio"]]
    
    preciosmensuales = preciosmensuales.groupby("anio-mes", as_index=False)["precio"].mean()
    
    preciosmensuales = preciosmensuales.rename(columns={"anio-mes":"fecha"})
    
    preciosmensuales["fecha"] = pd.to_datetime(preciosmensuales["fecha"]).dt.strftime('%Y-%m-%d')
    
    preciosmensuales.to_csv("data_lake/business/precios-mensuales.csv",index=None, header=True)
    
    
   


if __name__ == "__main__":
    import doctest
    compute_monthly_prices()
    doctest.testmod()
