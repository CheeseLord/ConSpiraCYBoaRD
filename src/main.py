import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
#from kivy.uix.screenmanager import Screen
from kivy.uix.scatterlayout import ScatterLayout

kivy.require('2.0.0')


class ConspiracyBoard(ScatterLayout):
    pass

class ConspiracyBoardApp(App):
    def build(self):
        self.title = 'ConSpiraCYBoaRD'
        return ConspiracyBoard()


if __name__ == '__main__':
    ConspiracyBoardApp().run()

