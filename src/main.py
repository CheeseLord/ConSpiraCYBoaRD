import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

kivy.require('2.0.0')


class FooScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        return Builder.load_file('data/test1.kv')
        #return Label(text='Hello, world!')


if __name__ == '__main__':
    MyApp().run()

