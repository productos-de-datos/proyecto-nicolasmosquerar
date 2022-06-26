"""
Módulo de ingestión de datos.

usamos la libreria wget para descargar los archivos del repositorio en el rango de fechas deseado
tambien se usa la libreria os para especificar la ruta del sistema 

"""
import argparse
import os
import shutil
from datetime import datetime
import requests 

def ingest_data():
    os.chdir('data_lake/landing/')
    for i in range(1995,2022):
        if i in range(2016,2018):
            dir='https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true'.format(i)
            requests.get(dir)
        else:
            dir='https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xlsx?raw=true'.format(i)
            requests.get(dir)
        
        
        
        
        
        
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
