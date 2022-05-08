import json
import os



def read_file(file_name):
    try:
        with open(f"data/{file_name}", 'r') as myfile:
            data=myfile.read()
        # parse file
        list_of_pokemon = json.loads(data)
        result_dict = {"data": list_of_pokemon}
        return result_dict
    except Exception as e:
        print(e)


def write_pokemon_info(list_of_pokemon, file_name):
    try:
        with open(file_name, 'w') as file:
            json.dump(list_of_pokemon,file,indent=4)
        return True
    except Exception as e:
        print(e)
        return False
