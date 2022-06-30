import pandas as pd
import matplotlib.pyplot as plt

def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.
    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.
    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.
    """
 

    precios_diarios = pd.read_csv(r'data_lake/business/precios-diarios.csv', sep=',', header=0, index_col=None)
    precios_diarios['fecha'] = pd.to_datetime(precios_diarios["fecha"])
    x = precios_diarios.fecha
    y = precios_diarios.precio
    plt.plot(x, y, 'g')
    plt.title('Promedio de Precios Diarios')
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.xticks(rotation='vertical')
    plt.savefig("data_lake/business/reports/figures/daily_prices.png")


if __name__ == "__main__":
    import doctest
    make_daily_prices_plot()
    doctest.testmod()
