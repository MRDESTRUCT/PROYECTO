# Text Classification with Naive Bayes Classifier

## Description / Descripción

**English:**
This code is used to classify user-inputted texts as "positive" or "negative" using a Naive Bayes classifier trained with a pre-labeled dataset. The program loads training data from a JSON file, trains the classifier, and then allows the user to input texts for classification until "exit" is typed to terminate the execution.

**Español:**
Este código se utiliza para clasificar textos ingresados por el usuario como "positivos" o "negativos" utilizando un clasificador Naive Bayes entrenado con un conjunto de datos previamente etiquetado. El programa carga los datos de entrenamiento desde un archivo JSON, entrena el clasificador y luego permite al usuario ingresar textos para clasificarlos hasta que se escriba "exit" para terminar la ejecución.

## Code / Código

```python
import json
from textblob.classifiers import NaiveBayesClassifier

# Ruta del archivo JSON que contiene los datos de entrenamiento
# Path to the JSON file containing the training data
file_path = 'B:/PROYECTO IA CLASIFICADORA/datossp.json'

# Abre el archivo JSON y carga los datos de entrenamiento
# Open the JSON file and load the training data
with open(file_path, 'r', encoding='utf-8') as fp:
    training_data = json.load(fp)

# Formatea los datos de entrenamiento para que sean una lista de tuplas (texto, etiqueta)
# Format the training data to be a list of tuples (text, label)
training_data_formatted = [(item['text'], item['label']) for item in training_data]

# Crea un clasificador Naive Bayes con los datos de entrenamiento formateados
# Create a Naive Bayes classifier with the formatted training data
cl = NaiveBayesClassifier(training_data_formatted)

# Bucle infinito para recibir entrada del usuario y clasificarla
# Infinite loop to receive user input and classify it
while True:
    # Solicita al usuario que ingrese un texto para clasificar
    # Prompt the user to input text for classification
    user_input = input("Me encanto la comida")

    # Si el usuario escribe 'exit', termina el bucle
    # If the user types 'exit', break the loop
    if user_input.lower() == 'exit':
        break

    # Clasifica el texto ingresado por el usuario
    # Classify the user input text
    classification = cl.classify(user_input)
    
    # Imprime la clasificación del texto como positivo o negativo
    # Print the classification of the text as positive or negative
    if classification == 'positive':
        print(f"The sentence is classified as positive: {user_input}")
    else:
        print(f"The sentence is classified as negative: {user_input}")
