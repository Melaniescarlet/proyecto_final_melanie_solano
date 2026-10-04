# ===========================================
# PROYECTO FINAL: SISTAMA DE RESERVAS CINEMAX
# ===========================================

# Guardo toda la cartelera de la semana 
# Cada dia tiene una lista con las 5 peliculas, sus salas, horarios y formatos.
cartelera = {
    "Lunes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 1, "horario": "2:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 2, "horario": "4:30 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 3, "horario": "6:00 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 4, "horario": "5:30 pm", "formato": "4DX"},
        {"pelicula": "El Final", "sala": 5, "horario": "8:00 pm", "formato": "CXC"}
    ],
    "Martes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 3, "horario": "5:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 1, "horario": "7:00 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 2, "horario": "3:00 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 5, "horario": "6:30 pm", "formato": "4DX"},
        {"pelicula": "El Final", "sala": 4, "horario": "9:00 pm", "formato": "Normal"}
    ],
    "Miércoles": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 4, "horario": "4:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 5, "horario": "2:30 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 1, "horario": "7:30 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 2, "horario": "5:00 pm", "formato": "4DX"},
        {"pelicula": "El Final", "sala": 3, "horario": "8:30 pm", "formato": "4DX"}
    ],
    "Jueves": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 2, "horario": "6:30 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 3, "horario": "3:30 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 4, "horario": "8:00 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 1, "horario": "4:30 pm", "formato": "Normal"},
        {"pelicula": "El Final", "sala": 5, "horario": "7:00 pm", "formato": "CXC"}
    ],
    "Viernes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 5, "horario": "8:30 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 4, "horario": "6:00 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 5, "horario": "8:30 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 3, "horario": "5:00 pm", "formato": "4DX"},
        {"pelicula": "El Final", "sala": 2, "horario": "9:30 pm", "formato": "Normal"}
    ],
    "Sábado": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 1, "horario": "3:00 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 2, "horario": "5:30 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 5, "horario": "8:30 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 4, "horario": "4:30 pm", "formato": "4DX"},
        {"pelicula": "El Final", "sala": 3, "horario": "7:30 pm", "formato": "CXC"}
    ],
    "Domingo": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 3, "horario": "2:30 pm", "formato": "Normal"},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 5, "horario": "5:00 pm", "formato": "3D"},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 2, "horario": "7:00 pm", "formato": "Normal"},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 1, "horario": "8:30 pm", "formato": "4DX"},
        {"pelicula": "El Final", "sala": 4, "horario": "4:00 pm", "formato": "Normal"}
    ]
}

# Configuramos el mapa de la sala (5 filas x 6 colomnas = 30 asientos)
FILAS = [ "A", "B", "C", "D", "E"]
COLUMNAS = [1, 2, 3, 4, 5, 6]

# Guardo los mapas de asientos 
asientos_funciones = {}

# Creamos una matriz inicial con todos los asientos libres
def crear_matriz_asientos():
    return[["." for _ in range(6)] for _ in range(5)]

for dia, lista_funciones in cartelera.items():
    for funcion in lista_funciones:
        clave = f"{dia}-{funcion['sala']}-{funcion['horario']}"
        asientos_funciones[clave] = crear_matriz_asientos()
    
def buscar_funcion(dia, sala, horario):
    """Busca una funcion especifica en el diccionario cartelera"""
    if dia in cartelera:
        for f in cartelera[dia]:
            if f["sala"] == sala and f["horario"].lower() == horario.lower():
                return f
    return None

def ver_cartelera_dia():
    # Muestra las peluculas programadas para el dia consultado
    """4.1 ver cartelera de un dia"""
    print("\n" + "="*45)
    print("         CARTELERA POR DIA")
    print("="*45)
    dia = input("Ingrese el dia de la semana (Ej. Lunes, Martes): ").strip().capitalize()
    
    if dia in cartelera:
        print(f"\n--- Funciones para el dia {dia} ---")
        for f in cartelera[dia]:
            print(f"pelicula: {f['pelicula']}")
            print(f"    Sala: {f['sala']} | horario: {f['horario']} | Formato: {f['formato']}")
            print("-" * 40)
    else:
        print("\nDia invalido. Por favor escriba un dia valido de Lunes a Domingo.")

def mostrar_asientos_pantalla():
    # Imprime en la consola el mapa grafico de los asientos libres u ocupados
    """4.2 Mostrar asintos de una funcion"""
    print("\n" + "="*45)
    print("       MAPA DE ASIENTOS DE LA SALA")
    print("="*45)
    dia = input("Igresa el dia: ").strip().capitalize()

    try:
        sala = int(input("Ingresa el numero de sala (1-5): "))
    except ValueError:
        print("La sala debe ser un numero entero.")
        return

    horario = input("Ingresa el horario (Ej. 2:00 pm, 5:00 pm): ").strip()

    funcion = buscar_funcion(dia, sala, horario)
    if not funcion:
        print("\n no se encontro ninguna funcion que coincida con esos datos.")
        return

    clave = f"{dia}-{sala}-{funcion['horario']}"
    matriz = asientos_funciones[clave]

    print(f"\nPeliculas: {funcion['pelicula']} ({funcion['formato']})")
    print(f"Dia: {dia} | Sala: {sala} | Horario: {funcion['horario']}\n")
    print("      PANTALLA  ")
    print("   1  2  3  4  5  6")

    for idx, FILAS in enumerate(matriz):
        letra_filas = FILAS[idx]
        asientos_str = "   ".join(FILAS)
        print(f"{letra_filas}  {asientos_str}")

    print("\nLeyenda:   . = Libre  |  X = Ocupado")

