from patterns.FactoryClass import FactoryConexao
from interface_cli.InterfaceCLI import InterfaceCLI
from patterns.StrateyClass import AvaliarClareza, AvaliadorComprimentoResposta
from patterns.ObserverClass import ClienteObserver, ProcessadorRespostasObserver
from rich.console import Console

if __name__ == "__main__":
    console = Console()
    cliente_observer = ClienteObserver()
    factory = FactoryConexao()
    interface = InterfaceCLI(factory)
    respostas = interface.criar_interface()

    # Estratégia de avaliação de comprimento de resposta
    
    console.print("-- Estratégia de avaliação de comprimento de resposta --", style="bold red")
    
    strategyAvaliarComprimento = AvaliadorComprimentoResposta()

    processador = ProcessadorRespostasObserver(strategyAvaliarComprimento)
    
    processador.adicionar_observer(cliente_observer)

    processador.processar(respostas)
    
    # Estratégia de avaliação de clareza de resposta
    
    console.print("-- Estratégia de avaliação de clareza de resposta --", style="bold red")
    
    strategyAvaliarClareza = AvaliarClareza()
    
    processador = ProcessadorRespostasObserver(strategyAvaliarClareza)

    processador.adicionar_observer(cliente_observer)

    processador.processar(respostas)
