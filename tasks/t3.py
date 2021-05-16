import requests
import time

class PokeWeight:
    def __init__ (self, pokemonType):
        self.pokemonType = pokemonType
        self.typeUrl = 'https://pokeapi.co/api/v2/type/' + pokemonType
        self.species = []
        self.minWeigth = None
        self.maxWeigth = None

    def iterative_loader(self):
        resp = requests.get(self.typeUrl).json()

        # almacenamos las url de cada pokemon. Solo se consideran aquellos con un id menor a 151 (1ra gen)
        self.species = [element['pokemon']['url'] for element in resp['pokemon'] if int(element['pokemon']['url'].split('/')[-2]) <= 151]
        self.get_weigth()

        # print("El peso maximo y minimo de los pokemon tipo {} son: [{}, {}] respectivamente".format(self.pokemonType, self.maxWeigth, self.minWeigth))
        return [self.maxWeigth, self.minWeigth]

    def get_weigth(self):
        for element in self.species:
            resp = requests.get(element).json()

            # comparamos el peso de cada pokemon con los valores actuales
            self.search_matches(resp['weight'])

        return self.species

    def search_matches(self, pokeData):
        # seteamos nuestro primer peso maximo y minimo
        if self.maxWeigth is None:
            self.maxWeigth = pokeData
            self.minWeigth = pokeData
            return False

        # comparamos el valuor de peso maximo y minimo con el de este pokemon
        if pokeData > self.maxWeigth :
            self.maxWeigth = pokeData

        if pokeData < self.minWeigth:
            self.minWeigth = pokeData

        return True


if __name__ == "__main__":
    pokeWeigth = PokeWeight('fighting')
    start_time = time.time()
    print(pokeWeigth.iterative_loader())
    print("--- {} seconds ---".format(time.time() - start_time))
