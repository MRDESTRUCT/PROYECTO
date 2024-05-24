# Text Classification with Naive Bayes Classifier - Beta Version

## Description / Descripción

**English:**
This beta version of the text classification code builds upon the previous version by adding new features and improvements. It now includes a graphical user interface (GUI) using Tkinter, allows users to analyze sentiment from text files, and incorporates additional natural language processing (NLP) functionalities such as word frequency analysis and filtering of stopwords. The results are displayed in a bar chart showing the percentage of positive and negative sentiments in the text.

**Español:**
Esta versión beta del código de clasificación de texto se basa en la versión anterior, añadiendo nuevas características y mejoras. Ahora incluye una interfaz gráfica de usuario (GUI) utilizando Tkinter, permite a los usuarios analizar el sentimiento de archivos de texto e incorpora funcionalidades adicionales de procesamiento de lenguaje natural (NLP), como el análisis de frecuencia de palabras y el filtrado de palabras vacías (stopwords). Los resultados se muestran en un gráfico de barras que muestra el porcentaje de sentimientos positivos y negativos en el texto.

## Notes / Notas

**Improvements over Alpha Version / Mejoras sobre la Versión Alpha:**
1. **Graphical User Interface (GUI):** The Beta version introduces a Tkinter GUI for a more user-friendly experience.
   - **Interfaz Gráfica de Usuario (GUI):** La versión Beta introduce una GUI de Tkinter para una experiencia más amigable para el usuario.
2. **Text File Analysis:** Users can select and analyze sentiment from text files.
   - **Análisis de Archivos de Texto:** Los usuarios pueden seleccionar y analizar el sentimiento de archivos de texto.
3. **Word Frequency Analysis:** The code now includes functionality to count word frequency and identify the most used word.
   - **Análisis de Frecuencia de Palabras:** El código ahora incluye la funcionalidad para contar la frecuencia de palabras e identificar la palabra más utilizada.
4. **Stopwords Filtering:** The Beta version filters out common stopwords to improve the accuracy of word frequency analysis.
   - **Filtrado de Palabras Vacías:** La versión Beta filtra las palabras vacías comunes para mejorar la precisión del análisis de frecuencia de palabras.
5. **Sentiment Results Visualization:** Sentiment analysis results are visualized using a bar chart.
   - **Visualización de Resultados de Sentimiento:** Los resultados del análisis de sentimiento se visualizan utilizando un gráfico de barras.

## Usage / Uso

1. Make sure you have the required libraries installed:
   ```bash
   pip install textblob nltk matplotlib tkinter

