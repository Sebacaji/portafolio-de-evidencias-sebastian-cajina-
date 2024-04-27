# Inicializamos las listas para almacenar los nombres y temperaturas
nombres = []
temperaturas = []

# Definimos un diccionario para guardar los datos por día
datos_por_dia = {
    "Lunes": {"temperaturas": [], "nombres": []},
    "Martes": {"temperaturas": [], "nombres": []},
    "Miércoles": {"temperaturas": [], "nombres": []},
    "Jueves": {"temperaturas": [], "nombres": []},
    "Viernes": {"temperaturas": [], "nombres": []},
}

# Definimos una función para calcular la temperatura promedio
def temperatura_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Definimos una función para buscar la temperatura más alta y más baja
def buscar_extremos(temperaturas, nombres):
    indice_temperatura_max = temperaturas.index(max(temperaturas))
    indice_temperatura_min = temperaturas.index(min(temperaturas))
    return {
        "temperatura_max": temperaturas[indice_temperatura_max],
        "nombre_max": nombres[indice_temperatura_max],
        "temperatura_min": temperaturas[indice_temperatura_min],
        "nombre_min": nombres[indice_temperatura_min],
    }

# Definimos una función para ingresar datos por día
def ingresar_datos_por_dia(dia):
    # Solicitamos el número de personas a ingresar
    num_personas = int(input(f"Ingrese el número de personas que ingresaron el día {dia}: "))
    # Solicitamos los datos de cada persona
    for i in range(num_personas):
        nombre = input(f"Ingrese el nombre de la persona {i + 1}: ")
        temperatura = float(input(f"Ingrese la temperatura de la persona {i + 1}: "))
        # Almacenamos los datos en las listas y en el diccionario
        nombres.append(nombre)
        temperaturas.append(temperatura)
        datos_por_dia[dia]["nombres"].append(nombre)
        datos_por_dia[dia]["temperaturas"].append(temperatura)

# Solicitamos el día de la semana
dia = input("Ingrese el día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes): ")

# Verificamos que el día ingresado sea válido
if dia in datos_por_dia:
    # Llamamos a la función para ingresar los datos
    ingresar_datos_por_dia(dia)
else:
    print("El día ingresado no es válido.")

# Calculamos la temperatura promedio
temperatura_promedio_dia = temperatura_promedio(datos_por_dia[dia]["temperaturas"])

# Buscamos la temperatura más alta y más baja
extremos_dia = buscar_extremos(datos_por_dia[dia]["temperaturas"], datos_por_dia[dia]["nombres"])

# Mostramos los resultados
print(f"La temperatura promedio del día es {dia}: {temperatura_promedio_dia:.2f}")
print(f"La temperatura más alta del día es {dia}: {extremos_dia['temperatura_max']} (Persona: {extremos_dia['nombre_max']})")
print(f"La temperatura más baja del día es {dia}: {extremos_dia['temperatura_min']} (Persona: {extremos_dia['nombre_min']})")
