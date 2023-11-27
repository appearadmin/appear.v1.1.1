from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window

Window.clearcolor = [147 / 255, 182 / 255, 124 / 255, 1]

class FirstPage(Screen):
    pass

class SecondPage(Screen):
    pass

class HomePage(Screen):
    pass

class WindowsManager(ScreenManager):
    pass
class MyApp(App):
    def build(self):
        return kv

kv = Builder.load_file("MyApp.kv")

MyApp().run()

