from logica import calculate_fare
import time # Importa el módulo 'time' para medir duraciones

def calculate_fare(seconds_stopped, seconds_moving):
    """
    Función para calcular la tarifa total en euros
    stopped: 0.02 €/s
    moving: 0.05 €/s
    """
    
    # Calcula la tarifa sumando el coste por tiempo detenido y en movimiento
    fare = seconds_stopped * 0.02 + seconds_moving * 0.05
    print(f"Este es el total:{fare}") # Muestra el total del cálculo
    return fare # Devuelve el total

def taximeter():
    """
    Función para manejar y mostrar las opciones del taxímetro
    """
    print("Welcome to the F5 taximeter!") # Bienvenida 
    print("Available commands: ")   # Menú
    print("   start - start a trip")
    print("   stop - stop the taxi")
    print("   move - move the taxi")
    print("   finish -finish the trip")
    print("   exit -exit the program\n")
    
    # Variables de control de viaje
    trip_activate = False # Indica si hay un viaje en curso
    start_time = 0 # Momento de inicio del viaje
    stopped_time = 0 # Tiempo acumulado detenido
    moving_time = 0 #Tiempo acumulado en movimiento
    state = None # Estado actual: "stopped" o "moving"
    state_start_time = 0 # Momento en que comenzó el estado actual
    
    while True:
        command = input("> ").strip().lower() # Lee el comando del usuario
        if command == "start":
            if trip_activate:
                print("Error: A trip is already in progress") # No se puede iniciar otro viaje
                continue

            # Inicia un nuevo viaje
            trip_activate = True
            start_time = time.time() # Guarda el tiempo de inicio
            stopped_time = 0 # Reinicia el tiempo detenido
            moving_time = 0 # Reinicia el tiempo en movimiento
            state = "stopped" # Estado inicial del viaje
            state_start_time = time.time() # Momento de inicio del estado
            print("Trip started. Initial state: 'stopped'")
            
        elif command in ("stop", "move"):
            if not trip_activate:
                print("Error: No active trip, please start first") # No hay viaje activo
                continue

            # Calcula la duración en el estado anterior
            duration = time.time() - state_start_time
            
            if state == "stopped":
                stopped_time += duration # Acumula tiempo detenido
                
            else:
                moving_time += duration # Acumula tiempo en movimiento

            # Cambia el estado actual según el comando
            state = "stopped" if command == "stop" else "moving"
            state_start_time = time.time() # Reinicia el tiempo del nuevo estado
            print(f"State changed to '{state}'. ")
            
        elif command == "finish":
            if not trip_activate:
                print("Error: No active trip to finish") # No hay viaje activo que finalizar
                continue
            
            # Calcula el tiempo en el estado final antes de terminar
            duration = time.time() - state_start_time
            if state == "stopped":
                stopped_time += duration
                
            else:
                moving_time += duration

            # Calcula la tarifa total    
            total_fare = calculate_fare(stopped_time, moving_time)

            # Muestra un resumen del viaje
            print("\n--- Trip Summary ---")
            print(f"Stopped time: {stopped_time:.1f} seconds")
            print(f"Moving time: {moving_time:.1f} seconds")
            print(f"Total fare: €{total_fare:.2f}")
            print("---------------------\n")
            
            # Reinicia varables para permitir un nuevo viaje
            trip_activate = False
            state = None
            
        elif command =="exit":
            print("Exiting the program. Good bye!") # Sale del programa. Despediada
            break
        
        else:
            print("Unknown command. Use: start, stop, move, finish, or exit") # Comando desconocido

                  
if __name__ == "__main__":
    taximeter() # Ejecuta el taxímetro cuando se corre el script