#metodo PUT & DELETE
import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/deqlete'
    #creamos diccionario
    payload= {'nombre':'Fernando', 'curso':'Python', 'nivel':'intermedio'}
    headers = {'Content-Type' : 'application/json', 'access-token': '12345' }
    
    response = requests.delete(url, data=json.dumps(payload), headers=headers)#forma serializada se guarda el diccionario en data
 
    
    if response.status_code == 200:    
        #print(response.content)
        headers_response= response.headers #diccionario
        server = headers_response['server']
        print(server)