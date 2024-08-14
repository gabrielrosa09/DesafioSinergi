from FactoryClass import FactoryConexao
from CommandClass import EncapsularPrompt

class InterfaceCLI:
    def __init__(self, factory: FactoryConexao):
        self.factory = factory
        
    def criar_interface(self):
        print("# ------------------- #")
        print(" Bem-vindo ao ChatBot! ")
        print("# ------------------- #")
        prompt = input("Digite o prompt: ")
        modelos = ['gpt2', 'cohere']
        respostas = []
        
        for modelo in modelos:
            conexao = self.factory.criar_conexao(modelo)
            comando = EncapsularPrompt(conexao, prompt)
            resposta = comando.enviar_prompt()
            respostas.append((modelo, resposta))
        
        return respostas
        