def reservar_asiento():
    """4.3 Reservar asiento"""
    print("\n" + "="*45)
    print("         RESERVAR ASIENTO")
    print("="*45)
    dia = input("Ingrese el dia: ").strip().capitalize()

    try:
        sala = int(input("Ingrese la sala (1-5): "))
    except ValueError:
        print(" Numero de sala invalido.")
        return

    horario = input("Ingrese el horario (Ej. 2:00 pm): ").strip()

    funcion = buscar_funcion(dia, sala, horario)
    if not funcion:
        print("\nLa funcion indicada no existe en la cartelera.")
        return

    asiento_codigo = input("Ingrese el asiento a reservar (Ej. C3, A1): ").strip().upper()

    # Valida el formato del codigo de asiento 
    if len(asiento_codigo) < 2 or asiento_codigo[0] not in FILAS or not asiento_codigo[1:].isdigit():
        print("Codigo de asiento invalido. Debe ser una letra de la A-E seguida de un numero del 1-6.")
        return

    fila_idx = FILAS.index(asiento_codigo[0])
    col_idx = int(asiento_codigo[1:]) - 1

    if col_idx < 0 or col_idx >= 6:
        print(" El numero de asiento esta fuera del rango de la sala (1-6.)")
        return
        
    clave = f"{dia}-{sala}-{funcion['horario']}"
    matriz = asientos_funciones[clave]

    if matriz[fila_idx][col_idx] == "X":
        print(f" El asiento {asiento_codigo} ya se encuentra ocupado.")
    else:
        matriz[fila_idx][col_idx] = "X"
        print(f"\n¡Reserva realizada con exito!")
        print(f"Asiento: {asiento_codigo} | pelicula: {funcion['pelicula']} | Formato: {funcion['formato']}")

def cancelar_reserva():
    # Libera el asiento reservado
    """4.4 Cancelar reserva"""
    print("\n" + "="*45)
    print("        CANCELAR RESERVA")
    print("="*45) 
    dia = input("Ingrese el dia: ").strip().capitalize()

    try:
        sala = int(input("Ingrese la sala (1-5): "))
    except ValueError:
        print("Numero de sala invalido.")
        return      

    horario = input("Ingresa el horario (Ej. 2:00 pm): ").strip()

    funcion = buscar_funcion(dia, sala, horario)
    if not funcion:
        print("Funcion no encontrada. verifique el dia, sala y horario.")
        return

    asiento_codigo = input("Ingrese el asiento a cancelar (Ej. C3): ").strip().upper()

    if len(asiento_codigo) < 2 or asiento_codigo[0] not in FILAS or not asiento_codigo[1:].isdigit():
        print("Codigo de asiento con formato incorrecto.")
        return

    fila_idx = FILAS.index(asiento_codigo[0])
    col_idx = int(asiento_codigo[1:]) - 1

    if col_idx < 0 or col_idx >= 6:
        print("El numero de asiento esta fuera del rango.")
        return

    clave = f"{dia}-{sala}-{funcion['horario']}"
    matriz = asientos_funciones[clave]

    if matriz[fila_idx][col_idx] == ".":
        print(f"El asiento {asiento_codigo} no esta reservado, ya se encuentra libre.")
    else:
        matriz[fila_idx][col_idx] == "."
        print(f"\nLa reserva del asiento {asiento_codigo} ha sido cancelada exitosamente.")

def ver_disponibilidad():
    """4.5 Ver disponibilidad general de un dia"""
    print("\n" + "="*45)
    print("     DISPONIBILIDAD GENERAL DEL DIA")
    print("="*45)
    dia = input("Ingrese el dia a consultar: ").strip().capitalize()

    if dia not in cartelera:
        print("\nDia no valido.")
        return

    print(f"\n--- Resumen de Dispinibilidad para el dia {dia} ---")
    for f in cartelera[dia]:
        clave = f"{dia}-{f['sala']}-{f['horario']}"
        matriz = asientos_funciones[clave]

        libres = 0
        ocupados = 0
        for filas in matriz:
            for asiento in filas:
                if asiento == ".":
                    libres += 1
                else:
                    ocupados += 1

    porcentaje_ocupacion = (ocupados / 30) * 100
    print(f"Pelicula: {f['pelicula']} | Sala: {f['sala']} | Horario: {f['horario']}")
    print(f"   Asientos Libres: {libres} | Asientos Ocupados: {ocupados} | Ocupacion: {porcentaje_ocupacion:.1f}%\n")
    print("-" * 60)

def menu_principal():
    # Controla el flujo principal del programa mediante las opciones
    while True:
        print("\n" + "="*45)
        print("     CineMax - Sistema de Reservas")
        print("="*45)
        print("1 Ver cartelera de un dia")
        print("2 Mostrar asientos de una funcion")
        print("3 Reservar asiento")
        print("4 Cancelar reserva")
        print("5 Ver disponibilidad")
        print("6 Salir")
        print("="*45)

        opcion = input("seleccione una opcion: ").strip()

        if opcion == "1":
            ver_cartelera_dia()
        elif opcion == "2":
            mostrar_asientos_pantalla()
        elif opcion == "3":
            reservar_asiento()
        elif opcion == "4":
            cancelar_reserva()
        elif opcion == "5":
            ver_disponibilidad()
        elif opcion == "6":
            print("\n¡Gracias por utilizar el sistema de reservas CineMax! Hasta luego.")
            break
        else:
            print("\nOpcion no valida. Igrese un numero del 1 al 6.")

# Ejecutar la aplicacion
if __name__ == "__main__":
    menu_principal()
        


    

    




