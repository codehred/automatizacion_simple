from funciones_agentes.obtener_clima import obtener_clima
from funciones_agentes.obtener_precio_accion import obtener_precio_accion
from utils.sanitizar import sanitizar


def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return obtener_precio_accion
    return None


print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")
while True:
    user_input = sanitizar(input("---> "))
    funcion_agente = procesar_input(user_input)
    if funcion_agente is None:
        print("No entendí tu solicitud. Intenta nuevamente.")
    else:
        respuesta = funcion_agente(user_input)
        print(f">>> {respuesta}")