# src/logica.py

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