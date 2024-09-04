import requests
from config import API_KEY, API_URL


def obtener_clima(city, country):
    url = f"{API_URL}?q={city},{country}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Verificar si el país devuelto por la API coincide con el país ingresado
        pais_api = data["sys"]["country"]

        if pais_api.lower() == country.lower():
            return {
                "ciudad": data["name"],
                "pais": pais_api,
                "temperatura": data["main"]["temp"],
                "condicion": data["weather"][0]["description"],
            }
        else:
            return {
                "error": f"La ciudad '{city}' no pertenece al país '{country}'. Pertenece a '{pais_api}'."
            }

    elif response.status_code == 404:
        return {"error": "Ubicación no encontrada, verifique los datos."}
    else:
        return {"error": "Se produjo un error al obtener los datos."}
