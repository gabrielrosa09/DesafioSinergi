from abc import ABC, abstractmethod
from textstat import textstat

class AvaliadorStrategy(ABC):
    @abstractmethod
    def avaliar(self, respostas: list) -> str:
        pass
    
class AvaliarClareza(AvaliadorStrategy):
    def avaliar(self, respostas: list) -> str:
        melhor_resposta = None
        melhor_clareza = float('inf')
        
        for modelo, resposta in respostas:
            clareza = self.calcular_clareza(resposta)
            if clareza < melhor_clareza:
                melhor_clareza = clareza
                melhor_resposta = (modelo, resposta)
        
        return melhor_resposta
    
    def calcular_clareza(self, texto: str) -> float:
        return textstat.flesch_reading_ease(texto)
    
class AvaliadorComprimentoResposta(AvaliadorStrategy):
    def avaliar(self, respostas: list) -> str:
        melhor_resposta = None
        maior_comprimento = 0
        
        for modelo, resposta in respostas:
            comprimento = len(resposta)
            
            if comprimento > maior_comprimento:
                maior_comprimento = comprimento
                melhor_resposta = (modelo, resposta)
        
        return melhor_resposta

class ProcessadorRespostasStrategy:
    def __init__(self, strategy: AvaliadorStrategy):
        self.strategy = strategy
    
    def processar(self, respostas: list) -> str:
        return self.strategy.avaliar(respostas)