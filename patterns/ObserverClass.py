from abc import ABC, abstractmethod
from patterns.StrateyClass import AvaliadorStrategy
from rich.console import Console
from rich.text import Text

console = Console()

# Classe abstrata Observer
class Observer(ABC):
    
    @abstractmethod
    def atualizar(self, resposta: str, explicacao: str):
        pass

# Classe ProcessadorRespostasObserver
class ProcessadorRespostasObserver:
    def __init__(self, strategy: AvaliadorStrategy):
        self.strategy = strategy
        self.observers = []
    
    def adicionar_observer(self, observer: Observer):
        # Adiciona um observer à lista de observers
        self.observers.append(observer)
    
    def remover_observer(self, observer: Observer):
        # Remove um observer da lista de observers
        self.observers.remove(observer)
    
    def notificar_observers(self, resposta: str, explicacao: str):
        # Notifica todos os observers da lista
        for observer in self.observers:
            observer.atualizar(resposta, explicacao)
    
    def processar(self, respostas: list) -> str:
        # Avalia as respostas
        melhor_resposta = self.strategy.avaliar(respostas)
        # Gera a explicação
        explicacao = self.gerar_explicacao(melhor_resposta)
        # Notifica os observers
        self.notificar_observers(melhor_resposta, explicacao)
        return melhor_resposta
    
    # Método para gerar a explicação
    def gerar_explicacao(self, melhor_resposta: str) -> str:
        return f"\nA resposta escolhida é a do modelo {melhor_resposta[0]} porque atendeu melhor ao critério selecionado.\n"
    
class ClienteObserver(Observer):
    def atualizar(self, resposta: str, explicacao: str):
        # Extrai a string da resposta de uma tuple
        modelo, conteudo_resposta = resposta  
        
        # Imprime a resposta e a explicação
        console.print("\n[bold magenta]Nova resposta selecionada:[/bold magenta]")
        console.print(Text(conteudo_resposta, style="italic")) 
        console.print("\n[bold yellow]Explicação:[/bold yellow]")
        console.print(Text(explicacao, style="italic"))
