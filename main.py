from patterns.FactoryClass import FactoryConexao
from interface_cli.InterfaceCLI import InterfaceCLI
from patterns.StrateyClass import AvaliarClareza, AvaliadorComprimentoResposta
from patterns.ObserverClass import ClienteObserver, ProcessadorRespostasObserver
from rich.console import Console

if __name__ == "__main__":
    # Inicialização dos objetos
    console = Console()
    cliente_observer = ClienteObserver()
    factory = FactoryConexao()
    interface = InterfaceCLI(factory)
    respostas = interface.criar_interface()

    # Estratégia de avaliação de comprimento de resposta
    
    console.print("-- Estratégia de avaliação de comprimento de resposta --", style="bold red")
    
    # Inicializando a estratégia de avaliação de comprimento de resposta
    strategyAvaliarComprimento = AvaliadorComprimentoResposta()

    # Inicializando o processador de respostas
    processador = ProcessadorRespostasObserver(strategyAvaliarComprimento)
    
    # Adicionando o observer
    processador.adicionar_observer(cliente_observer)

    # Processando as respostas
    processador.processar(respostas)
    
    # Estratégia de avaliação de clareza de resposta
    
    console.print("-- Estratégia de avaliação de clareza de resposta --", style="bold red")
    
    # Inicializando a estratégia de avaliação de clareza de resposta
    strategyAvaliarClareza = AvaliarClareza()
    
    # Inicializando o processador de respostas
    processador = ProcessadorRespostasObserver(strategyAvaliarClareza)

    # Adicionando o observer
    processador.adicionar_observer(cliente_observer)

    # Processando as respostas
    processador.processar(respostas)
