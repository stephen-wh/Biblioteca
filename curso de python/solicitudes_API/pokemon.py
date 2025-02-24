import requests

def get_pokemons(url, offset=0):
    while True:
        arg = { 'offset': offset } if offset else{}
        response = requests.get(url, params=arg)
        
        if response.status_code == 200:
            request_json = response.json()
            pokemones = request_json.get('results', [])

            if pokemones:
                for index, pokemon in enumerate(pokemones):
                    name = pokemon["name"]
                    print( str(index+1+offset) +" "+name)

        siguiente = input("¿Quieres continuar listando? [Y/N]").lower()
        if siguiente == "y":
            get_pokemons(url=url,offset=offset+20)

url = 'https://pokeapi.co/api/v2/pokemon'
get_pokemons(url=url)