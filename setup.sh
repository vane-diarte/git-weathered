
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación con parámetros predeterminados
python cli.py --city "Asuncion" --country "Paraguay" --format "json"

# Ejecutar pruebas automatizadas
pytest tests/
