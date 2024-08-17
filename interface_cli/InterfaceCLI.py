from patterns.FactoryClass import FactoryConexao
from patterns.CommandClass import EncapsularPrompt
from rich.console import Console
from rich.console import Console

console = Console()


class InterfaceCLI:
    def __init__(self, factory: FactoryConexao):
        self.factory = factory
        
    def criar_interface(self):
        console.print("# ------------------- #", style="bold blue")
        console.print(" Bem-vindo ao ChatBot! ", style="bold blue")
        console.print("# ------------------- #", style="bold blue")
        prompt = console.input("Digite o prompt: ")
        modelos = ['gpt2', 'cohere']
        respostas = []
        
        for modelo in modelos:
            conexao = self.factory.criar_conexao(modelo)
            comando = EncapsularPrompt(conexao, prompt)
            resposta = comando.enviar_prompt()
            respostas.append((modelo, resposta))
        
        return respostas
        