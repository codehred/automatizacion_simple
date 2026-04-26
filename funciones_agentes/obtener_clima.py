import requests

def obtener_clima(consulta):
    try:
        # Extraer solo el nombre de la ciudad
        ciudad_consulta = consulta.replace("clima", "").replace("temperatura", "").strip()

        # Primero obtenemos las coordenadas de la ciudad
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={ciudad_consulta}&count=1&language=es"
        geo_response = requests.get(geo_url).json()

        if not geo_response.get("results"):
            return f"No se encontró la ciudad: {ciudad_consulta}"

        ciudad = geo_response["results"][0]
        nombre = ciudad["name"]
        lat = ciudad["latitude"]
        lon = ciudad["longitude"]

        # Luego obtenemos el clima con las coordenadas
        clima_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        clima_response = requests.get(clima_url).json()
        clima = clima_response["current_weather"]

        temperatura = clima["temperature"]
        viento = clima["windspeed"]

        return f"{nombre}: {temperatura}°C, viento {viento} km/h"

    except Exception as e:
        return f"Error al obtener el clima: {e}"