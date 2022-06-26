"""Cree el data lake con sus capas.

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
    
    directorio = "./data_lake"
    directorio_landing = "./data_lake/landing"
    directorio_raw = "./data_lake/raw"
    directorio_cleansed = "./data_lake/cleansed"
    directorio_business = "./data_lake/business"
    directorio_business_features = "./data_lake/business/features"
    directorio_business_forecast = "./data_lake/business/forecasts" 
    directorio_business_reports= "./data_lake/business/reports/figures"
     
    if os.path.exists("./data_lake")==False:   
        os.mkdir(directorio)
        os.mkdir(directorio_landing)
        os.mkdir(directorio_raw)
        os.mkdir(directorio_cleansed)
        os.mkdir(directorio_business)
        os.mkdir(directorio_business_features)
        os.mkdir(directorio_business_forecast)
        os.makedirs(directorio_business_reports)
    else:
        os.removedirs(directorio_business_reports)
        os.rmdir(directorio_business_features)
        os.rmdir(directorio_business_forecast)
        os.rmdir(directorio_landing)
        os.rmdir(directorio_raw)
        os.rmdir(directorio_cleansed)
        os.rmdir(directorio_business)
        os.rmdir(directorio)
    

if __name__ == "__main__":
    import doctest
    create_data_lake()
    doctest.testmod()
