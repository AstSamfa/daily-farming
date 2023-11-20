import pandas as pd


def validar(departamento, municipio, vegetal):
    ruta_archivo = 'static/csv/resultado.csv'

    dataframe = pd.read_csv(ruta_archivo)

    fila_resultante = dataframe.loc[
                          (dataframe['Departamento'] == departamento) & (dataframe['Municipio'] == municipio)].iloc[0:1]

    if vegetal in fila_resultante.columns:
        dato_resultante = fila_resultante[vegetal].iloc[0]
        return dato_resultante
    else:
        print(f"Error: La columna '{vegetal}' no se encuentra en el DataFrame.")
        return None
