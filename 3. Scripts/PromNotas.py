""""
@author Sebastián PuenteR
"""
import os
import pandas as pd

# Lista vacia para acumular los registros
Registros = []

#=================
def AgregaCurso():
    """Esta función crea lo registros de la notas para un curso"""

    print('\n=== Ingresar Curso ===\n')
    Notas = []
    NombreCurso = input('Ingrese nombre del curso: ').strip()
    Escala = int(input('Valor máximo de notas (ej: 5 ó 10): '))
    NumPeriodos = int(input('Número Periodos: '))

    # Se capturan las 4 notas y se guardan en la lista notas
    print('Digitar Notas...')
    for n in range(1, NumPeriodos+1):
        nota = float(input(f'Digita la nota del Periodo {n}: '))
        Notas.append(nota)
    
    # Cálculos
    Promedio = sum(Notas) / len(Notas)
    Nivel = NivelDes(Promedio, Escala)
    Aprobacion = Aprobar(Promedio, Escala*0.6)

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
    print(f'Promedio Curso: {Promedio:.2f}')
    print(f'Aprobación: {Aprobacion.title()}')
    print(f'Nivel Desempeño: {Nivel.title()}')

    input('\nPulsa Enter para continuar...')
    os.system('clear')

# =================
def VerRegistros():

    print('\n=== Cursos Registrados ===\n')
    
    if len(Registros) == 0:
        print('Sin cursos registrados.')
    else:
        df = pd.DataFrame(Registros)
        print(df)
    
    input('\nPulsa Enter para continuar...')
    os.system('clear')

# =============================
def NivelDes(promedio, escala):
    """Devuelve el nivel de desempeño en una escala de 1 a 10"""

    Desempeño = ''
    PromedioNorma = promedio/escala

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
def Aprobar(promedio, notamin):

    if promedio >= notamin:
        return 'aprobado'
    else:
        return 'reprobado'

# ================
def MostrarMenu():
    """Imprime las opciones disponibles en la pantalla."""
    
    print("\n" + "="*25)
    print("      MENÚ PRINCIPAL      ")
    print("="*25)
    print("1. Ingresar Notas Curso")
    print("2. Ver Registros")
    print("3. Salir")
    print("="*25)
    print('Cursos registrados:', len(Registros))

# ================
# Inicio programa
def Inicio():

    while True:

        MostrarMenu()
        
        Opcion = input('\nDigite su opción del menú: ').strip()

        match Opcion:
            case '1':
                AgregaCurso()
            case '2':
                VerRegistros()
            case '3':
                print('Hasta Pronto')
                break
            case _:
                print("Opción no válida")  # The '_' acts as a default 'else' case
    

# Punto de entrada del script
if __name__ == "__main__":
    os.system('clear')
    Inicio()


