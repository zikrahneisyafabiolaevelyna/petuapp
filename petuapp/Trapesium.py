from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.metrics import sp, dp


class TrapesiumScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # =====================
        # ROOT
        # =====================
        root = FloatLayout()

        # =====================
        # BACKGROUND
        # =====================
        with root.canvas.before:
            self.bg = Rectangle(
                source="bg trapesium.png",
                pos=root.pos,
                size=root.size
            )

        root.bind(size=self.update_bg, pos=self.update_bg)

        # =====================
        # LAYOUT UTAMA
        # =====================
        layout = BoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(15),
            size_hint=(1, 1)
        )

        # =====================
        # JUDUL
        # =====================
        layout.add_widget(Label(
            text="HITUNG LUAS TRAPESIUM",
            font_name="MondayTuesdayDemo.otf",
            font_size=sp(30),
            color=(0.953, 0.737, 0.180, 1),
            size_hint_y=None,
            height=dp(50)
        ))

        # =====================
        # GAMBAR
        # =====================
        layout.add_widget(Image(
            source="trapesium.png",
            size_hint=(1, None),
            height=dp(180),
            allow_stretch=True,
            keep_ratio=True
        ))

        # =====================
        # RUMUS
        # =====================
        layout.add_widget(Label(
            text="Rumus: ½ × (a + b) × t",
            font_name= "Blustrue.otf",
            font_size=sp(18),
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=dp(30)
        ))

        # =====================
        # INPUT (STYLE KAMU)
        # =====================
        self.inputSisiAtas = TextInput(
            hint_text="Sisi atas (a)",
            multiline=False,
            input_filter="float",
            size_hint=(None, None),
            size=(dp(150), dp(45)),
            pos_hint={"center_x": 0.5}
        )
        layout.add_widget(self.inputSisiAtas)

        self.inputSisiBawah = TextInput(
            hint_text="Sisi bawah (b)",
            multiline=False,
            input_filter="float",
            size_hint=(None, None),
            size=(dp(150), dp(45)),
            pos_hint={"center_x": 0.5}
        )
        layout.add_widget(self.inputSisiBawah)

        self.inputTinggi = TextInput(
            hint_text="Tinggi (t)",
            multiline=False,
            input_filter="float",
            size_hint=(None, None),
            size=(dp(150), dp(45)),
            pos_hint={"center_x": 0.5}
        )
        layout.add_widget(self.inputTinggi)

        # =====================
        # TOMBOL HITUNG
        # =====================
        btn_hitung = Button(
            text="Hitung Luas",
            size_hint=(None, None),
            size=(dp(120), dp(50)),
            font_name = "Voyage Rush.otf",
            pos_hint={"center_x": 0.5}
        )
        btn_hitung.bind(on_press=self.hitung_luas)
        layout.add_widget(btn_hitung)

        # =====================
        # LABEL HASIL (ANTI TUMPANG TINDIH)
        # =====================
        self.label_hasil = Label(
            text="Luas akan muncul di sini",
            font_size=sp(18),
            color=(0, 0, 0, 1),
            size_hint_y=None,
            height=dp(40),
            halign="center",
            valign="middle"
        )
        self.label_hasil.bind(
            size=lambda *x: setattr(self.label_hasil, "text_size", self.label_hasil.size)
        )
        layout.add_widget(self.label_hasil)

        # =====================
        # MASUKKAN KE ROOT
        # =====================
        root.add_widget(layout)

        # =====================
        # TOMBOL BACK (KANAN BAWAH)
        # =====================
        btn_back = Button(
            text="BACK",
            color=(0, 0, 0, 1),
            font_size=sp(18),
            font_name = "Voyage Rush.otf",
            size_hint=(None, None),
            size=(dp(120), dp(50)),
            background_color= (1, 1, 1, 1),
            background_down="",
            background_normal="",
            pos_hint={"right": 0.95, "y": 0.05}
        )
        btn_back.bind(on_release=lambda x: setattr(self.manager, "current", "menu"))
        root.add_widget(btn_back)

        self.add_widget(root)

    # =====================
    # UPDATE BG
    # =====================
    def update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    # =====================
    # HITUNG LUAS
    # =====================
    def hitung_luas(self, instance):
        try:
            a = float(self.inputSisiAtas.text)
            b = float(self.inputSisiBawah.text)
            t = float(self.inputTinggi.text)
            luas = 0.5 * (a + b) * t
            self.label_hasil.text = f"Luas Trapesium: {luas:.2f}"
            self.label_hasil.color = (0, 0, 0, 1)
        except ValueError:
            self.label_hasil.text = "Input harus angka!"
            self.label_hasil.color = (1, 0, 0, 1)