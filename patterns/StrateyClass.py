from abc import ABC, abstractmethod
from textstat import textstat

# Classe abstrata AvaliadorStrategy
class AvaliadorStrategy(ABC):
    @abstractmethod
    def avaliar(self, respostas: list) -> str:
        pass
    
# Classes AvaliarClareza que herda de AvaliadorStrategy
class AvaliarClareza(AvaliadorStrategy):
    def avaliar(self, respostas: list) -> str:
        melhor_resposta = None
    
        # Inicializando a variável melhor_clareza como infinito para comparação
        melhor_clareza = float('inf')
        
        # Iterando sobre as respostas
        for modelo, resposta in respostas:
            # Calculando a clareza da resposta
            clareza = self.calcular_clareza(resposta)
            # Verificando se a clareza da resposta é menor que a melhor clareza
            if clareza < melhor_clareza:
                melhor_clareza = clareza
                melhor_resposta = (modelo, resposta)
        
        return melhor_resposta
    
    def calcular_clareza(self, texto: str) -> float:
        # Calculando a clareza do texto com a função flesch_reading_ease da biblioteca textstat
        return textstat.flesch_reading_ease(texto)
  
# Classe AvaliadorComprimentoResposta que herda de AvaliadorStrategy  
class AvaliadorComprimentoResposta(AvaliadorStrategy):
    def avaliar(self, respostas: list) -> str:
        melhor_resposta = None
        maior_comprimento = 0
        
        # Iterando sobre as respostas
        for modelo, resposta in respostas:
            comprimento = len(resposta)
            
            # Verificando se o comprimento da resposta é maior que o maior comprimento
            if comprimento > maior_comprimento:
                maior_comprimento = comprimento
                melhor_resposta = (modelo, resposta)
        
        return melhor_resposta

class ProcessadorRespostasStrategy:
    def __init__(self, strategy: AvaliadorStrategy):
        self.strategy = strategy
    
    def processar(self, respostas: list) -> str:
        # Avalia as respostas
        return self.strategy.avaliar(respostas)