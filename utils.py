import json
import csv
from io import StringIO

def formatear_datos(obtener_clima, formato_salida):
    if "error" in obtener_clima:
        return obtener_clima["error"]
    
    formatted_data = {
        "City": obtener_clima["ciudad"],
        "Country": obtener_clima["pais"],
        "Temperature": obtener_clima["temperatura"],
        "Condition": obtener_clima["condicion"],
    }

    if formato_salida == "json":
        return json.dumps(formatted_data, indent=4)
    elif formato_salida == "csv":
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=formatted_data.keys())
        writer.writeheader()
        writer.writerow(formatted_data)
        return output.getvalue()
    elif formato_salida == "text":
        return (
            f"Temperatura: {formatted_data['Temperature']}°C\n"
            f"Condición: {formatted_data['Condition']}"
        )
    else:
        return "Formato no compatible"