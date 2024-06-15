import json
import nltk
from textblob.classifiers import NaiveBayesClassifier
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.card import MDCard
from kivymd.uix.list import OneLineListItem
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
import os
import datetime

# Descargar el corpus de stopwords de NLTK
nltk.download('stopwords')

# Variables globales
cl = None  # Se inicializará con el clasificador después de cargar los datos de entrenamiento

# Función para cargar datos de entrenamiento desde un archivo JSON
def load_training_data(json_file):
    global cl

    with open(json_file, 'r', encoding='utf-8') as fp:
        training_data = json.load(fp)

    formatted_training_data = [(item['text'], item['label']) for item in training_data]
    cl = NaiveBayesClassifier(formatted_training_data)

# Función para analizar el sentimiento y obtener las palabras más mencionadas
def analyze_text(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Filtrar stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]

    # Análisis de frecuencia de palabras
    word_freq = Counter(filtered_words)
    most_common_words = word_freq.most_common()

    # Analizar sentimiento
    sentiment_scores = [cl.classify(sentence) for sentence in sentences]
    positive_count = sentiment_scores.count('pos')
    negative_count = sentiment_scores.count('neg')

    return most_common_words, positive_count, negative_count

# Cargar el archivo KV con estilos definidos
Builder.load_string('''
<RoundedButton@Button>:
    size_hint: None, None
    size: self.texture_size[0] + dp(16), dp(48)
    pos_hint: {"center_x": 0.5}
    md_bg_color: app.theme_cls.primary_color
    text_color: 1, 1, 1, 1
    radius: [dp(10)]
''')

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"  # Cambiar el color primario a BlueGray
        self.theme_cls.theme_style = "Light"  # Tema inicial es claro
        Window.set_icon('path_to_your_icon.png')  # Reemplaza 'path_to_your_icon.png' con la ruta de tu icono

        layout = MDBoxLayout(
            orientation='vertical', 
            padding=[dp(10), dp(20), dp(10), dp(20)],  # Padding [left, top, right, bottom]
            spacing=10
        )
        Window.size = (600, 800) 

        # Mensaje de bienvenida
        welcome_label = MDLabel(
            text='Bienvenido a la Aplicación de Análisis de Datos',
            size_hint=(1, 0.1),
            font_style="H5",
            halign="center",
            theme_text_color="Secondary",
            padding=[dp(10), dp(0)]  # Ajustar padding izquierda y derecha
        )
        layout.add_widget(welcome_label)

        # Botón circular para alternar el tema
        self.button_theme_toggle = MDIconButton(
            icon="brightness-4",
            pos_hint={'center_x': 0.95, 'center_y': 0.98},
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            md_bg_color=self.theme_cls.primary_color
        )
        self.button_theme_toggle.bind(on_press=self.change_theme)
        layout.add_widget(self.button_theme_toggle)

        # Etiqueta de título
        title_label = MDLabel(
            text='Análisis de Datos',
            size_hint=(1, 0.1),
            font_style="H5",
            halign="center",
            theme_text_color="Primary",
            padding=[dp(10), dp(0)]  # Ajustar padding izquierda y derecha
        )
        layout.add_widget(title_label)

        # Botón para cargar datos de entrenamiento con icono de descarga
        button_load_training_data = MDRaisedButton(
            text='Cargar Datos de Entrenamiento',
            size_hint=(1, 0.1),
            theme_text_color='Custom',
            text_color=(1, 1, 1, 1),
            md_bg_color=self.theme_cls.primary_color,
            on_press=self.load_training_data,
            padding=[dp(10), dp(0)]  # Ajustar padding izquierda y derecha
        )
        icon_download = MDIconButton(icon="download", theme_text_color="Custom", text_color=(1, 1, 1, 1))
        button_load_training_data.add_widget(icon_download)
        layout.add_widget(button_load_training_data)

        # Botón para cargar archivo de texto para análisis con icono de métrica
        button_analyze_text = MDRaisedButton(
            text='Cargar Archivo de Texto para Análisis',
            size_hint=(1, 0.1),
            theme_text_color='Custom',
            text_color=(1, 1, 1, 1),
            md_bg_color=self.theme_cls.primary_color,
            on_press=self.analyze_text_file,
            padding=[dp(10), dp(0)]  # Ajustar padding izquierda y derecha
        )
        icon_chart = MDIconButton(icon="chart-bar", theme_text_color="Custom", text_color=(1, 1, 1, 1))
        button_analyze_text.add_widget(icon_chart)
        layout.add_widget(button_analyze_text)

        # Botón para cambiar entre carita feliz y triste
        self.button_face = MDIconButton(
            icon="emoticon-happy-outline",
            pos_hint={'center_x': 0.05, 'center_y': 0.98},
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            md_bg_color=self.theme_cls.primary_color
        )
        self.button_face.bind(on_press=self.toggle_face)
        layout.add_widget(self.button_face)

        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            ext=[".json", ".txt"]
        )

        return layout

    # Método para cargar datos de entrenamiento
    def load_training_data(self, instance):
        self.file_manager_open()

    # Método llamado cuando se selecciona un archivo
    def select_path(self, path):
        if path.endswith('.json'):
            load_training_data(path)
            self.show_dialog("Datos de entrenamiento cargados correctamente")
        elif path.endswith('.txt'):
            text = self.read_text_file(path)
            most_common_words, positive_count, negative_count = analyze_text(text)
            self.save_recent_stats(most_common_words, positive_count, negative_count)
            self.show_sentiment_graph(positive_count, negative_count)
        self.exit_manager()

    # Método para abrir el gestor de archivos
    def file_manager_open(self):
        self.file_manager.show('/')  # Abrir gestor de archivos en directorio raíz
        Window.bind(on_keyboard=self.events)

    # Método para cerrar el gestor de archivos
    def exit_manager(self, *args):
        self.file_manager.close()
        Window.unbind(on_keyboard=self.events)

    # Método para manejar eventos de teclado
    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            self.file_manager.back()
        return True

    # Método para mostrar un diálogo
    def show_dialog(self, text):
        dialog = MDDialog(
            text=text,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ],
        )
        dialog.open()

    # Método para cargar archivo de texto y realizar análisis de sentimiento
    def analyze_text_file(self, instance):
        self.file_manager_open()

    # Método para cambiar entre temas claro y oscuro
    def change_theme(self, instance):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            instance.icon= "brightness-7"  # Cambiar icono a luna (tema oscuro)
        else:
            self.theme_cls.theme_style = "Light"
            instance.icon = "brightness-4"  # Cambiar icono a sol (tema claro)

    # Método para alternar entre carita feliz y triste
    def toggle_face(self, instance):
        if self.button_face.icon == "emoticon-happy-outline":
            self.button_face.icon = "emoticon-sad-outline"
        else:
            self.button_face.icon = "emoticon-happy-outline"

    # Método para leer contenido de un archivo de texto
    def read_text_file(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text

    # Método para guardar estadísticas recientes
    def save_recent_stats(self, most_common_words, positive_count, negative_count):
        # Guardar palabras más comunes
        if most_common_words:
            common_words_content = ""
            for word, frequency in most_common_words:
                common_words_content += f"{word}: {frequency}\n"
            self.save_to_file(common_words_content, "recent_common_words.txt")

        # Guardar gráfica de sentimientos
        self.show_sentiment_graph(positive_count, negative_count)

    # Método para guardar texto en un archivo
    def save_to_file(self, content, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            self.show_dialog(f"Archivo guardado como '{filename}'")
        except Exception as e:
            self.show_dialog(f"Error al guardar el archivo: {str(e)}")

    # Método para mostrar la gráfica de sentimientos y permitir guardarla
    def show_sentiment_graph(self, positive_count, negative_count):
        labels = ['Positivos', 'Negativos']
        sizes = [positive_count, negative_count]
        colors = ['#4CAF50', '#F44336']  # Verde para positivos y rojo para negativos

        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title('Análisis de Sentimientos')
        plt.axis('equal')

        # Guardar la gráfica como imagen
        filename = f"sentiment_analysis_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        plt.savefig(filename)
        plt.close()

        self.show_dialog(f"Gráfica de sentimientos guardada como '{filename}'")

    def on_start(self):
        self.show_welcome_message()

    def show_welcome_message(self):
        self.show_dialog("¡Bienvenido a la aplicación de Análisis de Datos!")

# Ejecutar la aplicación
if __name__ == '__main__':
    MainApp().run()

