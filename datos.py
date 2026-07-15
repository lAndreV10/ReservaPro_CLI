def menu():
    print("==== ReservaPro  CLI ====")
    print("---- Reserva tu espacio ----")
    print("1. Crear nueva cita")
    print("2. Ver citas del día")
    print("3. Cancelar cita")
    print("4. Salir")

def main():
        while True:
            menu()
            opcion=input("Selecciona una opcion: ").strip()
            if opcion == "4":
                print("GRACIAS por usar ReservaPro CLI! Saliendo del sistema :)")
                break
            elif opcion == "1":
                print("\n[Funcionalidad en desarrollo]: Aquí crearemos una nueva reserva.")
            
            elif opcion == "2":
             print("\n[Funcionalidad en desarrollo]: Aquí mostraremos las reservas del día.")
            
            elif opcion == "3":
                print("\n[Funcionalidad en desarrollo]: Aquí cancelaremos una reserva.")
            else:
                print("\nOpción no válida. Por favor, intente de nuevo con un número del 1 al 4.")

            
if __name__ == "__main__":
    main()
