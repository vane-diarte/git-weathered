import argparse
from api import obtener_clima
from utils import formatear_datos

def main():
    parser = argparse.ArgumentParser(description="Obten los datos del clima con el nombre de la ciudad y el pais.")
    
    parser.add_argument('--city', required=True, help='Nombre de la ciudad')
    parser.add_argument('--country', required=True, help='Nombre del pais')
    parser.add_argument('--format', choices=['json', 'csv', 'text'], default='text', help='Formato de salida: json, csv, o text')
    
    args = parser.parse_args()
    
    datos_clima = obtener_clima(args.city, args.country)
    formato_salida = formatear_datos(datos_clima, args.format)
    print(formato_salida)

if __name__ == '__main__':
    main()