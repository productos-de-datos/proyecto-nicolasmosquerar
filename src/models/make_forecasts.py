import pandas as pd
import pickle
from sklearn.metrics import r2_score
def make_forecasts():
    """construimos el forecast y lo guardamos como archivo csv
    """
    datos = pd.read_csv(
        'data_lake/business/features/precios-diarios.csv', index_col=None, header=0)
    final_db = datos.copy()

    datos['fecha'] = pd.to_datetime(datos['fecha'], format='%Y-%m-%d')
    datos['year'], datos['month'], datos['day'] = \
        datos['fecha'].dt.year, datos['fecha'].dt.month, datos['fecha'].dt.day

    x_total = datos.copy().drop('fecha', axis=1)
    y_total = x_total.pop('precio')

    regression = pickle.load(open('src/models/precios-diarios.pkl', 'rb'))
    prediccion = regression.predict(x_total)

    r2_score(y_total,regression.predict(x_total))

    final_db['prediccion'] = prediccion

    final_db.to_csv(
        'data_lake/business/forecasts/precios-diarios.csv', index=None)
if __name__ == "__main__":
    import doctest
    make_forecasts()
    doctest.testmod()