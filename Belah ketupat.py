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
            Color(0.72, 0.89, 0.56, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self.update_rect, pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class HitungBelahketupatApp(App):
    def build(self):
        self.layout = ColoredBoxLayout(
            orientation="vertical",
            padding=10,
            spacing=10
            )

        judul = Label(
            text="BELAH KETUPAT",
            size_hint=(1, None),
            height=40,
            color=(0,0,0,1),
            font_size='20sp',
            bold=True
            )
        self.layout.add_widget(judul)

        self.image_belahketupat = Image(source="belahketupat.png",
                                    size=(200,200),
                                    size_hint=(None,None), 
                                    pos_hint={"center_x":0.5, "top":1}
                                    )
        self.layout.add_widget(self.image_belahketupat)

        rumus = Label(
            text="Rumus : L = ½ × d1 × d2", 
            size_hint=(1, None),
            height=30,
            color=(0,0,0,1),
            font_size='16sp'
            )
        self.layout.add_widget(rumus)
            
        self.input_diagonal1 = TextInput(
            hint_text="Masukkan panjang diagonal1",
            multiline=False,
            input_filter="float",
            size=(225,50),
            size_hint=(None,None),
            pos_hint=({"center_x": 0.5})
            )
        self.layout.add_widget(self.input_diagonal1)

        self.input_diagonal2 = TextInput(
            hint_text="Masukkan panjang diagonal2",
            multiline=False,
            input_filter="float",
            size=(225,50),
            size_hint=(None,None),
            pos_hint=({"center_x": 0.5})
            )
        self.layout.add_widget(self.input_diagonal2)

        tombol_hitung = Button(text="Hitung Luas", 
                               size=(225,50),
                               size_hint=(None,None),
                               pos_hint={"center_x": 0.5}
                               )
        
        tombol_hitung.bind(on_press=self.hitung_luas)
        self.layout.add_widget(tombol_hitung)

        self.label_hasil = TextInput(
            hint_text="Luas akan muncul di sini",
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
            d1 = float(self.input_diagonal1.text)
            d2 = float(self.input_diagonal2.text)
            luas = 0.5 * d1 * d2
            self.label_hasil.text = f"Luas Belah ketupat: {luas}"
        except:
            self.label_hasil.text = "Input harus berupa angka!"

if __name__ == "__main__":
    HitungBelahketupatApp().run()