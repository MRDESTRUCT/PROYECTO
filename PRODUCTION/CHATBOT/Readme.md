# Chatbot

## Descripción

Esta aplicación se creó en base a una necesidad que muchas empresas ignoran: conocer la opinión de su público, ya sea sobre su marca o sobre sus productos. Este chatbot tiene como propósito principal recopilar los comentarios de la gente, ya sea desde la misma aplicación o desde una red social. Con esto, se espera que las compañías tengan una mayor cercanía con su clientela, lo que a largo plazo representa una ganancia para una empresa.

## Características

- **Recopilación de comentarios**: Permite la recopilación de comentarios de forma local.
- **Almacenamiento de datos**: Los comentarios introducidos se guardan en el sistema.
- **Integración con redes sociales**: Se inicia la integración con la API de Instagram.

## Versiones

### Versión Producción

En la versión de producción, se han realizado cambios específicos para mejorar la funcionalidad, la estabilidad y la experiencia de usuario del chatbot.

#### Cambios específicos realizados

- **Corrección de importación de Layout**: Cambié `window = sg.Window('Ingresar Comentarios').Layout(layout)` por `window = sg.Window('Ingresar Comentarios', layout)`.
- **Cerrar la ventana después de la lectura**: La ventana se cierra después de leer los valores en `obtener_comentarios_desde_input`.
- **Validación de comentarios**: Se verifica si los comentarios no están vacíos antes de proceder con la corrección y guardado en las funciones del menú principal.
- **Mejora en la Gestión de Excepciones**:
  - Incluye manejo de excepciones al dividir comentarios en líneas en `obtener_comentarios_desde_input`.
  - Mejora el manejo de excepciones en la función `guardar_comentarios_en_db`.
- **Refinamientos en la Interfaz de Usuario**:
  - Añade un mensaje de confirmación antes de cerrar la ventana en caso de que el usuario presione "Cancelar".
  - Mejora la disposición y el estilo de las ventanas para una mejor experiencia de usuario.
- **Organización Modular y Legible del Código**: Agrupa las funciones relacionadas en módulos o en clases si se considera necesario para mejorar la organización y reutilización del código.

---

# Chatbot

## Description

This application was created based on a need that many companies ignore: understanding public opinion about their brand or products. The primary purpose of this chatbot is to collect people's comments, either from the application itself or from a social network. This is expected to help companies build closer relationships with their clientele, representing long-term gains for the business.

## Features

- **Comment Collection**: Allows for the collection of comments locally.
- **Data Storage**: Stores the introduced comments within the system.
- **Social Media Integration**: Begins integration with the Instagram API.

## Versions

### Production Version

In the production version, specific changes were made to enhance functionality, stability, and user experience of the chatbot.

#### Specific Changes Made

- **Layout Import Correction**: Changed `window = sg.Window('Ingresar Comentarios').Layout(layout)` to `window = sg.Window('Ingresar Comentarios', layout)`.
- **Close Window After Reading**: The window now closes after reading values in `obtener_comentarios_desde_input`.
- **Comment Validation**: Ensures comments are not empty before proceeding with correction and saving in the main menu functions.
- **Improved Exception Handling**:
  - Includes exception handling when splitting comments into lines in `obtener_comentarios_desde_input`.
  - Improves exception handling in the function `guardar_comentarios_en_db`.
- **User Interface Refinements**:
  - Adds a confirmation message before closing the window if the user presses "Cancel".
  - Improves the layout and style of windows for a better user experience.
- **Modular and Readable Code Organization**: Groups related functions into modules or classes as needed to improve code organization and reusability.

---

**Responsable del desarrollo del proyecto**: Moises Chavarría.
