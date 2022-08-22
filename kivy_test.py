#this si a test
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout

Config.set("graphics", "width", "500")
Config.set("graphics", "height", "300")

kv = """
<RoundedCornerLayout@FloatLayout>:
    background_color: 0,0,0,0
    canvas.before:
        Color:
            rgba: (.4,.4,.4,1)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [(40, 40), (40, 40), (20, 20), (20, 20)]
"""

Builder.load_string(kv)


class RoundedCornerLayout(FloatLayout):
    def __init__(self):
        super().__init__()
        self.size_hint = (None, None)
        self.size = (400, 200)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}


class MainApp(App):
    def build(self):
        return RoundedCornerLayout()


if __name__ == "__main__":
    MainApp().run()

