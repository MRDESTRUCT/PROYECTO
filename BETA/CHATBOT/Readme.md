En la Beta v1.0.0 el codigo del Chatbot recibio multiples mejoras y añadidos entre estos añadidos encontramos la inclusion de una base de datos de Sqlite para proporcionar un respaldo de la informacion proporcionada ademas de la inclusion de que el chatbot puede utilizar archivos .json para recolectar informacion de distintas paginas de internet

Explicaciones de los cambios:

Función guardar_comentarios_en_db: Separé la lógica de guardar en la base de datos en su propia función para mayor claridad.

Validación de comentarios vacíos: Agregué una verificación para asegurarse de que se obtienen comentarios antes de proceder con la corrección y el guardado.

Adiciones en la version v1 1.0.1

Mejora en la legibilidad: Reordené el código y las funciones para que sean más fáciles de seguir y entender.

Claridad en la salida: Mensajes de impresión claros y específicos para cada acción completada, como guardar en el archivo de texto y en la base de datos, ayudan al usuario a entender qué está ocurriendo en cada etapa.
