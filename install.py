import os
import shutil

# Actualizamos pip
os.system("python -m pip install --upgrade pip")

# Instalamos los requerimientos
os.system("pip install -r requirements.txt")

# Instalamos las dependencias de npm
os.system("npm install")

# Guardamos la ruta absoluta del proyecto
path = os.path.abspath("./")
env_variables ={}

with open(".env", "r") as f:
    for line in f.readlines():
        key, value = line.split('=')
        env_variables[key] = value

if "PROJECT_PATH" not in env_variables:
    with open(".env", "w") as f:
        for key in env_variables:
            f.write(f'{key}={env_variables[key]}')
        f.write(f'PROJECT_PATH={path}\n')