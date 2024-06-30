import os
from pathlib import Path
import re
#Obtener path de los directorios dentro del train

#Algoritmo de ordenacion
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        left_value = int(re.findall(r'\d+', left[i])[0])
        right_value = int(re.findall(r'\d+', right[j])[0])
        
        if left_value < right_value:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

def ordenar(paths):
    return merge_sort(paths)


def create_dictionary_from_path(path):
    dir_path = Path(path)
    #Por preferencia, crearé un diccionario de los path de las imagenes. El key sera el path general y los values seran las listas que contendran los nombres de los archivos
    folders = [folder for folder in os.listdir(dir_path)]
    #Join paths 
    new_paths = [os.path.join(dir_path,name) for name in folders]
    diccionario_paths = {}
    #Crear diccionarios de los paths y los archivos dentro
    for path_name in new_paths:
        file_names = []
        for path in os.listdir(path_name):
            if os.path.isfile(os.path.join(path_name,path)):
                file_names.append(path)
        sorted_paths = ordenar(file_names)
        diccionario_paths[path_name] = sorted_paths
    return diccionario_paths


'''#Ejemplo que usare para renombrar
#Se coge una lista de ejemplo
lista_ejemplo = diccionario_paths[new_paths[0]]
print(len(lista_ejemplo))
letra_ejemplo = lista_ejemplo[2][:-4]
#agregar_diferenciador
letra_ejemplo = letra_ejemplo + '_ASL'
print(letra_ejemplo)
print(lista_ejemplo)'''

#Empezar a renombrar
def renombrar(route, sign_type):
    diccionario_paths = create_dictionary_from_path(route)
    try:
        for path,lista in diccionario_paths.items():
            for nombre in lista:
                old_name = os.path.join(path,nombre)
                new_name = os.path.join(path, nombre[:-4] + sign_type + nombre[-4:])
                os.rename(old_name,new_name)
            pass
    except Exception as e:
        print(e)

'''diccionario_revisar = create_dictionary_from_path(".\\datasets\\asl_alphabet_train\\asl_alphabet_train")
list_sizes = [int(len(diccionario_revisar[key])) for key in diccionario_revisar.keys()]'''



    