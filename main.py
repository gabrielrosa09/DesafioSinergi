from FactoryClass import FactoryConexao
from InterfaceCLI import InterfaceCLI
from StrateyClass import AvaliarClareza, ProcessadorRespostas

if __name__ == "__main__":
    factory = FactoryConexao()
    cli = InterfaceCLI(factory)
    
    respostas = cli.criar_interface()
    
    # Avaliar clareza
    avaliador_clareza = AvaliarClareza()
    processador_clareza = ProcessadorRespostas(avaliador_clareza)
    melhor_resposta_clareza = processador_clareza.processar(respostas)
    print(f"Melhor resposta com base na clareza: {melhor_resposta_clareza}")