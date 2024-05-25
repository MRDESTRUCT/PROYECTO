import requests
from spellchecker import SpellChecker
import sqlite3

def obtener_comentarios_desde_api():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/comments')
        response.raise_for_status()

        comentarios = response.json()
        comentarios = [comentario['body'] for comentario in comentarios]
        return comentarios
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener comentarios desde la API: {e}")
        return []

def obtener_comentarios_desde_input():
    comentarios = []
    print("Ingrese los comentarios (presione Enter para finalizar):")
    while True:
        comentario = input("> ")
        if not comentario:
            break
        comentarios.append(comentario)
    return comentarios

def corregir_ortografia_pyspellchecker(comentarios):
    spell = SpellChecker(language='es')
    comentarios_corregidos = []

    for comentario in comentarios:
        tokens_corregidos = [spell.correction(token) or token for token in comentario.split()]
        comentario_corregido = ' '.join(tokens_corregidos)
        comentarios_corregidos.append(comentario_corregido)

    return comentarios_corregidos

def guardar_comentarios_en_txt(comentarios):
    try:
        with open('comentarios.txt', 'w') as archivo:
            for comentario in comentarios:
                archivo.write(comentario + '\n')
        print("Comentarios guardados en comentarios.txt")
    except IOError as e:
        print(f"Error al guardar comentarios en el archivo: {e}")

def recopilar_comentarios_automaticamente():
    comentarios = []

    # Dar opción al usuario para elegir entre API o entrada manual
    print("Seleccione cómo desea obtener los comentarios:")
    print("1. Obtener comentarios desde la API")
    print("2. Ingresar comentarios manualmente")
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        comentarios = obtener_comentarios_desde_api()
    elif opcion == '2':
        comentarios = obtener_comentarios_desde_input()
    else:
        print("Opción no válida. Saliendo del programa.")
        return

    # Corregir ortografía
    comentarios_corregidos = corregir_ortografia_pyspellchecker(comentarios)

    # Imprimir comentarios
    print("Comentarios Recopilados:")
    for comentario in comentarios_corregidos:
        print("-", comentario)

    # Guardar comentarios en el archivo de texto
    guardar_comentarios_en_txt(comentarios_corregidos)

    # Guardar comentarios en la base de datos
    try:
        conexion = sqlite3.connect('comentarios.db')
        cursor = conexion.cursor()

        # Crear tabla si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS comentarios (id INTEGER PRIMARY KEY, comentario TEXT)''')

        # Insertar comentarios
        for comentario in comentarios_corregidos:
            cursor.execute('INSERT INTO comentarios (comentario) VALUES (?)', (comentario,))
        
        conexion.commit()
        conexion.close()
    except sqlite3.Error as e:
        print("Error al guardar comentarios en la base de datos:", e)

if __name__ == "__main__":
    recopilar_comentarios_automaticamente()
