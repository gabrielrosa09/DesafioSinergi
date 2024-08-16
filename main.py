from FactoryClass import FactoryConexao
from InterfaceCLI import InterfaceCLI
from StrateyClass import AvaliarClareza, AvaliadorComprimentoResposta
from ObserverClass import ClienteObserver, ProcessadorRespostasObserver

if __name__ == "__main__":
    cliente_observer = ClienteObserver()
    factory = FactoryConexao()
    interface = InterfaceCLI(factory)
    respostas = interface.criar_interface()

    # Estratégia de avaliação de comprimento de resposta
    
    strategyAvaliarComprimento = AvaliadorComprimentoResposta()

    processador = ProcessadorRespostasObserver(strategyAvaliarComprimento)
    
    processador.adicionar_observer(cliente_observer)

    processador.processar(respostas)
    
    # Estratégia de avaliação de clareza de resposta
    
    strategyAvaliarClareza = AvaliarClareza()
    
    processador = ProcessadorRespostasObserver(strategyAvaliarClareza)

    processador.adicionar_observer(cliente_observer)

    processador.processar(respostas)
