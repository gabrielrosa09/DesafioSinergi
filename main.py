from FactoryClass import FactoryConexao
from InterfaceCLI import InterfaceCLI
from StrateyClass import AvaliarClareza, AvaliadorComprimentoResposta, ProcessadorRespostas

if __name__ == "__main__":
    factory = FactoryConexao()
    cli = InterfaceCLI(factory)
    
    respostas = cli.criar_interface()
    
    avaliador_clareza = AvaliarClareza()
    processador_clareza = ProcessadorRespostas(avaliador_clareza)
    melhor_resposta_clareza = processador_clareza.processar(respostas)
    print(f"Melhor resposta com base na clareza: {melhor_resposta_clareza}")
    
    avaliador_comprimento = AvaliadorComprimentoResposta()
    processador_comprimento = ProcessadorRespostas(avaliador_comprimento)
    resposta_maior_comprimento = processador_comprimento.processar(respostas)
    print(f'Melhor resposta com base no comprimento: {resposta_maior_comprimento}')