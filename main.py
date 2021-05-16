from tasks.t1 import PokeList
from tasks.t2 import PokeSpecies
from tasks.t3 import PokeWeight

def run_t1(method = "iterative"):
    if method == "iterative":
        pokeList = PokeList()
        return pokeList.iterative_loader()
    elif method == "recursive":
        pokeList = PokeList()
        return pokeList.recursive_loader()
    else:
        pokeList = PokeList()
        recursive = pokeList.iterative_loader()
        pokeList.reset_pokelist()
        iterative = pokeList.recursive_loader()
        return [recursive, iterative]

def run_t2(pokemon = 'raichu'):
    pokeSpecies = PokeSpecies(pokemon)
    return pokeSpecies.iterative_loader()

def run_t3(pokeType = 'fighting'):
    pokeWeigth = PokeWeight(pokeType)
    return pokeWeigth.iterative_loader()



if __name__ == "__main__":
    print('T1')
    print(run_t1())
    # print(run_t1('recursive'))
    # print(run_t1('both'))

    print('T2')
    print(run_t2())
    # print(run_t2('charizard'))

    print('T3')
    print(run_t3())
    # print(run_t3('flying'))

