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
from luigi import Task, LocalTarget


class ingestar(Task):
    def output(self):
        return LocalTarget('data_lake/landing/test.csv')

    def run(self):

        from ingest_data import ingest_data
        with self.output().open('w') as archivos:
            ingest_data()


class transformar(Task):
    def requires(self):
        return ingestar()

    def output(self):
        return LocalTarget('data_lake/raw/test2.txt')

    def run(self):

        from transform_data import transform_data
        with self.output().open('w') as archivos:
            transform_data()


class limpiar(Task):
    def requires(self):
        return transformar()

    def output(self):
        return LocalTarget('data_lake/cleansed/test3.txt')

    def run(self):

        from clean_data import clean_data
        with self.output().open('w') as archivos:
            clean_data()


class computar_precio_diario(Task):
    def requires(self):
        return limpiar()

    def output(self):
        return LocalTarget('data_lake/business/test4.txt')

    def run(self):

        from compute_daily_prices import compute_daily_prices
        with self.output().open('w') as archivos:
            compute_daily_prices()


class computar_precio_mensual(Task):
    def requires(self):
        return computar_precio_diario()

    def output(self):
        return LocalTarget('data_lake/business/test4.txt')

    def run(self):

        from compute_monthly_prices import compute_monthly_prices
        with self.output().open('w') as archivos:
            compute_monthly_prices()


if __name__ == '__main__':
    luigi.run(["computar_precio_mensual", "--local-scheduler"])

if __name__ == "__main__":
    import doctest

    doctest.testmod()
