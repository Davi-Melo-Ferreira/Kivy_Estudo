meu_app/
├── main.py              # Arquivo principal que roda o app e gerencia as telas
├── screens/             # Pasta com as classes Python que representam as telas 
│   ├── tela_login.py
│   ├── tela_menu.py
├── kv/                  # Pasta com os arquivos de layout (.kv) das telas
│   ├── tela_login.kv
│   ├── tela_menu.kv

ARQUIVO MAIN.PY

<from kivy.app import App>
Importa a classe base App. Tudo que você quiser que seja um aplicativo Kivy precisa herdar dela. Internamente, ela gerencia o ciclo de vida (inicialização, exibição e finalização) do seu app.

<from kivy.uix.screenmanager import ScreenManager>
O ScreenManager é um container que gerencia múltiplas telas. Ele não exibe tudo ao mesmo tempo — mostra apenas uma tela ativa e oculta as outras.

<from screens.tela_login import TelaLogin
from screens.tela_menu import TelaMenu>
Essas são suas telas personalizadas, que herdam da classe Screen. Elas ficam na pasta screens/ e contêm a lógica Python de cada tela.

<from kivy.lang import Builder
import os>
Builder é responsável por carregar os arquivos .kv, que contêm os layouts declarativos. O os é usado para construir caminhos relativos (evita erros em diferentes SOs).

<class MeuApp(App):
    def build(self):
        Builder.load_file(os.path.join('kv', 'tela_login.kv'))
        Builder.load_file(os.path.join('kv', 'tela_menu.kv'))
        sm = ScreenManager()
        sm.add_widget(TelaLogin(name='login'))
        sm.add_widget(TelaMenu(name='menu'))
        return sm

Aqui o <Builder.load_file(...)> lê o layout visual de cada tela. Isso é obrigatório quando você separa os arquivos .kv, pois o Kivy não os detecta automaticamente se estiverem em subpastas.

Em seguida cria uma instância de ScreenManager, adiciona cada tela com um nome interno (name='login') que será usado para a navegação (manager.current = 'menu'), e retorna o ScreenManager como raiz do app.

TELA LOGIN.PY

from kivy.uix.screenmanager import Screen

class TelaLogin(Screen):
    pass
Cada classe aqui herda de Screen, que é uma tela do Kivy gerenciada pelo ScreenManager. O pass significa que a lógica da interface está toda no .kv.

TELA LOGIN.KV

<TelaLogin>:
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 10
<TelaLogin> conecta esse layout à classe TelaLogin do Python. O conteúdo interno é o layout da tela.
BoxLayout organiza elementos em linha ou em coluna.

        Label:
            text: 'Tela de Login'
            font_size: 32
            # Exibe texto. Usado para títulos, informações etc.

        TextInput:
            id: usuario
            hint_text: 'Usuário'
            # Campo de entrada de texto. O id é crucial: ele permite acessar esse #widget do Python via self.ids.usuario.

        Button:
            text: 'Entrar'
            on_press:
                root.manager.current = 'menu'
Cria um botão. O on_press executa código Python quando clicado.
root representa a instância da tela (TelaLogin) onde esse botão está.
root.manager.current = 'menu' troca para a tela com name='menu'.

TELA MENU.KV

<TelaMenu>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'Bem-vindo à menu!'
        Button:
            text: 'Voltar'
            on_press: root.manager.current = 'login'

Como tudo se conecta internamente:
O main.py carrega os layouts .kv
Cria e registra telas (TelaLogin, TelaMenu) dentro do ScreenManager
Cada tela é associada ao seu layout via <NomeDaClasse> no .kv
Os widgets com id: podem ser acessados no Python usando self.ids.nome
A navegação entre telas acontece via root.manager.current = 'nome'