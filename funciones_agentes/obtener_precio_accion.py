import requests
from bs4 import BeautifulSoup

def obtener_precio_accion(consulta):
    try:
        # Extraer solo el ticker
        ticker = consulta.replace("precio", "").replace("accion", "").replace("valor", "").strip().upper()

        url = f"https://finance.yahoo.com/quote/{ticker}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        precio = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})
        nombre = soup.find("h1", {"class": "yf-3a2v0c"})

        if not precio:
            return f"No se encontró el precio de {ticker}. Verifica que el ticker sea correcto."

        nombre_texto = nombre.text.strip() if nombre else ticker

        return f"{nombre_texto} [{ticker}]: ${precio.text.strip()} USD"

    except Exception as e:
        return f"Error al obtener el precio: {e}"