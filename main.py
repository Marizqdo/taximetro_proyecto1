from logica import calculate_fare, start_trip, change_state, finish_trip

def taximeter():
    """
    Función para manejar y mostrar las opciones del taxímetro
    """
    print("Welcome to the F5 taximeter!")  # Bienvenida
    print("Available commands:")
    print("   start - start a trip")
    print("   stop - stop the taxi")
    print("   move - move the taxi")
    print("   finish - finish the trip")
    print("   exit - exit the program\n")
    
    trip_activate = False  # Indica si hay un viaje activo
    trip = None            # Diccionario que guarda info del viaje actual
    
    while True:
        command = input("> ").strip().lower()  # Lee comando del usuario
        
        if command == "start":
            if trip_activate:
                print("Error: A trip is already in progress")
                continue
            trip = start_trip()  # Inicializa viaje
            trip_activate = True
            print("Trip started. Initial state: 'stopped'")
        
        elif command in ("stop", "move"):
            if not trip_activate:
                print("Error: No active trip, please start first")
                continue
            new_state = "stopped" if command == "stop" else "moving"
            trip = change_state(trip, new_state)
            print(f"State changed to '{new_state}'")
        
        elif command == "finish":
            if not trip_activate:
                print("Error: No active trip to finish")
                continue
            
            trip = finish_trip(trip)  # Finaliza el viaje
            
            # Calcula tarifa total usando la función de logica.py
            total_fare = calculate_fare("stopped", trip["stopped_time"]) + \
                         calculate_fare("moving", trip["moving_time"])
            
            # Muestra resumen del viaje
            print("\n--- Trip Summary ---")
            print(f"Stopped time: {trip['stopped_time']:.1f} seconds")
            print(f"Moving time: {trip['moving_time']:.1f} seconds")
            print(f"Total fare: €{total_fare:.2f}")
            print("---------------------\n")
            
            trip_activate = False
            trip = None
        
        elif command == "exit":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Unknown command. Use: start, stop, move, finish, or exit")


if __name__ == "__main__":
    taximeter()  # Ejecuta la CLI del taxímetro
