from patterns.FactoryClass import FactoryConexao
from patterns.CommandClass import EncapsularPrompt
from rich.console import Console
from rich.console import Console

console = Console()

# Classe InterfaceCLI que cria a interface de linha de comando
class InterfaceCLI:
    def __init__(self, factory: FactoryConexao):
        self.factory = factory
        
    def criar_interface(self):
        # Imprimindo a mensagem para o terminal
        console.print("# ------------------- #", style="bold blue")
        console.print(" Bem-vindo ao ChatBot! ", style="bold blue")
        console.print("# ------------------- #", style="bold blue")
        prompt = console.input("Digite o prompt: ")
        modelos = ['gpt2', 'cohere']
        respostas = []
        
        for modelo in modelos:
            # Criando a conexão
            conexao = self.factory.criar_conexao(modelo)
            # Encapsulando o prompt
            comando = EncapsularPrompt(conexao, prompt)
            # Enviando o prompt
            resposta = comando.enviar_prompt()
            # Adicionando a resposta à lista de respostas
            respostas.append((modelo, resposta))
        
        return respostas
        