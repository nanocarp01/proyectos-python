#obtener JSON
import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    #creamos diccionario
    args= {'nombre':'Fernando', 'curso':'Python', 'nivel':'intermedio'}
    response = requests.get(url, params=args)
    
    #verificamos como esta construida la url
    #print(response.url)
    
    if response.status_code == 200:
        
        
        response_json = response.json() #diccionario
        origin = response_json['origin']
        print(origin)
        
        response_json=json.loads(response.text)
        origin = response_json['origin']
        print(origin)