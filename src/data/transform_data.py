"""Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

"""
import pandas as pd
import glob
import os
import shutil

def transform_data():   
    destino= r'C:\Users\Nicolás\github-classroom\productos-de-datos\proyecto-nicolasmosquerar\data_lake\raw'
    os.chdir('data_lake/landing/')
    ruta=r'C:\Users\Nicolás\github-classroom\productos-de-datos\proyecto-nicolasmosquerar\data_lake\landing'
    for excel in os.listdir(ruta):
        if excel.endswith('.xlsx'):
            out = excel.split('.')[0]+'.csv'
            df=pd.read_excel(excel)
            df.to_csv(out,index=False)
        
    for excel in os.listdir(ruta):
        if excel.endswith('.xls'):
            out = excel.split('.')[0]+'.csv'
            df=pd.read_excel(excel)
            df.to_csv(out,index=False)
        
    for csv in os.listdir(ruta):
        if csv.endswith('.csv'):
            shutil.move(f"{csv}", destino)

#'data_lake/raw/{}.csv'.format(excel)
if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
