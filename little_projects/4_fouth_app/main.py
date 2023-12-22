import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('myapplication.kv')

kivy.require('1.9.0')

class MyRoot(Widget):
   
    name = ObjectProperty(None)
    last_name = ObjectProperty(None)
    email = ObjectProperty(None)

    # Create function to print text input
    def press(self):
        name = self.name.text
        last_name = self.last_name.text
        email = self.email.text

        # Print the text input in the self.output label
        self.output.text = f"Hello {name} {last_name}, your email is {email}"

        # Clear text input
        self.name.text = ''
        self.last_name.text = ''
        self.email.text = ''


class MyApplication(App):
    def build(self):
        return MyRoot()

if __name__ == '__main__':
    MyApplication().run()