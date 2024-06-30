import os
from rename_dataset_asl import ordenar,create_dictionary_from_path
import threading
from pathlib import Path

path_names = [Path(".\\datasets\\datasets_individuales\\datasets_tar\\dataset5\\" + p) for p in os.listdir(".\datasets\datasets_individuales\datasets_tar\dataset5")]

#Asignar paths respectivos
diccionario_paths = {p_name: os.listdir(p_name) for p_name in path_names}

#renombrar diccionarios

#Renombrar paths
def renombrar_paths(diccionario_paths):
    for path,array in diccionario_paths.items():
        for letter in array:
            upper_case = letter.upper()
            joned_path = os.path.join(path,upper_case)
            older_paths = os.path.join(path,letter)
            os.rename(older_paths,joned_path)

def eliminar_imagenes(diccionario):
    try:
        for path,lista in diccionario.items():
            for nom_archivo in lista:
                if "depth" in nom_archivo:
                    f_path = os.path.join(path,nom_archivo)
                    os.remove(f_path)
    except Exception as e:
        print(e)

#renombrar_paths(diccionario_paths)

'''thread1 = threading.Thread(target=lambda: eliminar_imagenes(diccionario_C))
thread2 = threading.Thread(target=lambda: eliminar_imagenes(diccionario_D))

thread1.start()
thread2.start()

thread1.join()
thread2.join()'''
#eliminar_imagenes(diccionario_E)

#Ver tamaño de dataset signos
paths_in_dataset = [os.path.join(".\datasets\ASL_Dataset_Combination",letter) for letter in os.listdir(".\datasets\ASL_Dataset_Combination")]
size_watch = [int(len(os.listdir(path))) for path in paths_in_dataset]
print(size_watch)

def renombrar(route, sign_type, j):
    diccionario_paths = create_dictionary_from_path(route)
    try:
        for row, (path,lista) in enumerate(diccionario_paths.items()):
            for i,nombre in enumerate(lista):
                old_name = os.path.join(path,nombre)
                new_name = os.path.join(path, path[-1] + str(i + j + 1) + sign_type + nombre[-4:].lower())
                os.rename(old_name,new_name)
                
            
    except Exception as e:
        print(e)

for i,p in enumerate(path_names):
    renombrar(p,"_ASL",i)
