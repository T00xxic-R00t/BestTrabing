import os
import random
import string
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def generar_contrasena(nombre, longitud=12, incluir_numeros=True, incluir_letras=True, incluir_puntuacion=True):
    caracteres = ''
    
    if incluir_numeros:
        caracteres += string.digits
    if incluir_letras:
        caracteres += string.ascii_letters
    if incluir_puntuacion:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return f"{nombre}_{contrasena}"

def mostrar_logo():
    os.system('clear')  # Limpiar la terminal en sistemas UNIX/Linux
    
    logo = f"""
{Fore.BLUE} 
  ____            _             _     _             
 |  _ \          | |           | |   (_)            
 | |_) | ___  ___| |_ _ __ __ _| |__  _ _ __   __ _ 
 |  _ < / _ \/ __| __| '__/ _` | '_ \| | '_ \ / _` |
 | |_) |  __/\__ \ |_| | | (_| | |_) | | | | | (_| |
 |____/ \___||___/\__|_|  \__,_|_.__/|_|_| |_|\__, |
                                               __/ |
                                              |___/ 
{Style.RESET_ALL}"""
    print(logo)

def guardar_contrasenas(contrasenas):
    nombre_archivo = "passwords.txt"
    ruta_completa = os.path.abspath(nombre_archivo)

    with open(nombre_archivo, 'a') as archivo:  
        for contrasena in contrasenas:
            archivo.write(f"{contrasena}\n")
    
    print(f"\n{Fore.GREEN}Las contraseñas se han guardado en el archivo: {ruta_completa}{Style.RESET_ALL}")

def visualizar_contrasenas():
    nombre_archivo = "passwords.txt"
    
    if os.path.exists(nombre_archivo):
        print(f"\n{Fore.GREEN}Contraseñas guardadas en {nombre_archivo}:{Style.RESET_ALL}\n")
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                print(linea.strip())
    else:
        print(f"\n{Fore.RED}El archivo {nombre_archivo} no existe o está vacío.{Style.RESET_ALL}")

    input("\nPresiona Enter para continuar...")

def main():
    contrasenas_generadas = []
    nombre = ""

    while True:
        mostrar_logo()
        
        print(f"{Fore.GREEN}Bienvenido a la herramienta generadora de contraseñas aleatorias!{Style.RESET_ALL}")
        if not nombre:
            nombre = input("\nIntroduce el nombre para la contraseña: ")

        while True:
            print(f"\nTipo de caracter seleccionado: {nombre}\n")
            print("Elige los tipos de caracteres para la contraseña:")
            print("1. Solo números")
            print("2. Solo letras")
            print("3. Números y letras")
            print("4. Números, letras y puntuación")
            print("5. Visualizar contraseñas guardadas")
            print("6. Volver al inicio")

            opcion = input("Selecciona una opción (1/2/3/4/5/6) [Predeterminado: 3]: ") or '3'

            if opcion in ['1', '2', '3', '4', '5', '6']:
                break

        if opcion == '6':
            nombre = ""
            continue
        elif opcion == '5':
            visualizar_contrasenas()
            continue

        longitud = int(input("\nIntroduce la longitud de la contraseña [Predeterminado: 12]: ") or 12)
        
        incluir_numeros = opcion in ['1', '3', '4']
        incluir_letras = opcion in ['2', '3', '4']
        incluir_puntuacion = opcion == '4'

        cantidad = int(input("\nIntroduce la cantidad de contraseñas a generar [Predeterminado: 1]: ") or 1)

        print("\nGenerando contraseñas...\n")

        for _ in range(cantidad):
            contrasena_generada = generar_contrasena(nombre, longitud, incluir_numeros, incluir_letras, incluir_puntuacion)
            contrasenas_generadas.append(contrasena_generada)
            print(f"Contraseña generada: {Fore.CYAN}{contrasena_generada}{Style.RESET_ALL}")
            print("-" * 50)

        guardar_opcion = input(f"\n¿Deseas guardar las contraseñas en un archivo? (s/n) [Predeterminado: s]: ") or 's'
        if guardar_opcion.lower() == 's':
            guardar_contrasenas(contrasenas_generadas)

        revisar_opcion = input("\n¿Deseas revisar si se han guardado las contraseñas en el archivo passwords.txt? (s/n) [Predeterminado: s]: ") or 's'
        if revisar_opcion.lower() == 's':
            visualizar_contrasenas()

        continuar = input("\n¿Deseas generar más contraseñas? (s/n) [Predeterminado: s]: ") or 's'
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()
