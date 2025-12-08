from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

class ColoredBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 0.90, 0.55, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class HitungTrapesiumApp(App):
    def build(self):
        self.layout = ColoredBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
            )
        
        judul = Label(
            text="TRAPESIUM",
            size_hint=(1, None),
            height=40,
            color=(0,0,0,1),
            font_size='20sp',
            bold=True
            )
        self.layout.add_widget(judul)

        self.image_trapesium = Image(source="trapesium.png",
                                    size=(200,200),
                                    size_hint=(None,None), 
                                    pos_hint={"center_x":0.5, "top":1}
                                    )
        
        self.layout.add_widget(self.image_trapesium)

        rumus = Label(
            text="Rumus : L = ½ × (sisi atas + sisi bawah) × tinggi",
            size_hint=(1, None),
            height=30,
            color=(0,0,0,1),
            font_size='16sp'
            )
        self.layout.add_widget(rumus)

        self.input_sisi_atas = TextInput(
            hint_text="Masukkan sisi atas trapesium",
            multiline=False,
            input_filter="float",
            size=(225,50),
            size_hint=(None,None),
            pos_hint=({"center_x": 0.5})
            )
        
        self.layout.add_widget(self.input_sisi_atas)

        self.input_sisi_bawah = TextInput(
            hint_text="Masukkan sisi bawah trapesium",
            multiline=False,
            input_filter="float",
            size=(225,50),
            size_hint=(None,None),
            pos_hint=({"center_x": 0.5})
            )
        
        self.layout.add_widget(self.input_sisi_bawah)

        self.input_tinggi = TextInput(
            hint_text="Masukkan tinggi trapesium",
            multiline=False,
            input_filter="float",
            size=(225,50),
            size_hint=(None,None),
            pos_hint=({"center_x": 0.5})
            )

        self.layout.add_widget(self.input_tinggi)

        tombol_hitung = Button(text="Hitung Luas", 
                               size=(225,50),
                               size_hint=(None,None),
                               pos_hint={"center_x": 0.5}
                               )
        
        tombol_hitung.bind(on_press=self.hitung_luas)
        self.layout.add_widget(tombol_hitung)

        self.label_hasil = TextInput(
            hint_text="Luas akan muncul si sini",
            multiline=False,
            input_filter="float",
            size=(225,50),
            size_hint=(None,None),
            pos_hint=({"center_x": 0.5})
            )
        self.layout.add_widget(self.label_hasil)

        return self.layout

    def hitung_luas(self, instance):
        try:
            sisi_atas = float(self.input_sisi_atas.text)
            sisi_bawah = float(self.input_sisi_bawah.text)
            tinggi = float(self.input_tinggi.text)
            luas = 0.5 * (sisi_atas + sisi_bawah) * tinggi
            self.label_hasil.text = f"Luas Trapesium: {luas}"
        except:
            self.label_hasil.text = "Input harus berupa angka!"

if __name__ == "__main__":
    HitungTrapesiumApp().run()