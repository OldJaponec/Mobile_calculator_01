from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

from kivy.core.window import Window
from kivy.config import Config

width = Window.size[0]
height = Window.size[1]
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', width)
Config.set('graphics', 'height', height)


class Calculator(App):

    def del_num(self, instanse):
        self.lbl.text = self.lbl.text[:-1]
        self.formula = self.formula[:-1]

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instanse):
        if self.formula == '0':
            self.formula = ''

        self.formula += str(instanse.text)
        self.update_label()

    def operation(self, instanse):
        self.formula += str(instanse.text)
        self.formula = self.formula.replace('x', '*')
        self.update_label()

    def equals(self, instanse):
        while self.formula[-1] in '+-x*':
            self.formula = self.formula[:-1]
        # self.equals(instanse)
        self.lbl.text = str(eval(self.formula))
        self.formula = self.lbl.text

    def build(self):
        self.formula = '0'

        bl = BoxLayout(orientation='vertical', padding=[50], spacing=60)
        gl = GridLayout(cols=4, spacing=5, size_hint=(1, .8))

        self.lbl = Label(text='0', font_size=40, halign='right', size_hint=(1, .4), text_size=(300, 100))

        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='7', background_color=[.47, .90, .80, 1], on_press=self.add_number))
        gl.add_widget(Button(text='8', background_color=[.47, .90, .80, 1], on_press=self.add_number))
        gl.add_widget(Button(text='9', background_color=[.47, .90, .80, 1], on_press=self.add_number))
        gl.add_widget(Button(text='x', background_color=[.43, .47, .87, 1], on_press=self.operation))

        gl.add_widget(Button(text='4', background_color=[.47, .90, .80, 1], on_press=self.add_number))
        gl.add_widget(Button(text='5', background_color=[.47, .90, .80, 1], on_press=self.add_number))
        gl.add_widget(Button(text='6', background_color=[.47, .90, .80, 1], on_press=self.add_number))
        gl.add_widget(Button(text='-', background_color=[.43, .47, .87, 1], on_press=self.operation))

        gl.add_widget(Button(text='1', background_color=[.47, .90, .80, 1], on_press=self.add_number))
        gl.add_widget(Button(text='2', background_color=[.47, .90, .80, 1], on_press=self.add_number))
        gl.add_widget(Button(text='3', background_color=[.47, .90, .80, 1], on_press=self.add_number))
        gl.add_widget(Button(text='+', background_color=[.43, .47, .87, 1], on_press=self.operation))

        gl.add_widget(Button(text='<<', background_color=[.87, .43, .43, 1], on_press=self.del_num))
        gl.add_widget(Button(text='0', background_color=[.47, .90, .80, 1], on_press=self.add_number))
        gl.add_widget(Button(text='.', background_color=[.47, .90, .80, 1], on_press=self.operation))
        gl.add_widget(Button(text='=', background_color=[.43, .47, .87, 1], on_press=self.equals))

        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    print(width)
    print(height)
    Calculator().run()