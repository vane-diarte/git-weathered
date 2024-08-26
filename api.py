#funcion que solicita los datos a la api del clima
import requests
from config import API_KEY, API_URL

def obtener_clima(city, country):
    url = f"{API_URL}?q={city},{country}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return {"error": "Ubicacion no encontrada, verifique los datos."}
    else:
        return {"error": "Se produjo un error al obtener los datos."}