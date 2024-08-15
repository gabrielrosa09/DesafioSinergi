from FactoryClass import FactoryConexao
from InterfaceCLI import InterfaceCLI
from StrateyClass import AvaliarClareza, AvaliadorComprimentoResposta
from ObserverClass import ClienteObserver, ProcessadorRespostasObserver

if __name__ == "__main__":
    factory = FactoryConexao()
    interface = InterfaceCLI(factory)
    respostas = interface.criar_interface()

    # strategy = AvaliarClareza()
    strategy = AvaliadorComprimentoResposta()

    processador = ProcessadorRespostasObserver(strategy)
    cliente_observer = ClienteObserver()

    processador.adicionar_observer(cliente_observer)

    processador.processar(respostas)
