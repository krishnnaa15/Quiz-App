from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder

class HomePage(Screen):
    pass
    
class Q1(Screen):
    pass

class Q2(Screen):
    pass

class Q3(Screen):
    pass

class Q4(Screen):
    pass

class Q5(Screen):
    pass

class Q6(Screen):
    pass

class Q7(Screen):
    pass

class Q8(Screen):
    pass

class Q9(Screen):
    pass

class Q10(Screen):
    pass

class FinalPage(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

file=Builder.load_file('kivy.kv')

class QuizApp(App):
    def build(self):
        return file

QuizApp().run()
