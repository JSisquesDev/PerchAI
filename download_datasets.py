from dotenv import load_dotenv
import os
import json
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import shutil
import time

def download_dataset(dataset, path):
    # Aseguramos que la ruta exista
    os.makedirs(path, exist_ok=True)
       
    # Nos autenticamos con la API de Kaggle
    api = KaggleApi()
    api.authenticate()

    # Descargamos los datos
    print(f'Descargando dataset {dataset}...')
    os.system(f'kaggle datasets download {dataset} --force')
    
    # Obtenemos el autor y el nombre del dataset
    AUTHOR = dataset.split("/")[0]
    DATASET_NAME = dataset.split("/")[1]

    # Copiamos el ZIP descargado a la carpeta correspondiente
    shutil.move(f'{DATASET_NAME}.zip', os.path.join(path, f'{DATASET_NAME}.zip'))
    
    # Obtenemos el zip descargado
    ZIP_PATH = os.path.join(path, f'{DATASET_NAME}.zip')

    # Descomprimimos el ZIP
    print(f'Descomprimiendo el dataset {DATASET_NAME}...')
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip:
        zip.extractall(path)

    # Borramos el ZIP descargado
    os.remove(ZIP_PATH)
    print(f'El dataset {dataset} se ha descargado correctamente')


def create_kaggle_file(username, key) -> None:
    # Obtenemos la ruta de kaggle
    KAGGLE_PATH = os.path.expanduser('~/.kaggle')
    
    # Creamos la carpeta kaggle si no existe
    os.makedirs(KAGGLE_PATH, exist_ok=True)

    # Obtenemos la ruta para el archivo JSON de Kaggle
    FILE_PATH = os.path.join(KAGGLE_PATH, 'kaggle.json')

    # Guardamos las credenciales en kaggle.json
    with open(FILE_PATH, 'w') as json_file:
        json.dump({"username": username, "key": key}, json_file)

    print(f'Creado el archivo de credenciales de Kaggle en {FILE_PATH}')

if __name__ == '__main__':
    start_time = time.time()
    
    # Cargamos las variables de entorno
    load_dotenv()
    
    USERNAME = os.getenv('KAGGLE_USERNAME')
    KEY = os.getenv('KAGGLE_API_KEY')
    
    create_kaggle_file(USERNAME, KEY)
    
    # Nombre de los datasets
    DATASET_NAME = os.getenv('DATASET_NAME')
   
    # Rutas de los dataset
    DATASET_PATH = os.getenv('DATASET_PATH')
    
    # Descargamos los datasets
    download_dataset(DATASET_NAME, DATASET_PATH)
    
    end_time = time.time() - start_time
    
    print(f'Todos los datasets se han descargado, tiempo total {end_time} segundos')
    
    

