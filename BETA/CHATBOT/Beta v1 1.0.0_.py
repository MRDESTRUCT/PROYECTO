import pymongo
import requests
from spellchecker import SpellChecker

# Conexión a MongoDB
cliente = pymongo.MongoClient("mongodb://localhost:27017/")  # Conexión a MongoDB local, cambiar según sea necesario
base_de_datos = cliente["comentarios_db"]  # Nombre de tu base de datos
coleccion = base_de_datos["comentarios"]  # Nombre de la colección

def obtener_comentarios_desde_api():
    try:
        response = requests.get('https://restcountries.com/v3.1/all')
        response.raise_for_status()

        paises = response.json()
        comentarios = [pais['name']['common'] for pais in paises]
        return comentarios
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener comentarios desde la API: {e}")
        return []

def corregir_ortografia_pyspellchecker(comentarios):
    spell = SpellChecker(language='es')
    comentarios_corregidos = []

    for comentario in comentarios:
        tokens_corregidos = [spell.correction(token) or token for token in comentario.split()]  # Usar token original si la corrección es None
        comentario_corregido = ' '.join(tokens_corregidos)
        comentarios_corregidos.append(comentario_corregido)

    return comentarios_corregidos

def recopilar_y_guardar_comentarios():
    nuevos_comentarios = obtener_comentarios_desde_api()
    nuevos_comentarios_corregidos = corregir_ortografia_pyspellchecker(nuevos_comentarios)
    
    # Guardar comentarios en la base de datos MongoDB
    for comentario in nuevos_comentarios_corregidos:
        if coleccion.count_documents({"comentario": comentario}) == 0:
            coleccion.insert_one({"comentario": comentario})
    
    # Guardar comentarios en un archivo de texto como respaldo
    with open('comentarios_respaldo.txt', 'a') as archivo:
        for comentario in nuevos_comentarios_corregidos:
            archivo.write(comentario + '\n')

    print("Comentarios recopilados y guardados en MongoDB y como respaldo en un archivo de texto.")

if __name__ == "__main__":
    recopilar_y_guardar_comentarios()
