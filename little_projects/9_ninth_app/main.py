import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window


# Load kv file
Builder.load_file('add_image.kv')

kivy.require('1.9.0')

class MyRoot(Widget):
  pass


class MyApplication(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        return MyRoot()

if __name__ == '__main__':
    MyApplication().run()