# Chatbot

## Descripción

Esta aplicación se creó en base a una necesidad que muchas empresas ignoran: conocer la opinión de su público, ya sea sobre su marca o sobre sus productos. Este chatbot tiene como propósito principal recopilar los comentarios de la gente, ya sea desde la misma aplicación o desde una red social. Con esto, se espera que las compañías tengan una mayor cercanía con su clientela, lo que a largo plazo representa una ganancia para una empresa.

## Características

- **Recopilación de comentarios**: Permite la recopilación de comentarios de forma local.
- **Almacenamiento de datos**: Los comentarios introducidos se guardan en el sistema.
- **Integración con redes sociales**: Se inicia la integración con la API de Instagram.

## Versiones

### Beta v1.0.0

En esta versión beta, el código del chatbot recibió múltiples mejoras y añadidos. Entre estos añadidos encontramos la inclusión de una base de datos SQLite para proporcionar un respaldo de la información proporcionada, además de la capacidad del chatbot para utilizar archivos .json para recolectar información de distintas páginas de internet.

#### Explicaciones de los cambios

- **Función `guardar_comentarios_en_db`**: Separé la lógica de guardar en la base de datos en su propia función para mayor claridad.
- **Validación de comentarios vacíos**: Agregué una verificación para asegurarse de que se obtienen comentarios antes de proceder con la corrección y el guardado.

### Beta v1.0.1

En esta actualización, se han realizado mejoras adicionales para optimizar la legibilidad y funcionalidad del código.

#### Adiciones y mejoras

- **Mejora en la legibilidad**: Reordené el código y las funciones para que sean más fáciles de seguir y entender.
- **Claridad en la salida**: Mensajes de impresión claros y específicos para cada acción completada, como guardar en el archivo de texto y en la base de datos, ayudan al usuario a entender qué está ocurriendo en cada etapa.

---

# Chatbot

## Description

This application was created based on a need that many companies ignore: understanding public opinion about their brand or products. The primary purpose of this chatbot is to collect people's comments, either from the application itself or from a social network. This is expected to help companies build closer relationships with their clientele, representing long-term gains for the business.

## Features

- **Comment Collection**: Allows for the collection of comments locally.
- **Data Storage**: Stores the introduced comments within the system.
- **Social Media Integration**: Begins integration with the Instagram API.

## Versions

### Beta v1.0.0

In this beta version, the chatbot code received multiple improvements and additions. Notably, the inclusion of a SQLite database provides a robust backup of the provided information, and the chatbot can now utilize .json files to gather information from various web pages.

#### Changes Explained

- **Function `guardar_comentarios_en_db`**: Separated the logic for saving to the database into its own function for clarity.
- **Empty Comment Validation**: Added a check to ensure comments are obtained before proceeding with correction and saving.

### Beta v1.0.1

In this update, additional enhancements were made to optimize code readability and functionality.

#### Additions and Improvements

- **Improved Readability**: Reorganized the code and functions to make them easier to follow and understand.
- **Clear Output Messages**: Clear and specific print messages for each completed action, such as saving to the text file and database, help users understand what is happening at each stage.

---

**Responsable del desarrollo del proyecto**: Moises Chavarría.
