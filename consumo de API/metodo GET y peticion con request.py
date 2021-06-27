#metodo GET y peticion con request
import requests

if __name__ == '__main__':
    url = 'https://ghibliapi.herokuapp.com/films'
    response = requests.get(url)
    
    print(response)
    
    if response.status_code == 200:
        content = response.content
        #generamos el archivo google.html con el contenido que nos envia el servidor, wb escritura binaria
        file = open('2.html', 'wb')
        file.write(content)
        file.close()