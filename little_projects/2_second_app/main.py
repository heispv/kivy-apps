import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGrid, self).__init__(**kwargs)

        # Set number of columns
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text='First Name: '))
        # Add text input
        self.name = TextInput(multiline=True)
        self.add_widget(self.name)

        # Add widgets
        self.add_widget(Label(text='Last Name: '))
        # Add text input
        self.lastName = TextInput(multiline=True)
        self.add_widget(self.lastName)

        # Add widgets
        self.add_widget(Label(text='Email: '))
        # Add text input
        self.email = TextInput(multiline=True)
        self.add_widget(self.email)

        # Create submit button
        self.submit = Button(text='Submit', font_size=40)
        self.add_widget(self.submit)
        # Bind button to function
        self.submit.bind(on_press=self.press)
    
    # Create function to print text input
    def press(self, instance):
        name = self.name.text
        lastName = self.lastName.text
        email = self.email.text

        # print it to the next widget
        self.add_widget(Label(text=f'Hello {name} {lastName}! Your email is {email}'))

        # Clear text input
        self.name.text = ''
        self.lastName.text = ''
        self.email.text = ''


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()