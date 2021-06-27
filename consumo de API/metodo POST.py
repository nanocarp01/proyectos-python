#metodo POST
import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    #creamos diccionario
    payload= {'nombre':'Fernando', 'curso':'Python', 'nivel':'intermedio'}
    response = requests.post(url, data=json.dumps(payload))#forma serializada se guarda el diccionario en data
    #response = requests.post(url, json=payload) este es otro metodo
    
    #verificamos como esta construida la url
    #print(response.url)
    
    if response.status_code == 200:    
        print(response.content)