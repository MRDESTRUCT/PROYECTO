import requests
import spacy

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

def corregir_ortografia_spacy(comentarios):
    nlp = spacy.load("es_core_news_sm")
    comentarios_corregidos = []

    for comentario in comentarios:
        doc = nlp(comentario)
        comentario_corregido = ' '.join([token.text for token in doc])
        comentarios_corregidos.append(comentario_corregido)

    return comentarios_corregidos

def recopilar_comentarios_automaticamente():
    comentarios = []

    try:
        with open('comentarios.txt', 'r') as archivo:
            comentarios = archivo.read().splitlines()
    except FileNotFoundError:
        pass

    nuevos_comentarios = obtener_comentarios_desde_api()
    nuevos_comentarios_corregidos = corregir_ortografia_spacy(nuevos_comentarios)

    for comentario in nuevos_comentarios_corregidos:
        if comentario not in comentarios:
            comentarios.append(comentario)

    print("Comentarios Recopilados:")
    for comentario in comentarios:
        print("-", comentario)

    with open('comentarios.txt', 'w') as archivo:
        for comentario in comentarios:
            archivo.write(comentario + '\n')

if __name__ == "__main__":
    recopilar_comentarios_automaticamente()
