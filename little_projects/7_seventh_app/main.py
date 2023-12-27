import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# Load kv file
Builder.load_file('label_color.kv')

kivy.require('1.9.0')

class MyRoot(Widget):
  pass


class MyApplication(App):
    def build(self):
        return MyRoot()

if __name__ == '__main__':
    MyApplication().run()