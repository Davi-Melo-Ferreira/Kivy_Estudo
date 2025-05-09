from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from telas.login import TelaLogin
from telas.menu import TelaMenu  # outra tela exemplo
from kivy.lang import Builder

class GerenciadorTelas(ScreenManager):
    pass

class MeuApp(App):
    def build(self):
        Builder.load_file(('kv\login.kv')) # lê o arquivo e compila o conteúdo
        Builder.load_file(('kv\menu.kv')) # para usar os wigdets, regras e etc.

        screen_manager = GerenciadorTelas()
        screen_manager.add_widget(TelaLogin(name='login'))#name tem q ser igual
        screen_manager.add_widget(TelaMenu(name='menu'))#ao root.manager do kv
        return screen_manager # retorna duas telas adicionadas à ScreenManager

if __name__ == '__main__':
    MeuApp().run()
