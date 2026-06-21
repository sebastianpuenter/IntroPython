""""
@author Sebastián PuenteR
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import termplotlib as tpl

# Lista vacia para acumular los registros
Registros = []

#==================
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
    Promedio = round(sum(Notas) / len(Notas), 1)
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
    print(f'Escala: /{Escala}\n')
    print(f'- Promedio Curso: {Promedio}')
    print(f'- Aprobación: {Aprobacion.title()}')
    print(f'- Nivel Desempeño: {Nivel.title()}')

    # Guardar info en Dataframe
    global Data
    Nueva_Data = pd.DataFrame([Nuevo_Registro])
    Data = pd.concat([Data, Nueva_Data], ignore_index=True)

    input('\nPulsa Enter para continuar...')
    os.system('clear')

# ================
def borrarCurso():
    """Borra curso tanto en la lista Registro como en el Dataframe"""

    print('\n=== Borrar Curso ===')

    if len(Registros) == 0:
        print('Sin cursos para borrar')
    else:
        Posicion = pedirNumero('Número de curso a borrar: ', 1, len(Registros))
        indice = Posicion - 1

        print(f'\nCurso a borrar: {Posicion}. {Registros[indice]['Nombre'].title()}')
        
        # Borrar curso en la lista Registros
        del Registros[indice]
        # Borrar curso en el Dataframe
        global Data
        Data.drop(indice, inplace=True)
        Data.reset_index(drop=True, inplace=True)
        print('Curso borrado.')
    
    input('\nPulsa Enter para continuar...')
    os.system('clear')

# =================
def verRegistros():

    print(f'\nCursos registrados: {len(Registros)}')
    print('----------------------')
    for n in range(0, len(Registros)):
        print(f'{n+1}. {Registros[n]['Nombre'].title()}: {Registros[n]['Promedio']}, {Registros[n]['Nivel'].title()}, {Registros[n]['Aprobación'].title()}')

# =================
def verDataFrame():
    """Visualiza en pantalla todos los datos del curso que acaba de crearse"""

    print('\n=== Cursos Registrados ===\n')
    
    global Data
    if len(Registros) == 0:
        print('Sin cursos registrados.')
    else:
        print(Data)
        print(f'\nTotal Cursos Registrados: {len(Data)}')

    input('\nPulsa Enter para continuar...')
    os.system('clear')

# ================================
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

# ===================================
def verAprobacion(promedio, notamin):
    """Devuelve si el curso es aprobado o reprobado de acuerdo a la notamin de aprobación"""

    if promedio >= notamin:
        return 'aprobado'
    else:
        return 'reprobado'

# =====================
def iniciarDataFrame():
    """Funciín que crea el DataFrame inicial vacio donde se iran guardando los cursos"""
    
    global Data
    Data = pd.DataFrame(columns=["Nombre", "Periodos", "Nota Periodos", "Escala", "Promedio", "Aprobación", "Nivel"])

# =============================================================
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

# ===================
def graficarCursos():

    print('\n=== Gráfica Promedios ===\n')

    if len(Registros) == 0:
        print('Sin datos para graficar')
    
    else:
        Cursos = []
        Promedios = []

        # se obtiene lista de nombres de cursos y lista con los promedios
        for n in range(0, len(Registros)):
            Cursos.append(Registros[n]['Nombre'].title())
            Promedios.append(Registros[n]['Promedio'])
    
        # === Crear la figura para la terminal ===
        fig = tpl.figure()
        # Dibujar el gráfico de barras horizontales
        fig.barh(Promedios, labels=Cursos, force_ascii=False)
        # Mostrar el gráfico en la consola
        fig.show()

        # === Graficar con Matplotlib ===
        promedio_general = sum(Promedios) / len(Promedios)
        
        # Crear gráfico de barras
        plt.figure(figsize=(8,5))
        barras = plt.bar(Cursos, Promedios,)

        # Agregar el promedio general como línea horizontal
        plt.axhline(y=promedio_general, color='red', linestyle='--', linewidth=2,
                    label=f'Promedio General ({promedio_general:.1f})')
        
        # Personalizar el gráfico
        plt.title('Promedio de Cursos', fontsize=14, fontweight='bold')
        plt.xlabel('Cursos', fontsize=12)
        plt.ylabel('Calificación', fontsize=12)
        #plt.ylim(0, 10) # Ajusta este límite según la escala de tus notas (ej. 100 o 5)
        plt.legend()

        # Mostrar valores encima de cada barra
        for bar in barras:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, round(yval, 2),
                     ha='center', va='bottom', fontsize=10)
        
        # Ajustar diseño y mostrar
        plt.tight_layout()
        plt.show()


    input('\nPulsa Enter para continuar...')
    os.system('clear')

# ================
def mostrarMenu():
    """Imprime las opciones disponibles en la pantalla y muestra los cursos registrados"""
    
    print("\n" + "="*25)
    print("      MENÚ PRINCIPAL      ")
    print("="*25)
    print("1. Ingresar Curso")
    print("2. Ver Registros")
    print("3. Borrar Curso")
    print("4. Graficar")
    print("5. Salir")
    print("="*25)

# ======================================
def degly():
    Nuevo_Registro1 = {'Nombre': 'fisica', 'Periodos': 4, 'Nota Periodos': [7, 8, 8, 7], 'Escala': 10, 'Promedio': 7.5, 'Aprobación': 'aprobado', 'Nivel': 'alto'}
    Registros.append(Nuevo_Registro1)
    Nuevo_Registro2 = {'Nombre': 'tecnologia', 'Periodos': 4, 'Nota Periodos': [6, 6, 6, 6], 'Escala': 10, 'Promedio': 6.0, 'Aprobación': 'aprobado', 'Nivel': 'basico'}
    Registros.append(Nuevo_Registro2)
    Nuevo_Registro3 = {'Nombre': 'ciencias', 'Periodos': 4, 'Nota Periodos': [8.5, 8.5, 8.5, 8.5], 'Escala': 10, 'Promedio': 8.5, 'Aprobación': 'aprobado', 'Nivel': 'alto'}
    Registros.append(Nuevo_Registro3)
    Nuevo_Registro4 = {'Nombre': 'sociales', 'Periodos': 4, 'Nota Periodos': [7.5, 7.5, 7.5, 7.5], 'Escala': 10, 'Promedio': 7.5, 'Aprobación': 'aprobado', 'Nivel': 'alto'}
    Registros.append(Nuevo_Registro4)

    global Data
    Data = pd.DataFrame(Registros)
    
    os.system('clear')
# ==========================================

# ================
# Inicio programa
def Inicio():

    iniciarDataFrame()

    while True:

        mostrarMenu()
        verRegistros()
        
        Opcion = input('\nDigite su opción del menú: ').strip()

        match Opcion:
            case '1':
                agregarCurso()
            case '2':
                verDataFrame()
            case '3':
                borrarCurso()
            case '4':
                graficarCursos()
            case '5':
                print('\nHasta Pronto!...')
                print('= Sebas PuenteR =\n')
                break
            case 'degly':
                degly()
            case _:
                print("Opción no válida")  # The '_' acts as a default 'else' case
                os.system('clear')

# Punto de entrada del script
if __name__ == "__main__":
    os.system('clear')
    Inicio()