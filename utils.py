import json
import csv
from io import StringIO

def formatear_datos(obtener_clima, formato_salida):
    if "error" in obtener_clima:
        return obtener_clima["error"]
    
    main = obtener_clima['main']
    weather = obtener_clima['weather'][0]
    formatted_data = {
        "Temperature": main['temp'],
        "Condition": weather['description'],
    }

    if formato_salida == 'json':
        return json.dumps(formatted_data, indent=4)
    elif formato_salida == 'csv':
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=formatted_data.keys())
        writer.writeheader()
        writer.writerow(formatted_data)
        return output.getvalue()
    elif formato_salida == 'text':
        return f"Temperatura: {formatted_data['Temperature']}°C\nCondicion: {formatted_data['Condition']}"
    else:
        return "Formato no compatible"