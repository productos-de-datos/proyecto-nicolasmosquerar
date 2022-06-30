"""Transformamos los archivos a formato csv 

"""
import pandas as pd
import os
import shutil

def transform_data():   
    
  for file in range(1995,2022):
      
      if file in range(1995,2000):
          read_file = pd.read_excel(
              'data_lake/landing/{}.xlsx'.format(file),header= 3)
          read_file.to_csv(
                  'data_lake/raw/{}.csv'.format(file),index=None )
      elif file in range(2000,2018):
          if file in [2016,2017]:
              read_file=pd.read_excel(
                  'data_lake/landing/{}.xls'.format(file),header= 2)
              read_file.to_csv('data_lake/raw/{}.csv'.format(file),index=None)
          else:
              read_file = pd.read_excel(
              'data_lake/landing/{}.xlsx'.format(file),header= 3)
          read_file.to_csv(
                  'data_lake/raw/{}.csv'.format(file),index=None )
          
      else:
                read_file = pd.read_excel(
              'data_lake/landing/{}.xlsx'.format(file),header= 0)
                read_file.to_csv(
              'data_lake/raw/{}.csv'.format(file),index=None ) 

if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
