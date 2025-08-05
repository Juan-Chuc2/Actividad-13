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
            name_estudent = input("Ingrese el nombre del estudiante: ").capitalize()
            carrera = input("Ingrese la carrera del estudiante: ").capitalize()
            estudents[carnet] = { "Nombre": name_estudent,
                    "Carrera": carrera, #Se agrega los datos al diccionario
                    "Cursos":{}
                                  }
            print("Se a registrado correctamente al estudiante ")
        break
def curso_con_nota():
    while True:
        print("\n Agregar curso con nota")
        carne = input("Ingrese el carnet del estudiante: ")  # se solicita el carné
        if carne not in estudents:
            print(" Verifique el carné, no se encontró. Vuelva a intentarlo")
        else:
            while True: # Validamos nombre del curso
                name_curs = input("Ingrese el nombre del curso: ").capitalize().strip()
                if name_curs == "":
                    print(" El nombre del curso no puede quedar vacío")
                else:
                    break
            while True: # Con un try-except se valida la nota
                try:
                    nota = float(input(f"Ingrese la nota del curso {name_curs}: "))
                    if 0 <= nota <= 100:
                        estudents[carne]['Cursos'][name_curs] = nota
                        print(" Se agregó correctamente el curso y la nota")
                        break
                    else:
                        print(f" La nota {nota} no está entre 0 y 100, vuelva a intentarlo")
                except ValueError:
                    print(" Error: Se ingresó un dato inválido, intente nuevamente")
        break
def consultar_estudiante():
    while True:
        try:
            print("\n --CONSULTA DE ESTUDIANTE--")
            carne = input("Ingrese el carne del estudiante a mostrar: ")
            if carne not in estudents:
                print(f"el numero de carné {carne} no se encontro. vuelva a intentarlo") # se verifica que si exista el carne
            else:
                print(f" Nombre: {estudents[carne]['Nombre']}")
                print(f" Carrera: {estudents[carne]['Carrera']}")
                if estudents[carne]['Cursos']:
                    print("Cursos que tiene asignados: ")
                    print("Nombre del Curso   ||   Nota final")
                    for curso, nota in estudents[carne]["Cursos"].items():
                        print(f"{curso} || {nota}")  # se impime información del estudiante
                    break
        except ValueError:
            print("Se ingreso un dato invalidop") #Para evitar errores
def calcular_promedio():
    while True:
        print("\n --PROMEDIO ESTUDIANTE--")
        carne = input("Ingrese el numero de carné a buscar: ")
        if carne not in estudents:
            print(f"El numero de carné {carne} no se encontro. Vuelva a intenralo")# se evalua que si este el carne en el dcicionario
        else:
            curso = estudents[carne]['Cursos'] #comienza el proceso de promedio
            if len(curso) ==0:
                print("No hay ningun curso registrado") # Se evalua que si haya cursos registrados
            else:
                sum_notas = 0 #declaro contadores para calcular el promedio
                cantidad_curs = 0
                for nota in curso.values():
                    sum_notas += nota
                    cantidad_curs +=1
                print(f"El promedio de {estudents[carne]['Nombre']} es {sum_notas/cantidad_curs}") #Se calcula el promedio
                break
saludar()
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
        case "2":
            curso_con_nota()
        case "3":
            consultar_estudiante()
        case "4":
            calcular_promedio()