import PySimpleGUI as sg
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
        sg.popup_error(f"Error al obtener comentarios desde la API: {e}")
        return []

def obtener_comentarios_desde_input():
    comentarios = []
    layout = [
        [sg.Text("Ingrese los comentarios (presione Enter para finalizar):")],
        [sg.Multiline(size=(40, 8), key='-COMMENTS-')],
        [sg.Button('Guardar Comentarios'), sg.Button('Cancelar')]
    ]
    window = sg.Window('Ingresar Comentarios').Layout(layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
        elif event == 'Guardar Comentarios':
            comentarios = values['-COMMENTS-'].split('\n')
            break

    window.close()
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
        sg.popup("Comentarios guardados en comentarios.txt")
    except IOError as e:
        sg.popup_error(f"Error al guardar comentarios en el archivo: {e}")

def guardar_comentarios_en_db(comentarios):
    try:
        conexion = sqlite3.connect('comentarios.db')
        cursor = conexion.cursor()

        # Crear tabla si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS comentarios (id INTEGER PRIMARY KEY, comentario TEXT)''')

        # Insertar comentarios
        for comentario in comentarios:
            cursor.execute('INSERT INTO comentarios (comentario) VALUES (?)', (comentario,))
        
        conexion.commit()
        conexion.close()
        sg.popup("Comentarios guardados en la base de datos comentarios.db")
    except sqlite3.Error as e:
        sg.popup_error("Error al guardar comentarios en la base de datos:", e)

def menu_principal():
    layout = [
        [sg.Text('Chatbot', font=('Helvetica', 20))],
        [sg.Button('Obtener Comentarios Localmente')],
        [sg.Button('Obtener Comentarios desde API')],
        [sg.Button('Salir')]
    ]
    window = sg.Window('Chatbot').Layout(layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Salir':
            break
        elif event == 'Obtener Comentarios Localmente':
            comentarios = obtener_comentarios_desde_input()
            comentarios_corregidos = corregir_ortografia_pyspellchecker(comentarios)
            guardar_comentarios_en_txt(comentarios_corregidos)
            guardar_comentarios_en_db(comentarios_corregidos)
        elif event == 'Obtener Comentarios desde API':
            comentarios = obtener_comentarios_desde_api()
            comentarios_corregidos = corregir_ortografia_pyspellchecker(comentarios)
            guardar_comentarios_en_txt(comentarios_corregidos)
            guardar_comentarios_en_db(comentarios_corregidos)

    window.close()

if __name__ == "__main__":
    menu_principal()
