from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty


class MeuLayout(GridLayout): # classe para definir a estética do a GUI
    def __init__(self, **kwargs):
        super(MeuLayout, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label (text='ENTRADA'))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Button (text='ENTRADA'))
        


class MeuApp(App):
    def build(self):
        return MeuLayout()
   
if __name__ == '__main__':
    MeuApp().run()



class MeuApp(App):
    def build(self):
        return MeuLayout()
    
if __name__ == '__main__':
    MeuApp().run()