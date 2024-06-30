import os
from rename_dataset_asl import ordenar,create_dictionary_from_path,list_sizes

'''print(list_sizes)
suma = sum(list_sizes)
print(suma)'''

def renombrar(route, sign_type):
    diccionario_paths = create_dictionary_from_path(route)
    try:
        for path,lista in diccionario_paths.items():
            for i,nombre in enumerate(lista):
                old_name = os.path.join(path,nombre)
                new_name = os.path.join(path, path[-1] + str(3000 + (i + 1)) + sign_type + nombre[-4:].lower())
                os.rename(old_name,new_name)
            pass
    except Exception as e:
        print(e)

renombrar(".\datasets\DataSet Signos","_ASL")
