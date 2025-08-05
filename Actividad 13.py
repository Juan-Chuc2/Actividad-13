estudents = {}

def saludar(): #inicio del programa
    print("\nBienvenido al programa")
def agregar_estudiante():
    while True:
        print("\n --AGREGAR ESTUDIANTES--")
        carnet = input("Ingrese el carné del estudiante: ") #se solicita el id del estudiante
        if carnet in estudents:
            print(f"El numero de carné {carnet} ya existe, vuelva a intentarlo")
            carnet = input("Ingrese el carné del estudiante: ")#si se equivoca en repetir un carnet se vuelve a solicitar
        else:
            name_estudent = input("Ingrese el nombre del estudiante: ")
            carrera = input("Ingrese la carrera del estudiante: ")
            estudents[carnet] = { "Nombre": name_estudent,
                    "Carrera": carrera,
                    "Cursos":{}
                                  }
            print("Se a registrado correctamente al estudiante ")
        break
while True:
    print("\n ---MENU---")
    print("1. Agregar Estudiante")
    print("2. Agregar curso con nota")
    print("3. Consultar Estudiante")
    print("4. Calcular el promedio del estudiante")
    print("5. Veificar si aprueba")
    print("6. Mostrar todos los estudiantes")
    print("7. Salir del programa")
    option = input("Ingrese una ocpion (1-7): ") #Ingreso de opcion menu
    match option:
        case "1":
            agregar_estudiante()