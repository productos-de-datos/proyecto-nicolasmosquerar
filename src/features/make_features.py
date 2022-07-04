import pandas as pd
def make_features():
    """Leemos el data frame para luego configurar su fecha en el formato pedido
        luego lo movemos a la subcarpeta features para los puntos posteriores
    """
    

    df = pd.read_csv(r'data_lake/business/precios-diarios.csv',index_col=None,header=0)
    
    df["fecha"] = pd.to_datetime(df["fecha"]).dt.strftime('%Y-%m-%d')
    
    df.to_csv("data_lake/business/features/precios-diarios.csv",index=None, header=True)
    
    


if __name__ == "__main__":
    import doctest
    make_features()
    doctest.testmod()
