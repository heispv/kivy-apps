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
        self.cols = 1

        # Create a second grid layout
        self.top_grid = GridLayout()
        # Set number of columns
        self.top_grid.cols = 2

        ############################################
        ################# Top grid #################
        # Add widgets
        self.top_grid.add_widget(Label(text='First Name: '))
        # Add text input
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)

        # Add widgets
        self.top_grid.add_widget(Label(text='Last Name: '))
        # Add text input
        self.lastName = TextInput(multiline=True)
        self.top_grid.add_widget(self.lastName)

        # Add widgets
        self.top_grid.add_widget(Label(text='Email: '))
        # Add text input
        self.email = TextInput(multiline=True)
        self.top_grid.add_widget(self.email)

        # Add top_grid to MyGrid
        self.add_widget(self.top_grid)

        ############################################
        ################ Bottom grid ###############

        self.bottum_grid = GridLayout()
        # Set number of columns
        self.bottum_grid.cols = 3

        # Create Label
        self.bottum_grid.add_widget(Label())

        # Create submit button
        self.submit = Button(text='Submit', font_size=40)
        self.bottum_grid.add_widget(self.submit)
        # Bind button to function
        self.submit.bind(on_press=self.press)

        # Create Label
        self.bottum_grid.add_widget(Label())

        # Add bottum_grid to MyGrid
        self.add_widget(self.bottum_grid)
        
        # The output of the function will be printed in the screen
        self.output = Label(text='')
        self.add_widget(self.output)

        # Adjust the size of the top_grid row
        self.top_grid.size_hint_y = 3

    # Create function to print text input
    def press(self, instance):
        name = self.name.text
        lastName = self.lastName.text
        email = self.email.text

        # Print the text input in the self.output label
        self.output.text = 'Hello ' + name + ' ' + lastName + ' ' + email
        

        # Clear text input
        self.name.text = ''
        self.lastName.text = ''
        self.email.text = ''


class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()