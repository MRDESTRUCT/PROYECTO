import requests
from spellchecker import SpellChecker

def obtener_comentarios_desde_api(token_acceso):
    try:
        url = f'https://api.instagram.com/comments?access_token={token_acceso}'
        response = requests.get(url)
        response.raise_for_status()

        comentarios = response.json()
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

def recopilar_comentarios_automaticamente(token_acceso):
    comentarios = []

    try:
        with open('comentarios.txt', 'r') as archivo:
            comentarios = archivo.read().splitlines()
    except FileNotFoundError:
        pass

    nuevos_comentarios = obtener_comentarios_desde_api(token_acceso)
    nuevos_comentarios_corregidos = corregir_ortografia_pyspellchecker(nuevos_comentarios)

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
    token_acceso = 'IGQWRNb053VWgtd2hnRW5GWFdPYm12cjRiWmR4d21NV0VaeGVJMHNUT0N3VWRWa1dQd25KSTM3UnBieE1QeUd1clo0YzRFTTMwZAzlGemRWenQtOG1GR0NaYWJtZAndja3ZAVZAzI0d0FzUEU5eUZAhRVo4bFBrWElnS28ZD'
    recopilar_comentarios_automaticamente(token_acceso)
