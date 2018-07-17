from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class SplitTimer(App):

    def build(self):
        main_layout = BoxLayout(orientation='vertical')
        # Build title bar
        main_layout.add_widget(Label(text='Game Name Here'))
        # Build menu bar
        menu_layout = BoxLayout(orientation='horizontal')
        menu_layout.add_widget(Button(text='Split'))
        menu_layout.add_widget(Button(text='Edit Splits'))
        menu_layout.add_widget(Button(text='Edit Game Info'))
        main_layout.add_widget(menu_layout)
        # Build event list
        event_layout = BoxLayout(orientation='vertical')
        # TODO: Replace with events
        for i in xrange(4):
            event_layout.add_widget(Label(text='Event #%s' % (i + 1)))
        main_layout.add_widget(event_layout)
        return main_layout


if __name__ == '__main__':
    SplitTimer().run()