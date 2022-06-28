"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
import luigi
import ingest_data
class DataIngestion(luigi.Task):
    
    def output(self):
        return luigi.LocalTarget('/resultado.txt')
    
    def run(self):
        from ingest_data import ingest_data
        with self.output().open('w') as files_ingested:
            ingest_data()
            
class DataTransformation(luigi.Task):
    
    def requires(self):
        return DataIngestion()   
     
    def output(self):
        return luigi.LocalTarget('data_lake/raw/resultado2.txt')   
    
    def run(self):
        from transform_data import transform_data
        with self.output().open('w') as files_transformed:
            transform_data()     

class CreacionTabla(luigi.Task):
    def requires(self):
        return DataTransformation()
    
    def output(self):
        return luigi.LocalTarget('data_lake/cleansed/resultado3.txt')
    
    def run(self):
        from clean_data import clean_data
        with self.output().open('w') as table:
            clean_data()
class CalculoPreciosPromedio(luigi.Task):
    def requires(self):
        return CreacionTabla()
    
    def output(self):
        return luigi.LocalTarget('data_lake/business/resultado4.txt')
    
    def run(self):
        from compute_daily_prices import compute_daily_prices
        with self.output().open('w') as daily_prices:
            compute_daily_prices()
class CalculoPreciosMensual(luigi.Task):
    def requires(self):
        return CalculoPreciosPromedio()
    
    def output(self):
        return luigi.LocalTarget('data_lake/business/resultado5.txt')
    
    def run(self):
        from compute_monthly_prices import compute_monthly_prices
        with self.output().open('w') as monthly_prices:
            compute_monthly_prices()       
    
if __name__ == "__main__":    
    luigi.run(['CalculoPreciosMensual','--local-scheduler'])
    
if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
