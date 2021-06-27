#ARGS
import requests

if __name__ == '__main__':
    url = 'https://httpbin.org/get'
    #creamos diccionario
    args= {'nombre':'Fernando', 'curso':'Python', 'nivel':'intermedio'}
    response = requests.get(url, params=args)
    
    #verificamos como esta construida la url
    print(response.url)
    
    if response.status_code == 200:
        
        content = response.content
        print(content)
        #generamos el archivo google.html con el contenido que nos envia el servidor, wb escritura binaria
        #file = open('httbin.html', 'wb')
        #file.write(content)
        #file.close()