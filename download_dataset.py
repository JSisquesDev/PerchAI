from dotenv import find_dotenv, load_dotenv
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
    os.system(f'kaggle datasets download "{dataset}" --force')
    
    # Obtenemos el autor y el nombre del dataset
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
    os.remove(os.path.join(path, "EfficientNetB0-525-(224 X 224)- 98.97.h5"))
    
    print(f'El dataset {dataset} se ha descargado correctamente')


def create_kaggle_file(username, key) -> None:
    # Obtenemos la ruta de kaggle
    KAGGLE_PATH = os.path.expanduser(f'~{os.sep}.kaggle')
    
    if not os.path.exists(KAGGLE_PATH):
        # Creamos la carpeta kaggle si no existe
        os.makedirs(KAGGLE_PATH, exist_ok=True)

    # Obtenemos la ruta para el archivo JSON de Kaggle
    FILE_PATH = os.path.join(KAGGLE_PATH, 'kaggle.json')
    print(FILE_PATH)

    # Guardamos las credenciales en kaggle.json
    with open(FILE_PATH, 'w') as json_file:
        json.dump({"username": username, "key": key}, json_file)

    print(f'Creado el archivo de credenciales de Kaggle en {FILE_PATH}')

if __name__ == '__main__':
    start_time = time.time()
    
    # Cargamos las variables de entorno
    load_dotenv(find_dotenv())
    print("x")
    
    KAGGLE_USERNAME = os.getenv('KAGGLE_USERNAME')
    KAGGLE_KEY = os.getenv('KAGGLE_KEY')
    
    print(KAGGLE_USERNAME)
    print(KAGGLE_KEY)
    
    create_kaggle_file(KAGGLE_USERNAME, KAGGLE_KEY)
    
    # Nombre de los datasets
    DATASET_NAME = os.getenv('DATASET_NAME')
   
    # Rutas de los dataset
    DATASET_PATH = os.getenv('DATASET_PATH')
    
    # Descargamos los datasets
    download_dataset(DATASET_NAME, DATASET_PATH)
    
    end_time = time.time() - start_time
    
    print(f'Todos los datasets se han descargado, tiempo total {end_time} segundos')
    
    

