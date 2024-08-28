import sys
import os

# Agrega el directorio raíz del proyecto a sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import obtener_clima

def test_obtener_clima():
    result = obtener_clima("Asuncion", "Paraguay")
    assert result is not None
    assert "main" in result  # Verifica que la respuesta contiene datos esperados
