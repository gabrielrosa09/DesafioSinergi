from FactoryClass import FactoryConexao
from InterfaceCLI import InterfaceCLI

if __name__ == "__main__":
    factory = FactoryConexao()
    cli = InterfaceCLI(factory)
    
    cli.criar_interface()
    