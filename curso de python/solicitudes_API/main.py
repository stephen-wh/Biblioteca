import requests
import json

#podemos tambien extraer imagenes
if __name__ == '__main__':
    url = 'https://nupec.com/wp-content/uploads/2021/02/Captura-de-pantalla-2021-02-08-a-las-13.59.48.png'

    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open('image.png', 'wb') as file:
            for chunk in response.iter_content():
                file.write(chunk)
    response.close()

#podemos enviar parametros para gestionar los parametrso con argumemto
if __name__ == '__main2__':
    url = 'http://httpbin.org/get'
    args = { "find" : "diccionarios" }
    response = requests.get(url, params=args)
    if response.status_code == 200:
        response_json = json.loads(response.text)
        origin = response_json["origin"]
        print(origin)
#podemos hacer peticoines a paginas web
if __name__ == '__main1__':
    url = 'https://www.google.com.mx/'
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        file = open("google.html", "wb")
        file.write(content)
        print(response.content)
    print(response)