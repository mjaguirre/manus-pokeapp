import requests
import time

class PokeSpecies:
    def __init__ (self, pokemonName):
        self.pokemonName = pokemonName
        self.speciesUrl = 'https://pokeapi.co/api/v2/pokemon-species/' + pokemonName
        self.eggGroupsUrls = []
        self.species = {}
        self.matches = []
        self.count = 0

    def iterative_loader(self):
        # primero, encontramos los egg_gropus correspondientes al pokemon
        resp = requests.get(self.speciesUrl).json()
        self.eggGroupsUrls = [element['url'] for element in resp['egg_groups']]

        # Luego, almacenamos los nombres de cada uno de los pokemons de cada egg-group en una lista dentro de un diccionario
        self.get_species()

        # Finalmente, unimos las listas de cada entrada del diccionario, eliminando los repetidos
        self.count = self.search_matches()

        # print("La cantidad de especies que pueden procrear {} son: {}, provenientes de {} egg-gropus".format(self.pokemonName, self.count, len(self.eggGroupsUrls)))
        return self.count

    def get_species(self):
        for element in self.eggGroupsUrls:
            resp = requests.get(element).json()

            # El objeto contiene tambien una URL. Solo almacenamos los nombres
            self.species[resp['name']] = [pokemon['name'] for pokemon in resp['pokemon_species']]

        return self.species

    def search_matches(self):
        for key in self.species:
            # el siguiente código nos permite realizar la union de la lista actual con la siguiente del diccionario
            # set nos permite eliminar los repetidos de dicha union
            self.matches = list(set().union(self.matches, self.species[key]))
        return len(self.matches)


if __name__ == "__main__":
    pokeSpecies = PokeSpecies('raichu')
    start_time = time.time()
    print(pokeSpecies.iterative_loader())
    print("--- {} seconds ---".format(time.time() - start_time))
