
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from runner import KhanjarRunner

class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.status = Label(text='Stopped')
        self.add_widget(self.status)
        self.runner = KhanjarRunner(self.update_status)
        self.btn = Button(text='START')
        self.btn.bind(on_press=self.toggle)
        self.add_widget(self.btn)

    def toggle(self, *_):
        if self.runner.running:
            self.runner.stop()
            self.btn.text = 'START'
        else:
            self.runner.start()
            self.btn.text = 'STOP'

    def update_status(self, txt):
        self.status.text = txt

class KhanjarApp(App):
    def build(self):
        return MainUI()

if __name__ == '__main__':
    KhanjarApp().run()
