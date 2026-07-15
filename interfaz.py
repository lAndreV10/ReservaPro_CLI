from negocio import valFecha, valHora

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
                print("\nGRACIAS por usar ReservaPro CLI! Saliendo del sistema :)")
                break
            elif opcion == "1":
                print("--- Nueva Reserva ---")
                
                cliente = input("Nombre del cliente: ").strip()
                servicio = input("Servicio a realizar: ").strip()

                while True:
                    fecha = input("Fecha de la cita (AAAA-MM-DD): ").strip()
                    if valFecha(fecha):
                        break  
                    else:
                     print("Error: La fecha no es válida o no tiene el formato AAAA-MM-DD. Intente de nuevo.")
            
                while True:
                    hora = input("Hora de la cita (HH:MM - formato 24h): ").strip()
                    if valHora(hora):
                        break
                    print("Error: La hora no es válida o no tiene el formato HH:MM (00:00 a 23:59). Intente de nuevo.")

                print("\n[CONFIRMACIÓN DE CITA]: \n") 
                print(f"[NOMBRE] ---> {cliente}")          
                print(f"[SERVICIO] ---> {servicio}")
                print(f"[fecha] ---> {fecha}")
                print(f"[hora] ---> {hora}")

                input("\nPresione ENTER para regresar al menu principal...")

            elif opcion == "2":
             print("\n[Funcionalidad en desarrollo]: Aquí mostraremos las reservas del día.")
            
            elif opcion == "3":
                print("\n[Funcionalidad en desarrollo]: Aquí cancelaremos una reserva.")
            else:
                print("\nOpción no válida. Por favor, intente de nuevo con un número del 1 al 4.")

            
if __name__ == "__main__":
    main()
