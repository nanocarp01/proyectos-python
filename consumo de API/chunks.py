#chunks
#descargar una imagen
import requests
if __name__=='__main__':
    url ='https://i2.wp.com/losmejoresrock.com/wp-content/uploads/2018/07/rata-blanca-1021x550.jpg?fit=1021%2C550&ssl=1'
    
    #realiza la peticion sin descargar el contenido
    response = requests.get(url, stream=True)
    with open('image.jpg', 'wb') as file:
        #descarga el contenido poco a poco
        for chunk in response.iter_content():
            file.write(chunk)
    
    response.close()