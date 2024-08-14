from abc import ABC, abstractmethod
from FactoryClass import ConexaoLLM

class CommandClass(ABC):
    
    @abstractmethod
    def enviar_prompt(self) -> str:
        pass
    
class EncapsularPrompt(CommandClass):
    def __init__(self, conexao: ConexaoLLM, prompt: str):
        self.conexao = conexao
        self.prompt = prompt
    
    def enviar_prompt(self) -> str:
        return self.conexao.conectar(self.prompt)
