import requests
import time

class PokeList:
    def __init__ (self):
        self.currentUrl = None
        self.nextUrl = 'https://pokeapi.co/api/v2/pokemon'
        self.count = 0

    def recursive_loader(self):
        # Esta es una busqueda recursiva para encontrar los nombres de pokemos que coinsiden con lo estipulado.
        # Es necesario destacar que la complejidad es mayor a la version iterativa.
        if not self.nextUrl:
            # print("La cantidad de pokemones con AT y dos A en su nombre son: {}".format(self.count))
            return self.count

        self.currentUrl = self.nextUrl
        resp = requests.get(self.currentUrl).json()
        self.nextUrl = resp['next']
        self.poke_counter(resp['results'])

        return self.recursive_loader()

    def iterative_loader(self):
        self.currentUrl = self.nextUrl

        # Realizamos la primera iteración para ir a buscar los primeros 20 pokemons y tambien conocer el total de pokemons
        resp = requests.get(self.currentUrl).json()

        # Luego contamos los nombres que coinciden con lo requerido
        self.poke_counter(resp['results'])

        # Repetimos el proceso, pero esta vez realizamos una request para ir a buscar la lista de todos los pokemons faltantes, menos los 20 primeros
        resp = requests.get(self.currentUrl + '?limit={}&offset=20'.format(resp['count'])).json()
        self.poke_counter(resp['results'])

        # print("La cantidad de pokemones con AT y dos A en su nombre son: {}".format(self.count))
        return self.count

    def reset_pokelist(self):
        # Seteamos los valores iniciales para volver a realizar la operación
        self.currentUrl = None
        self.nextUrl = 'https://pokeapi.co/api/v2/pokemon'
        self.count = 0

        return True

    def poke_counter(self, data):

        # revisamos la lista de popkemons y buscamos aquellos nombres que coinciden con lo estipulado
        for element in data:
            if 'at' in element['name'] and element['name'].count('a') == 2:
                self.count += 1

        return self.count

if __name__ == "__main__":
    pokeList = PokeList()
    start_time = time.time()
    print(pokeList.recursive_loader())
    print("--- {} seconds ---".format(time.time() - start_time))
    pokeList.reset_pokelist()
    start_time = time.time()
    print(pokeList.iterative_loader())
    print("--- {} seconds ---".format(time.time() - start_time))