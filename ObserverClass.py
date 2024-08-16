from abc import ABC, abstractmethod
from StrateyClass import AvaliadorStrategy

class Observer(ABC):
    
    @abstractmethod
    def atualizar(self, resposta: str, explicacao: str):
        pass

class ProcessadorRespostasObserver:
    def __init__(self, strategy: AvaliadorStrategy):
        self.strategy = strategy
        self.observers = []
    
    def adicionar_observer(self, observer: Observer):
        self.observers.append(observer)
    
    def remover_observer(self, observer: Observer):
        self.observers.remove(observer)
    
    def notificar_observers(self, resposta: str, explicacao: str):
        for observer in self.observers:
            observer.atualizar(resposta, explicacao)
    
    def processar(self, respostas: list) -> str:
        melhor_resposta = self.strategy.avaliar(respostas)
        explicacao = self.gerar_explicacao(melhor_resposta)
        self.notificar_observers(melhor_resposta, explicacao)
        return melhor_resposta
    
    def gerar_explicacao(self, melhor_resposta: str) -> str:
        return f"\nA resposta escolhida é a do modelo {melhor_resposta[0]} porque atendeu melhor ao critério selecionado."
    
class ClienteObserver(Observer):
    def atualizar(self, resposta: str, explicacao: str):
        print("\nNova resposta selecionada:")
        print(resposta)
        print("\nExplicação:")
        print(explicacao)
