import sys
import os

# Agrega el directorio raíz del proyecto a sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api import obtener_clima

def test_obtener_clima():
    # Caso exitoso
    result = obtener_clima("Buenos Aires", "Ar")
    assert result is not None
    assert "ciudad" in result
    assert "pais" in result
    assert "temperatura" in result
    assert "condicion" in result

    # Caso de error (ciudad inexistente)
    result_error = obtener_clima("CiudadInexistente", "PaisInexistente")
    assert "error" in result_error
