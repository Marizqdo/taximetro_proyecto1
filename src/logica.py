# src/logica.py

# --------------------------------------------------------------------------------
# Cálculo de tarifas
# --------------------------------------------------------------------------------

def calculate_fare(state, elapsed_time):
    """
    Calcula la tarifa según el estado y el tiempo transcurrido.
    
    state: "stopped" o "moving"
    elapsed_time: tiempo en segundos que se ha pasado en este estado

    Devuelve la tarifa total en euros.
    """

    # Definimos tarifas en €/segundo
    stopped_rate = 0.02 # tarifa por segundo cuando el taxi está parado
    moving_rate = 0.05 # tarifa por segundo cuando el taxi está en movimiento

    # Calculamos la tarifa según el estado
    if state == "stopped":
        fare = elapsed_time * stopped_rate
    elif state == "moving":
        fare = elapsed_time * moving_rate
    else:
        # Si el estado no es válido, la tarifa es O
        fare = 0
    return fare

# --------------------------------------------------------------------------------
# Gestión del viaje
# --------------------------------------------------------------------------------

def start_trip():
    """
    Inicia un viaje del taxímetro.
    
    Devuelve un diccionario con toda la información del viaje:
    - active: si el viaje está activo
    - state: estado actual (stopped o moving)
    - stopped_time: segundos totales parado
    - moving_time: segundos totales en movimiento
    - state_start: momento en que empezó el estado actual
    """
    return {
        "active": True,
        "state": "stopped",       # estado inicial del taxi
        "stopped_time": 0,
        "moving_time": 0,
        "state_start": time.time()
    }


def change_state(trip, new_state):
    """
    Cambia el estado del taxi y actualiza los tiempos acumulados.

    trip: diccionario del viaje actual
    new_state: "stopped" o "moving"

    Pasos:
    - calcular cuánto tiempo ha pasado en el estado actual
    - sumarlo al contador correspondiente (stopped_time / moving_time)
    - actualizar el estado
    - reiniciar el temporizador del estado
    """

    now = time.time()
    elapsed = now - trip["state_start"]

    # Sumar tiempo al estado anterior
    if trip["state"] == "stopped":
        trip["stopped_time"] += elapsed
    else:
        trip["moving_time"] += elapsed

    # Cambiar al nuevo estado
    trip["state"] = new_state
    trip["state_start"] = now

    return trip


def finish_trip(trip):
    """
    Finaliza el viaje actual.

    Pasos:
    - Calcula los segundos finales del estado actual
    - Suma ese tiempo al contador correspondiente
    - Devuelve el viaje actualizado

    El cálculo final de la tarifa se hace fuera, usando calculate_fare().
    """

    now = time.time()
    elapsed = now - trip["state_start"]

    # Sumar tiempo del último estado
    if trip["state"] == "stopped":
        trip["stopped_time"] += elapsed
    else:
        trip["moving_time"] += elapsed

    # Marcar viaje como terminado
    trip["active"] = False

    return trip
