from ast import Try
import imp
from posixpath import split
import requests
from constants import POKE_API
from files_utils import write_pokemon_info, read_file
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger('mon')
logger.setLevel(logging.DEBUG)

def get_next_pokemon(next):
    try:
        r = requests.get(next)
        if r.status_code == 200:
            pokemon_dict = r.json()
            other_next = pokemon_dict.get('next')
            return pokemon_dict['results'], other_next
    except Exception as e:
        logger.error(e)

def get_pokemon_api():
    try:
        list_of_all_pokemon = []
        r = requests.get(POKE_API)
        if r.status_code == 200:
            pokemon_dict = r.json()
            list_of_all_pokemon.append(pokemon_dict['results'])
            next_poke = pokemon_dict.get('next')
            while True:
                if next_poke != None:
                    result_pokemon, next_poke = get_next_pokemon(next_poke)
                    list_of_all_pokemon.append(result_pokemon)
                else:
                    break
            return list_of_all_pokemon
    except Exception as e:
        logger.error(e)

get_pokemon_api()
def vocals_splitter(pokemon_list):
    vocals_list = {"a": [], "e":[], "i":[], "o": [], "u": [], "consonante": []} 
    pokemon_list = [y for x in pokemon_list for y in x] # List comprehesion
    for pk in pokemon_list:
        if pk['name'][0].lower() == "a":
            vocals_list.get('a').append(pk)
        elif pk['name'][0].lower() == "e":
            vocals_list.get('e').append(pk)
        elif pk['name'][0].lower() == "i":
            vocals_list.get('i').append(pk)
        elif pk['name'][0].lower() == "o":
            vocals_list.get('o').append(pk)
        elif pk['name'][0].lower() == "u":
            vocals_list.get('u').append(pk)
        else:
            vocals_list.get("consonante").append(pk)
    return vocals_list

def create_files(pokemon_dict):
    try:
        write_pokemon_info(pokemon_dict.get('a'), 'data/pokea.json')
        write_pokemon_info(pokemon_dict.get('e'), 'data/pokee.json')
        write_pokemon_info(pokemon_dict.get('i'), 'data/pokei.json')
        write_pokemon_info(pokemon_dict.get('o'), 'data/pokeo.json')
        write_pokemon_info(pokemon_dict.get('u'), 'data/pokeu.json')
        write_pokemon_info(pokemon_dict.get('consonante'), 'data/pokec.json')
        logger.info("Files successfully created!")
        return True
    except Exception as e:
        logger.error(e)
        return False

def init_pokemons():
    # TODO: verify if file exists------ 
    pokemones = get_pokemon_api()
    splitted = vocals_splitter(pokemones)
    create_files(splitted)


