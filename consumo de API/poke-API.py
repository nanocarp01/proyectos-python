#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


def get_pokemons(url='https://pokeapi.co/api/v2/pokemon-form', offset=0):
    args={'offset': offset} if offset else{}
    response = requests.get(url, params=args)
    
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])
        
        if results:
            for pokemon in results:
                name = pokemon['name']
                
                print(name)
           
                
        next = input("¿continuar listando? [Y/N]").lower()
        if next == 'y':
            get_pokemons(offset=offset+20)
# me muestra en una lista de 20 elementos el nombre de los pokemon

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form'
    get_pokemons()
   
    
  #  response = requests.get(url)
    
   # if response.status_code == 200:
    #    payload = response.json()
     #   results = payload.get('results', [])
        
      #  if results:
       #     for pokemon in results:
        #        name = pokemon['name']
         #       print(name)        
