from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

class TrapesiumApp(App):
    def build(self):
        Window.clearcolor = (1, 0.95, 0.6, 1)   # background #FFEAA0 seperti gambar

        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Judul
        title = Label(text="TRAPESIUM", font_size=28, bold=True, color=(0,0,0,1))
        layout.add_widget(title)

        # Gambar (gunakan gambar kamu sendiri)
        img = Image(source="trapesium.png", size_hint=(1, 0.4))
        layout.add_widget(img)

        # Rumus
        rumus = Label(
            text="Rumus : L = ½ × (sisi atas + sisi bawah) × tinggi",
            font_size=18,
            color=(0, 0, 0, 1)
        )
        layout.add_widget(rumus)

        # Input sisi atas
        self.sisi_atas = TextInput(
            hint_text="Masukkan sisi atas trapesium",
            multiline=False,
            size_hint=(1, None),
            height=45
        )
        layout.add_widget(self.sisi_atas)

        # Input sisi bawah
        self.sisi_bawah = TextInput(
            hint_text="Masukkan sisi bawah trapesium",
            multiline=False,
            size_hint=(1, None),
            height=45
        )
        layout.add_widget(self.sisi_bawah)

        # Input tinggi
        self.tinggi = TextInput(
            hint_text="Masukkan tinggi trapesium",
            multiline=False,
            size_hint=(1, None),
            height=45
        )
        layout.add_widget(self.tinggi)

        # Tombol hitung
        tombol = Button(
            text="Hitung Luas",
            size_hint=(1, None),
            height=50,
            background_color=(0.3, 0.3, 0.3, 1)
        )
        tombol.bind(on_press=self.hitung)
        layout.add_widget(tombol)

        # Output
        self.hasil = Label(
            text="Luas akan muncul di sini",
            font_size=18,
            color=(0, 0, 0, 1)
        )
        layout.add_widget(self.hasil)

        return layout

    def hitung(self, instance):
        try:
            a = float(self.sisi_atas.text)
            b = float(self.sisi_bawah.text)
            t = float(self.tinggi.text)

            L = 0.5 * (a + b) * t
            self.hasil.text = f"Luas = {L}"
        except:
            self.hasil.text = "Input tidak valid!"

TrapesiumApp().run()