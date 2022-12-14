import requests
import os
import errno
from logg import log


class Alkemy:

    """  Esta clase contiene las funciones en la cual se obtienen los datos de museo, cine y biblioteca (petición GET), se descargan y se guardan en un directorio, además 
    en esta misma función se les da el manejo en tal caso de que el archivo ya esté en los directorios  """

    def museo_datos():
        try:
            data = requests.get(
                "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv ", allow_redirects=True)
            os.makedirs('museos/2022-julio')
            open('museos/2022-julio/museos-24-07-2022.csv',
                 'wb').write(data.content)
            log.info('Archivo de Museo obtenido con éxito')
        except OSError as e:
            log.info('Archivo de Museo ya esta en el directorio')
            if e.errno != errno.EEXIST:
                raise

    def cine_datos():

        try:
            data = requests.get(
                "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/392ce1a8-ef11-4776-b280-6f1c7fae16ae/download/cine.csv ", allow_redirects=True)
            os.makedirs('cines/2022-julio')
            open('cines/2022-julio/cines-24-07-2022.csv',
                 'wb').write(data.content)
            log.info('Archivo Cine obtenido con éxito')
        except OSError as e:
            log.info('Archivo Cine ya esta en el directorio')
            if e.errno != errno.EEXIST:
                raise

    def biblioteca_datos():
        try:
            data = requests.get(
                "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/biblioteca_popular.csv", allow_redirects=True)
            os.makedirs('bibliotecas/2022-julio')
            open('bibliotecas/2022-julio/bibliotecas-24-07-2022.csv',
                 'wb').write(data.content)
            log.INFO('Archivo Biblioteca obtenido con éxito')
        except OSError as e:
            log.info('Archivo Biblioteca ya esta en el directorio')
            if e.errno != errno.EEXIST:
                raise


if __name__ == "__main__":
    log.info('Extracción de datos en proceso')
    Alkemy.museo_datos()
    Alkemy.cine_datos()
    Alkemy.biblioteca_datos()
