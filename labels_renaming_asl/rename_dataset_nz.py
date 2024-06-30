from rename_dataset_asl import ordenar,create_dictionary_from_path
from pathlib import Path
import os
nz_dataset_path = Path(".\\datasets\\datasets_individuales\\datasets_tar\\nz_dataset")
from PIL import Image

list_items = os.listdir(nz_dataset_path)
letras = ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]
to_folders_diccionary = {letra : [item for item in list_items if item[6].upper() == letra] for letra in letras }

for letra,items in to_folders_diccionary.items():
    try:
        for i,item in enumerate(items):
            #Convertir imágenes presentes a jpg
            '''path = os.path.join(nz_dataset_path,item)
            image = Image.open(os.path.join(nz_dataset_path,item))
            image_name = letra + "_ASL" + str(i) + ".jpg"
            new_path = os.path.join(nz_dataset_path,image_name)
            image.convert("RGB").save(new_path, "JPEG")'''
            #Eliminar imagenes viejas
            os.remove(os.path.join(nz_dataset_path,item))
    except Exception as e:
        print(e)

