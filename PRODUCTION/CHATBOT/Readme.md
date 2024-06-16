Cambios específicos realizados:

Corrección de importación de Layout: Cambié window = sg.Window('Ingresar Comentarios').Layout(layout) por window = sg.Window('Ingresar Comentarios', layout).

Cerrar la ventana después de la lectura: La ventana se cierra después de leer los valores en obtener_comentarios_desde_input.

Validación de comentarios: Se verifica si los comentarios no están vacíos antes de proceder con la corrección y guardado en las funciones del menú principal.

Mejora en la Gestión de Excepciones:Incluye manejo de excepciones al dividir comentarios en líneas en obtener_comentarios_desde_input.
Mejora el manejo de excepciones en la función guardar_comentarios_en_db.
Refinamientos en la Interfaz de Usuario:

Añade un mensaje de confirmación antes de cerrar la ventana en caso de que el usuario presione "Cancelar".
Mejora la disposición y el estilo de las ventanas para una mejor experiencia de usuario.
Organización Modular y Legible del Código:

Agrupa las funciones relacionadas en módulos o en clases si se considera necesario para mejorar la organización y reutilización del código.



