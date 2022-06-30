import pandas as pd
import matplotlib.pyplot as plt

def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios mensuales.
    Usando el archivo data_lake/business/precios-mensuales.csv
    """
    

    precios_mes = pd.read_csv(r'data_lake/business/precios-mensuales.csv', sep=',', header=0, index_col=None)
    precios_mes['fecha'] = pd.to_datetime(precios_mes["fecha"])
    x = precios_mes.fecha
    y = precios_mes.precio
    plt.figure(figsize=(15, 6))
    plt.plot(x, y, 'r', label='Promedio mes')
    plt.title('Promedio  Mensual')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.legend()
    plt.xticks(rotation='vertical')
    plt.savefig("data_lake/business/reports/figures/monthly_prices.png")

   

if __name__ == "__main__":
    import doctest
    make_monthly_prices_plot()

    doctest.testmod()