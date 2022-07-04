"""
descargamos con  wget para  los archivos del repositorio y movemos a la carpeta landing

"""

from datetime import datetime
import argparse
import os
import shutil
import wget 
import requests

def ingest_data():
    for num in range(1995, 2022):
        if num in range(2016, 2018):
            url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xls?raw=true'.format(num)
            file = requests.get(url, allow_redirects=True)
            open('data_lake/landing/{}.xls'.format(num), 'wb').write(file.content)
        else:
            url = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{}.xlsx?raw=true'.format(num)
            file = requests.get(url, allow_redirects=True)
            open('data_lake/landing/{}.xlsx'.format(num), 'wb').write(file.content)


if __name__ == "__main__":
    import doctest
    ingest_data()
    doctest.testmod()
        
        
        
        
        
        
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
