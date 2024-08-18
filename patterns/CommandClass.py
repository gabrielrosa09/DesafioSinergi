from abc import ABC, abstractmethod
from patterns.FactoryClass import ConexaoLLM

# Classe abstrata CommandClass
class CommandClass(ABC):
    
    @abstractmethod
    def enviar_prompt(self) -> str:
        pass
    
# Classe EncapsularPrompt que herda de CommandClass
class EncapsularPrompt(CommandClass):
    def __init__(self, conexao: ConexaoLLM, prompt: str):
        self.conexao = conexao
        self.prompt = prompt
    
    def enviar_prompt(self) -> str:
        # Chamando o método conectar da classe ConexaoLLM
        return self.conexao.conectar(self.prompt)
