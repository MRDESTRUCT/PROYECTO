# DATAPAN

## Descripción
Esta aplicación se creó en base a una necesidad que muchas empresas ignoran: conocer la opinión de su público, ya sea sobre su marca o sobre sus productos. El propósito del algoritmo es proporcionar una herramienta sencilla y efectiva para clasificar opiniones de los clientes como positivas o negativas. Esto permite a las empresas construir una mayor cercanía con su clientela, lo que a largo plazo representa una ganancia para una empresa.

## Características
- **Análisis de Sentimientos:**
  - Clasifica oraciones en positivas o negativas utilizando un clasificador Naive Bayes preentrenado.
  - Proporciona un análisis de la distribución de sentimientos en el texto cargado.
- **Análisis de Frecuencia de Palabras:**
  - Filtra las palabras comunes (stopwords).
  - Calcula la frecuencia de las palabras restantes y muestra las más mencionadas.
- **Interfaz Gráfica:**
  - Utiliza KivyMD para una interfaz moderna y estilizada.
  - Incluye botones para cargar datos de entrenamiento y archivos de texto para análisis.
- **Cambio de Tema:**
  - Alterna entre temas claro y oscuro.
  - Cambia el icono del botón según el tema seleccionado.
- **Guardar Resultados:**
  - Guarda los resultados del análisis de sentimientos en una gráfica.
  - Guarda las palabras más mencionadas en un archivo de texto.

## Versiones

### v1.0.0
En esta versión de producción inicial, se han añadido características avanzadas y una interfaz gráfica mejorada para facilitar la interacción del usuario.

#### Funcionalidades Iniciales
- **Análisis de Sentimientos:** Clasifica oraciones en positivas o negativas utilizando un clasificador Naive Bayes preentrenado. Proporciona un análisis de la distribución de sentimientos en el texto cargado.
- **Análisis de Frecuencia de Palabras:** Filtra las palabras comunes (stopwords) y calcula la frecuencia de las palabras restantes, mostrando las más mencionadas.
- **Interfaz Gráfica:** Utiliza KivyMD para una interfaz moderna y estilizada, incluyendo botones para cargar datos de entrenamiento y archivos de texto para análisis.
- **Cambio de Tema:** Alterna entre temas claro y oscuro, cambiando el icono del botón según el tema seleccionado.
- **Guardar Resultados:** Guarda los resultados del análisis de sentimientos en una gráfica y las palabras más mencionadas en un archivo de texto.

#### Errores Iniciales y Mejoras
- **Problema con el filtro de stopwords:** El filtro estaba configurado para inglés en lugar de español. Solución: Cambiar el filtro de stopwords a español.
- **Gestión del Gestor de Archivos:** La gestión del gestor de archivos podría ser más intuitiva. Solución: Mejorar la navegación y la interacción con el gestor de archivos.
- **Iconos y Estilo:** Algunos botones no estaban correctamente estilizados o faltaban iconos. Solución: Añadir y mejorar iconos y estilos en los botones.
- **Manejo de Archivos y Rutas:** La ruta del icono de la ventana no estaba definida. Solución: Asegurarse de que los recursos estén correctamente referenciados y cargados.

### v1.0.1
En esta actualización, se han realizado múltiples mejoras y correcciones de errores para aumentar la estabilidad y funcionalidad del chatbot.

#### Mejoras y Correcciones
- **Filtro de Stopwords:** Actualizado para español para mejorar el análisis de frecuencia de palabras.
- **Gestor de Archivos:** Mejorada la navegación y la interacción con el gestor de archivos para una experiencia de usuario más intuitiva.
- **Iconos y Estilo:** Añadidos y mejorados iconos y estilos en los botones para una interfaz más atractiva.
- **Manejo de Archivos y Rutas:** Corregidas las referencias de recursos para asegurar que los iconos y otros elementos gráficos se carguen correctamente.

---

# DATAPAN

## Description
This application was created based on a need that many companies ignore: understanding public opinion about their brand or products. The purpose of the algorithm is to provide a simple and effective tool to classify customer opinions as positive or negative. This allows companies to build a closer relationship with their clientele, representing long-term gains for the business.

## Features
- **Sentiment Analysis:**
  - Classifies sentences as positive or negative using a pre-trained Naive Bayes classifier.
  - Provides an analysis of the sentiment distribution in the loaded text.
- **Word Frequency Analysis:**
  - Filters common words (stopwords).
  - Calculates the frequency of the remaining words and displays the most mentioned ones.
- **Graphical Interface:**
  - Uses KivyMD for a modern and stylish interface.
  - Includes buttons for loading training data and text files for analysis.
- **Theme Switching:**
  - Alternates between light and dark themes.
  - Changes the button icon according to the selected theme.
- **Save Results:**
  - Saves sentiment analysis results in a graph.
  - Saves the most mentioned words in a text file.

## Versions

### v1.0.0
In this initial production version, advanced features and an improved graphical interface have been added to facilitate user interaction.

#### Initial Features
- **Sentiment Analysis:** Classifies sentences as positive or negative using a pre-trained Naive Bayes classifier. Provides an analysis of the sentiment distribution in the loaded text.
- **Word Frequency Analysis:** Filters common words (stopwords) and calculates the frequency of the remaining words, displaying the most mentioned ones.
- **Graphical Interface:** Uses KivyMD for a modern and stylish interface, including buttons for loading training data and text files for analysis.
- **Theme Switching:** Alternates between light and dark themes, changing the button icon according to the selected theme.
- **Save Results:** Saves sentiment analysis results in a graph and the most mentioned words in a text file.

#### Initial Errors and Improvements
- **Stopwords Filter Issue:** The filter was set to English instead of Spanish. Solution: Change the stopwords filter to Spanish.
- **File Manager Handling:** The file manager handling could be more intuitive. Solution: Improve navigation and interaction with the file manager.
- **Icons and Styling:** Some buttons were not correctly styled or lacked icons. Solution: Add and improve icons and styles on the buttons.
- **File and Path Handling:** The window icon path was not defined. Solution: Ensure resources are correctly referenced and loaded.

### v1.0.1
In this update, multiple improvements and bug fixes have been made to enhance the stability and functionality of the chatbot.

#### Improvements and Fixes
- **Stopwords Filter:** Updated to Spanish to improve word frequency analysis.
- **File Manager:** Improved navigation and interaction with the file manager for a more intuitive user experience.
- **Icons and Styling:** Added and improved icons and styles on the buttons for a more attractive interface.
- **File and Path Handling:** Fixed resource references to ensure icons and other graphical elements load correctly.

---

**Responsable del desarrollo del proyecto**: Amilkar Moreno.
