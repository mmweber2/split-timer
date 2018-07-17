from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class EventWidget(Widget):
    pass

class TimerBoxWidget(Widget):
    pass

class SplitTimer(App):
    """"""

    def build(self):
        return TimerBoxWidget()

if __name__ == '__main__':
    SplitTimer().run()