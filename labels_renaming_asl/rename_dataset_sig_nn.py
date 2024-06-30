import os
from pathlib import Path
from rename_dataset_asl import create_dictionary_from_path

#Comprobar cantidad de elementos que hay en cada directorio
'''diccionario_dataset = create_dictionary_from_path(".\datasets\ASL_Dataset_Combination")
amount_list = [int(len(diccionario_dataset[key])) for key in diccionario_dataset.keys()]
total_imagenes = sum(amount_list)
print(total_imagenes)'''


def renombrar(route, sign_type):
    diccionario_paths = create_dictionary_from_path(route)
    try:
        for row, (path,lista) in enumerate(diccionario_paths.items()):
            for i,nombre in enumerate(lista):
                old_name = os.path.join(path,nombre)
                new_name = os.path.join(path, path[-1] + str(amount_list[row] + (i + 1)) + sign_type + nombre[-4:].lower())
                os.rename(old_name,new_name)
                
            
    except Exception as e:
        print(e)

'''renombrar(".\datasets\SigNN Character Database","_ASL")'''