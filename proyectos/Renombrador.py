import os 

# Ruta de la carpeta con los archivos 
folder_path = "C:/Users/moham/Desktop/renombrar-archivos/archivos_a_renombrar"


# Obtener lista de archivos en esa carpeta
files = os.listdir(folder_path)

files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

print("Archivos Encontrados: ")
print(files)

# Prefijo para los nuevos nombres
new_name_prefix = "archivo"

# Recorre la lista de archivos

for index, filename in enumerate(files, start=-1):
    # Obtener la extensión del archivo, por ejemplo: ".txt"
    extension = os.path.splitext(filename)[1]

    # Crear el nuevo nombre, por ejemolo "archivo_1.txt"
    new_name = f"{new_name_prefix}_{index}{extension}"

    # Ruta completa del archivo original y del nuevo archivo
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)

    # Renombrar el archivo
    os.rename(old_path, new_path)

print("Archivos Renombrados.")