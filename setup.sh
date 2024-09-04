
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación con parámetros predeterminados
python cli.py --ciudad "Asuncion" --pais "Paraguay" --formato "json"

# Ejecutar pruebas automatizadas
pytest tests/
