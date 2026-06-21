""""
@author Sebastián PuenteR
"""
import os
import pandas as pd

# Lista vacia para acumular los registros
Registros = []

#=================
def agregarCurso():
    """Esta función crea lo registros de la notas para un curso"""

    print('\n=== Ingresar Curso ===\n')
    Notas = []
    NombreCurso = input('Ingrese nombre del curso: ').strip()
    #Escala = int(input('Valor máximo de notas (ej: 5 ó 10): '))
    Escala = pedirNumero('Valor máximo de notas (ej: 5 ó 10): ', 1, 100)
    #NumPeriodos = int(input('Número Periodos: '))
    NumPeriodos = pedirNumero('Número Periodos (máx 10): ', 1, 10)

    # Se capturan las 4 notas y se guardan en la lista notas
    print('\nDigitar Notas...')
    for n in range(1, NumPeriodos+1):
        nota = pedirNumero(f'Digita la nota del Periodo {n}: ', 1, Escala, permitir_float=True)
        Notas.append(nota)
    
    # Cálculos
    Promedio = sum(Notas) / len(Notas)
    Nivel = nivelDesempeño(Promedio, Escala)
    Aprobacion = verAprobacion(Promedio, Escala*0.6)

    # Se agrega el registro como un diccionario dentro de la lista Registros
    Nuevo_Registro = {
        'Nombre': NombreCurso,
        'Periodos': NumPeriodos,
        'Nota Periodos': Notas,
        'Escala': Escala,
        'Promedio': Promedio,
        'Aprobación': Aprobacion,
        'Nivel': Nivel
    }
    Registros.append(Nuevo_Registro)
    
    # Mostrar datos registrados
    print('\n=== Datos Registrados ===\n')
    print(f'Nombre Curso: {NombreCurso.title()}')
    print(f'Número Periodos: {NumPeriodos}')
    print(f'Notas Registradas: {Notas}')
    print(f'Escala: {Escala}')
    print(f'- Promedio Curso: {Promedio:.2f}')
    print(f'- Aprobación: {Aprobacion.title()}')
    print(f'- Nivel Desempeño: {Nivel.title()}')

    # Guardar info en Dataframe
    global Data
    Nueva_Data = pd.DataFrame([Nuevo_Registro])
    Data = pd.concat([Data, Nueva_Data], ignore_index=True)

    input('\nPulsa Enter para continuar...')
    os.system('clear')

# =================
def verRegistros():
    """Visualiza en pantalla todos los datos del curso que acaba de crearse"""

    print('\n=== Cursos Registrados ===\n')
    
    if len(Registros) == 0:
        print('Sin cursos registrados.')
    
    else:
        global Data
        print(Data)
        #print(Data)
        
    input('\nPulsa Enter para continuar...')
    os.system('clear')

# =============================
def nivelDesempeño(promedio, max):
    """Devuelve el nivel de desempeño en una escala de 1 a max"""

    Desempeño = ''
    PromedioNorma = promedio/max

    if PromedioNorma >=  9/10:
        Desempeño = 'superior'
    elif PromedioNorma >= 8/10:
        Desempeño = 'alto'
    elif PromedioNorma >= 6/10:
        Desempeño = 'básico'
    else:
        Desempeño = 'bajo'
    
    return Desempeño

# =============================
def verAprobacion(promedio, notamin):
    """Devuelve si el curso es aprobado o reprobado de acuerdo a la notamin de aprobación"""

    if promedio >= notamin:
        return 'aprobado'
    else:
        return 'reprobado'

# =========================
def iniciarDataFrame():
    """Funciín que crea el DataFrame inicial vacio donde se iran guardando los cursos"""
    
    global Data
    Data = pd.DataFrame(columns=["Nombre", "Periodos", "Nota Periodos", "Escala", "Promedio", "Aprobación", "Nivel"])

# ==============
def pedirNumero(mensaje, minimo, maximo, permitir_float=False):
    """Función que captura un número del teclado en un rango fijo (min - max),
    ya sea entero o float de acuerdo al respectivo parámetro"""
    
    while True:

        entrada = input(mensaje)
        try:
            # Conversión según parámetro
            if permitir_float:
                numero = float(entrada)
            else:
                numero = int(entrada)

            # Validar rango
            if minimo <= numero <= maximo:
                return numero  # Retorna el número y termina la función
            else:
                print(f'❌ Error: El número debe estar entre {minimo} y {maximo}.\n')
        
        except ValueError:
            if permitir_float:
                print('❌ Error: Ingresa un número válido (entero o decimal).\n')
            else:
                print('❌ Error: Por favor, ingresa solo números enteros.\n')

# ================
def mostrarMenu():
    """Imprime las opciones disponibles en la pantalla y muestra los cursos registrados"""
    
    print("\n" + "="*25)
    print("      MENÚ PRINCIPAL      ")
    print("="*25)
    print("1. Ingresar Notas Curso")
    print("2. Ver Registros")
    print("3. Salir")
    print("="*25)
    
    print(f'Cursos registrados: {len(Registros)}')
    for n in range(0, len(Registros)):
        print(f'- {n+1}. {Registros[n]['Nombre'].title()}: {Registros[n]['Promedio']:.1f}, {Registros[n]['Nivel'].title()}, {Registros[n]['Aprobación'].title()}')

# ================
# Inicio programa
def Inicio():

    iniciarDataFrame()

    while True:

        mostrarMenu()
        
        Opcion = input('\nDigite su opción del menú: ').strip()

        match Opcion:
            case '1':
                agregarCurso()
            case '2':
                verRegistros()
            case '3':
                print('\nHasta Pronto!...')
                print('= Sebas PuenteR =\n')
                break
            case _:
                print("Opción no válida")  # The '_' acts as a default 'else' case
                os.system('clear')

# Punto de entrada del script
if __name__ == "__main__":
    os.system('clear')
    Inicio()