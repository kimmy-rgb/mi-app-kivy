from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.clearcolor = (0.05, 0.05, 0.1, 1)  # fondo oscuro futurista


class AppFuturista(App):

    def build(self):
        self.root = BoxLayout(orientation="vertical", padding=20, spacing=15)

        self.titulo = Label(
            text="⚡ SISTEMA INTERGALÁCTICO ⚡",
            font_size=24,
            color=(0, 1, 1, 1)
        )

        self.input = TextInput(
            hint_text="Escribe un comando...",
            size_hint=(1, 0.2),
            multiline=False
        )

        self.boton = Button(
            text="Ejecutar",
            size_hint=(1, 0.2),
            background_color=(0, 0.8, 1, 1)
        )

        self.resultado = Label(
            text="Esperando comando...",
            font_size=18,
            color=(0, 1, 0.5, 1)
        )

        self.boton.bind(on_press=self.ejecutar)

        self.root.add_widget(self.titulo)
        self.root.add_widget(self.input)
        self.root.add_widget(self.boton)
        self.root.add_widget(self.resultado)

        return self.root

    def ejecutar(self, instance):
        texto = self.input.text

        if texto == "":
            self.resultado.text = "⚠ Escribe algo primero"
        elif "hola" in texto.lower():
            self.resultado.text = "🌌 Hola viajero del sistema"
        elif "python" in texto.lower():
            self.resultado.text = "🐍 Python activado en modo mental"
        else:
            self.resultado.text = f"🔮 Comando recibido: {texto}"


AppFuturista().run()
