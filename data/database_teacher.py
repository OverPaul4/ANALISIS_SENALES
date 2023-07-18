import requests

# Ruta del repositorio
url ='https://raw.githubusercontent.com/JulianDPastrana/signal_analysis/main/seniales_sep_p2.py'

# Se realiza la solicitud para copiar el archivo en el repositorio
r = requests.get(url)

# El archivo de la ruta es leido
with open('seniales_sep.py', 'w') as f:  # Se copia el contenido del repositorio en un archivo nuevo
    # en la ruta actual
    f.write(r.text)
