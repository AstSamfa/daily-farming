import pandas as pd


def validar(departamento, municipio, vegetal):
    ruta_archivo = 'static/csv/resultado.csv'

    dataframe = pd.read_csv(ruta_archivo)

    fila_resultante = dataframe.loc[
                          (dataframe['Departamento'] == departamento) & (dataframe['Municipio'] == municipio)].iloc[0:1]

    if not fila_resultante.empty:
        dato_resultante = fila_resultante[vegetal].iloc[0]
    else:
        return None

    return dato_resultante
