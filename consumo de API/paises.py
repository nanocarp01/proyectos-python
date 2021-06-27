import requests  #Importamos la librería requests

print("SOLICITANDO INFORMACION DE INTERNET")
print("espere....") 
url = 'https://restcountries.eu/rest/v2/all' #configuramos la url

#solicitamos la información y guardamos la respuesta en data.
data = requests.get(url) 


data = data.json() #convertimos la respuesta en dic

pais = input("Ingrese pais: ")
for element in data: #iteramos sobre data
    if element['name'] == pais: 
        #Accedemos a sus valores
        #print("Pais: ", element['name']) 
        print("Capital: ", element['capital'])
        print("Region: ", element['region'])
        print("Poblacion: ", element['population'])
        print("----------")

        