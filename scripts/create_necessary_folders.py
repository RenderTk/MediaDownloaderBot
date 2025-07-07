import os

# Obtener el directorio raíz un nivel por encima del directorio actual del script
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir)

# Directorios a crear
directories = [
    "media/",
]

# Iterar sobre los directorios y crearlos si no existen
for dir_path in directories:
    full_path = os.path.join(base_dir, dir_path)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        print(f"Creado el directorio: {full_path}")
    else:
        print(f"El directorio ya existe: {full_path}")
