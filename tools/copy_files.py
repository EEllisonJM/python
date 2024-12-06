import os
import shutil
from pathlib import Path

def copy_images(source_folder, destination_folder):
    # Crear la carpeta de destino si no existe
    os.makedirs(destination_folder, exist_ok=True)
    
    # Extensiones de imagen válidas
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}

    # Recorrer todos los archivos en la carpeta fuente y subcarpetas
    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in image_extensions:  # Verificar si es una imagen
                dest_path = Path(destination_folder) / file
                
                # Añadir numeración si el archivo ya existe
                counter = 1
                while dest_path.exists():
                    dest_path = Path(destination_folder) / f"{file_path.stem}_{counter}{file_path.suffix}"
                    counter += 1
                
                # Copiar el archivo
                shutil.copy2(str(file_path), str(dest_path))
                print(f"Copiado: {file_path} -> {dest_path}")

import os
import shutil
from pathlib import Path

def move_videos(source_folder, destination_folder):
    # Crear la carpeta de destino si no existe
    os.makedirs(destination_folder, exist_ok=True)
    
    # Extensiones de video válidas
    video_extensions = {".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".mpeg", ".mpg"}

    # Recorrer todos los archivos en la carpeta fuente y subcarpetas
    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in video_extensions:  # Verificar si es un video
                dest_path = Path(destination_folder) / file
                
                # Añadir numeración si el archivo ya existe
                counter = 1
                while dest_path.exists():
                    dest_path = Path(destination_folder) / f"{file_path.stem}_{counter}{file_path.suffix}"
                    counter += 1
                
                # Mover el archivo
                shutil.move(str(file_path), str(dest_path))
                print(f"Movido: {file_path} -> {dest_path}")

import os
import shutil
from pathlib import Path

def move_documents(source_folder, destination_folder):
    # Crear la carpeta de destino si no existe
    os.makedirs(destination_folder, exist_ok=True)
    
    # Extensiones de documentos válidas
    document_extensions = {".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".txt", ".csv", ".ods", ".odt"}

    # Recorrer todos los archivos en la carpeta fuente y subcarpetas
    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix.lower() in document_extensions:  # Verificar si es un documento
                dest_path = Path(destination_folder) / file
                
                # Añadir numeración si el archivo ya existe
                counter = 1
                while dest_path.exists():
                    dest_path = Path(destination_folder) / f"{file_path.stem}_{counter}{file_path.suffix}"
                    counter += 1
                
                # Mover el archivo
                shutil.move(str(file_path), str(dest_path))
                print(f"Movido: {file_path} -> {dest_path}")

# # Uso del script
# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) != 3:
#         print("Uso: python mover_documentos.py <carpeta_origen> <carpeta_destino>")
#     else:
#         source = sys.argv[1]
#         destination = sys.argv[2]
#         move_documents(source, destination)


# # Uso del script
# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) != 3:
#         print("Uso: python mover_videos.py <carpeta_origen> <carpeta_destino>")
#     else:
#         source = sys.argv[1]
#         destination = sys.argv[2]
#         move_videos(source, destination)

# Uso del script
# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) != 3:
#         print("Uso: python copiar_imagenes.py <carpeta_origen> <carpeta_destino>")
#     else:
#         source = sys.argv[1]
#         destination = sys.argv[2]
#         copy_images(source, destination)

# copy_images(r"D:\Respaldo", r"D:\result")
# move_videos(r"D:\Respaldo", r"D:\result")
# move_documents(r"D:\Respaldo", r"D:\result")