# DATAPAN

## Descripción
Esta aplicación se creó en base a una necesidad que muchas empresas ignoran: conocer la opinión de su público, ya sea sobre su marca o sobre sus productos. El propósito del algoritmo es proporcionar una herramienta sencilla y efectiva para clasificar opiniones de los clientes como positivas o negativas. Esto permite a las empresas construir una mayor cercanía con su clientela, lo que a largo plazo representa una ganancia para una empresa.

## Características
- **Clasificación de Sentimientos:** El código está diseñado para clasificar textos como "positivos" o "negativos" utilizando un clasificador Naive Bayes.
- **Entrenamiento con Datos Pre-etiquetados:** Utiliza un conjunto de datos pre-etiquetados almacenados en un archivo JSON para entrenar el clasificador.
- **Interfaz Gráfica de Usuario (GUI) con Kivy:** Utiliza Kivy para proporcionar una interfaz gráfica de usuario que permite cargar archivos de texto y mostrar resultados.
- **Visualización de Resultados:** Genera un gráfico de barras para mostrar el porcentaje de oraciones positivas y negativas en el texto analizado.
- **Análisis de Frecuencia de Palabras:** Identifica y muestra las palabras más mencionadas en el texto analizado, excluyendo las stopwords.

## Versiones

### Beta v1.0.0
En esta versión beta del chatbot, se han añadido características avanzadas y una interfaz gráfica mejorada para facilitar la interacción del usuario.

#### Funcionalidades Iniciales
- **Carga de Datos de Entrenamiento:** El programa abre un archivo JSON y carga los datos de entrenamiento, que se espera que estén en formato de lista de diccionarios con claves 'text' y 'label'.
- **Formateo de Datos:** Convierte los datos de entrenamiento en una lista de tuplas (texto, etiqueta), que es el formato requerido por el clasificador de Naive Bayes de textblob.
- **Entrenamiento del Clasificador:** Crea y entrena un clasificador de Naive Bayes utilizando los datos formateados.
- **Interfaz Gráfica de Usuario:** Crea una ventana de Kivy con botones que permiten al usuario cargar archivos de texto y datos de entrenamiento, y realizar análisis.
- **Análisis y Clasificación de Textos:** Tokeniza el texto en oraciones y palabras, filtra las stopwords, y clasifica cada oración como positiva o negativa.
- **Visualización de Resultados:** Muestra un gráfico de barras con los porcentajes de oraciones positivas y negativas, y muestra las palabras más mencionadas en el texto.

#### Errores Conocidos
- **Problemas de Codificación:** Si el archivo JSON o el archivo de texto no están codificados en UTF-8, podría causar errores al intentar cargar los datos.
- **Estructura del Archivo JSON:** Si el archivo JSON no tiene la estructura esperada (lista de diccionarios con claves 'text' y 'label'), el programa fallará al intentar formatear los datos.
- **Dependencia de NLTK:** El código depende de que ciertos recursos de NLTK, como las stopwords, estén descargados previamente, lo que podría causar problemas si no se han descargado.
- **Limitaciones del Clasificador:** La precisión del clasificador depende en gran medida de la calidad y cantidad de los datos de entrenamiento. Si los datos de entrenamiento no están equilibrados o son insuficientes, el clasificador podría no funcionar correctamente.
- **Interfaz de Usuario:** La interfaz gráfica es básica y podría mejorarse para manejar mejor errores, como la cancelación de la selección de archivos o la carga de archivos no válidos.

---

# DATAPAN

## Description
This application was created based on a need that many companies ignore: understanding public opinion about their brand or products. The purpose of the algorithm is to provide a simple and effective tool to classify customer opinions as positive or negative. This allows companies to build a closer relationship with their clientele, representing long-term gains for the business.

## Features
- **Sentiment Classification:** The code is designed to classify texts as "positive" or "negative" using a Naive Bayes classifier.
- **Training with Pre-labeled Data:** Uses a set of pre-labeled data stored in a JSON file to train the classifier.
- **Graphical User Interface (GUI) with Kivy:** Uses Kivy to provide a graphical user interface for loading text files and displaying results.
- **Results Visualization:** Generates a bar chart to show the percentage of positive and negative sentences in the analyzed text.
- **Word Frequency Analysis:** Identifies and displays the most mentioned words in the analyzed text, excluding stopwords.

## Versions

### Beta v1.0.0
In this beta version of the chatbot, advanced features have been added and an improved graphical interface has been created to facilitate user interaction.

#### Initial Features
- **Training Data Loading:** The program opens a JSON file and loads the training data, which is expected to be in the format of a list of dictionaries with keys 'text' and 'label'.
- **Data Formatting:** Converts the training data into a list of tuples (text, label), which is the format required by the textblob Naive Bayes classifier.
- **Classifier Training:** Creates and trains a Naive Bayes classifier using the formatted data.
- **Graphical User Interface:** Creates a Kivy window with buttons that allow the user to load text files and training data, and perform analysis.
- **Text Analysis and Classification:** Tokenizes the text into sentences and words, filters out stopwords, and classifies each sentence as positive or negative.
- **Results Visualization:** Displays a bar chart with the percentages of positive and negative sentences, and shows the most mentioned words in the text.

#### Known Issues
- **Encoding Issues:** If the JSON file or the text file is not encoded in UTF-8, it may cause errors when trying to load the data.
- **JSON File Structure:** If the JSON file does not have the expected structure (list of dictionaries with 'text' and 'label' keys), the program will fail when trying to format the data.
- **NLTK Dependency:** The code depends on certain NLTK resources, such as stopwords, being downloaded beforehand, which could cause issues if they are not downloaded.
- **Classifier Limitations:** The accuracy of the classifier depends largely on the quality and quantity of the training data. If the training data is unbalanced or insufficient, the classifier may not work correctly.
- **User Interface:** The graphical interface is basic and could be improved to better handle errors, such as canceling file selection or loading invalid files.
  
--- 

**Responsable del desarrollo del proyecto** : Amilkar Moreno
