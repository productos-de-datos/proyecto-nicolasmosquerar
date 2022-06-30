"""Limpiamos la data y movemos este archivo limpio a la carpeta cleansed
    """
import pandas as pd
import glob

def clean_data():
    
    ruta=glob.glob(r'data_lake/raw/*.csv')
    lista_csv=[]
    
    for archivo in ruta:
        df=pd.read_csv(archivo,index_col=None,header=0)
        lista_csv.append(df)
        
    lectura=pd.concat(lista_csv,axis=0,ignore_index=True)
    
    fechas= lectura.iloc[: , 0]
    datos=[]
    precio=0
    filas=0
    
    for fecha in fechas:
        for hora in range(0,24):
            precio=(lectura.iloc[filas,(hora+1)])
            datos.append([fecha,hora,precio])
        filas+=1
            
    df=pd.DataFrame(datos,columns=["fecha","hora","precio"])
    df.to_csv("data_lake/cleansed/precios-horarios.csv",index=None,header=True)

if __name__ == "__main__":
    import doctest
    clean_data()
    doctest.testmod()
