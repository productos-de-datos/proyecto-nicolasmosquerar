"""

    Esta función crea la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """


import os

def create_data_lake():
    
    
    os.mkdir("./data_lake")
    carpetas = ["landing", "raw", "cleansed", "business"]
    subcarp_bus = ["reports", "features", "forecasts"]
    subcarp_bus_reportes = ["figures"]
    raiz = [os.mkdir(os.path.join("./data_lake/", each_dir))
     for each_dir in carpetas]
    business = [os.mkdir(os.path.join("./data_lake/business/", each_dir))
     for each_dir in subcarp_bus]
    reportes = [os.mkdir(os.path.join("./data_lake/business/reports/", each_dir))
     for each_dir in subcarp_bus_reportes]

if __name__ == "__main__":
    import doctest
    create_data_lake()
    doctest.testmod()
