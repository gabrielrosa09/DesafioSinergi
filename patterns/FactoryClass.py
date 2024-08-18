from abc import ABC, abstractmethod
from senha import API_KEY
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import requests, json
from rich.console import Console
from rich.text import Text

# Instanciando a classe Console
console = Console()

# Classe abstrata ConexaoLLM
class ConexaoLLM(ABC):
    
    @abstractmethod
    def conectar(self, prompt: str) -> str:
        pass
    
# Classe ConexaoGPT que herda de ConexaoLLM
class ConexaoGPT(ConexaoLLM):
    
    def conectar(self, prompt: str) -> str:
        
        try:
            # Carregando o modelo e o tokenizador
            model = GPT2LMHeadModel.from_pretrained('gpt2')
            tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

            # Definindo o token de padding como o token de fim de sequência
            tokenizer.pad_token = tokenizer.eos_token
            
            # Codificando a entrada e gerando a saída do modelo GPT-2
            inputs = tokenizer.encode(prompt, return_tensors='pt', add_special_tokens=True, padding=True)
            
            # Criando a máscara de atenção para os tokens de padding
            # Foi necessário isso devido aos warings de FutureWarning
            attention_mask = inputs.ne(tokenizer.pad_token_id).long()
            
            # Gerando a saída do modelo GPT-2 com base na entrada e na máscara de atenção criada
            # Definindo o tamanho máximo da sequência de saída como 40
            # Definindo o número de sequências de saída como 1
            # Definindo o tamanho do n-grama sem repetição como 2
            # Definindo o token de padding como o token de fim de sequência
            outputs = model.generate(
                inputs, 
                max_length=40, 
                num_return_sequences=1, 
                no_repeat_ngram_size=2,
                attention_mask=attention_mask,
                pad_token_id=tokenizer.eos_token_id
            )
            
            # Decodificando a saída do modelo GPT-2
            # Pulando os tokens especiais e limpando os espaços de tokenização
            mensagem = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
            
            # Imprimindo a resposta do GPT-2
            console.print("\n[bold green]Resposta do GPT-2:[/bold green]")
            console.print(Text(mensagem, style="dim"))
            console.print("\n")
            
            return mensagem
        
        # Tratamento de exceções
        except Exception as e:
            console.print(f"[bold red]Erro na conexão com o GPT-2: {e}[/bold red]")
            return f"Erro: {str(e)}"
    
class ConexaoCohere(ConexaoLLM):
    
    def conectar(self, prompt: str) -> str:
        
        try:
            # Definindo o cabeçalho da requisição
            headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
            link = "https://api.cohere.com/v1/chat"
            
            # Definindo o corpo da mensagem
            body_mensagem = {
                "message": f"{prompt}",
                "connectors": [{"id": "web-search"}]
            }
            
            # Convertendo o corpo da mensagem para JSON
            body_mensagem = json.dumps(body_mensagem)

            # Realizando a requisição POST para o Cohere
            requisicao = requests.post(link, headers=headers, data=body_mensagem)
            
            # Verificando se a requisição foi bem sucedida
            requisicao.raise_for_status()
            
            # Convertendo a resposta da requisição para JSON
            mensagem = requisicao.json() 
            
            # Imprimindo a resposta do Cohere
            console.print("\n[bold cyan]Resposta do Cohere:[/bold cyan]")
            console.print(Text(mensagem["text"], style="dim"))
            console.print("\n")
            
            return mensagem["text"]
        
        # Tratamento do erro de conexão
        except requests.exceptions.HTTPError as http_err:
            console.print(f"[bold red]Erro HTTP na conexão com o Cohere: {http_err}[/bold red]")
            return f"Erro HTTP: {str(http_err)}"
        
        # Traamento do erro de requisição
        except requests.exceptions.RequestException as req_err:
            console.print(f"[bold red]Erro de requisição na conexão com o Cohere: {req_err}[/bold red]")
            return f"Erro de requisição: {str(req_err)}"
        
        # Tratamento do erro de chave
        except KeyError as key_err:
            console.print(f"[bold red]Erro ao processar a resposta do Cohere: {key_err}[/bold red]")
            return f"Erro na resposta: {str(key_err)}"
        
        # Tratamento de exceções
        except Exception as e:
            console.print(f"[bold red]Erro na conexão com o Cohere: {e}[/bold red]")
            return f"Erro: {str(e)}"
        
        
        
class FactoryConexao:
    
    def criar_conexao(self, model_name: str) -> ConexaoLLM:
        
        try:
            # Verificando o modelo a ser utilizado
            if model_name == 'gpt2':
                return ConexaoGPT()
            elif model_name == 'cohere':
                return ConexaoCohere()
            else:
                raise ValueError(f"Modelo {model_name} não suportado")
        
        # Tratamento de exceções
        except Exception as e:
            console.print(f"[bold red]Erro ao criar conexão: {e}[/bold red]")
            raise
        