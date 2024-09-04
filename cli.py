import argparse
from api import obtener_clima
from utils import formatear_datos


def main():
    parser = argparse.ArgumentParser(
        prog="Clima",
        description="Obten los datos del clima con el nombre de la ciudad y el pais.",
    )

    parser.add_argument("-c", "--ciudad", required=True, help="Nombre de la ciudad")
    parser.add_argument("-p", "--pais", required=True, help="Nombre del pais")
    parser.add_argument(
        "-f",
        "--formato",
        choices=["json", "csv", "text"],
        default="text",
        help="Formato de salida: json, csv, o text",
    )

    args = parser.parse_args()

    datos_clima = obtener_clima(args.ciudad, args.pais)
    formato_salida = formatear_datos(datos_clima, args.formato)
    print(formato_salida)


if __name__ == "__main__":
    main()
