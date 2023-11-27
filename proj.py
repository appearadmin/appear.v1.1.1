from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.core.window import Window
Window.size = (310, 580)
class Login(FloatLayout):
    screen_mngr = ObjectProperty(None)

class AppEar(MDApp):
    def build(self):
        return Builder.load_file("AppEar.kv")
    
AppEar().run()






