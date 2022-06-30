from sklearn.linear_model import LinearRegression
import pickle
from sklearn.metrics import r2_score
import pandas as pd
"""Realizamos el entrenamiento del modelo el cual se guardara como archivo binario
   
    """
def train_daily_model():

    datos = pd.read_csv( 'data_lake/business/features/precios-diarios.csv', index_col=None, header=0)

    datos['fecha'] = pd.to_datetime(datos['fecha'], format='%Y-%m-%d')
    
    datos['year'], datos['month'], datos['day'] = \
    datos['fecha'].dt.year, datos['fecha'].dt.month, datos['fecha'].dt.day

    x_total = datos.copy().drop('fecha', axis=1)
    y_total = x_total.pop('precio')

    x_train = x_total[:round(x_total.shape[0]*0.75)]
    x_test = x_total[round(x_total.shape[0]*0.75):]
    y_train = y_total[:round(x_total.shape[0]*0.75)]
    y_test = y_total[round(x_total.shape[0]*0.75):]

    regression = LinearRegression()
    regression.fit(x_train, y_train)

    r2_score(y_test,regression.predict(x_test))

    pickle.dump(regression, open('src/models/precios-diarios.pkl', 'wb'))

if __name__ == "__main__":
    import doctest
    train_daily_model()
    doctest.testmod()
