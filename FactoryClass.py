from abc import ABC, abstractmethod
from senha import API_KEY
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import requests, json
from rich.console import Console
from rich.text import Text

console = Console()

class ConexaoLLM(ABC):
    
    @abstractmethod
    def conectar(self, prompt: str) -> str:
        pass
    
class ConexaoGPT(ConexaoLLM):
    
    def conectar(self, prompt: str) -> str:
        
        try:
            model = GPT2LMHeadModel.from_pretrained('gpt2')
            tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

            tokenizer.pad_token = tokenizer.eos_token
            
            inputs = tokenizer.encode(prompt, return_tensors='pt', add_special_tokens=True, padding=True)
            
            attention_mask = inputs.ne(tokenizer.pad_token_id).long()
            
            outputs = model.generate(
                inputs, 
                max_length=40, 
                num_return_sequences=1, 
                no_repeat_ngram_size=2,
                attention_mask=attention_mask,
                pad_token_id=tokenizer.eos_token_id
            )

            mensagem = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)
            
            console.print("\n[bold green]Resposta do GPT-2:[/bold green]")
            console.print(Text(mensagem, style="dim"))
            console.print("\n")
            
            return mensagem
        
        except Exception as e:
            console.print(f"[bold red]Erro na conexão com o GPT-2: {e}[/bold red]")
            return f"Erro: {str(e)}"
    
class ConexaoCohere(ConexaoLLM):
    
    def conectar(self, prompt: str) -> str:
        
        try:
            headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
            link = "https://api.cohere.com/v1/chat"
            
            body_mensagem = {
                "message": f"{prompt}",
                "connectors": [{"id": "web-search"}]
            }
            
            body_mensagem = json.dumps(body_mensagem)

            requisicao = requests.post(link, headers=headers, data=body_mensagem)
            requisicao.raise_for_status()
            
            mensagem = requisicao.json() 
            
            console.print("\n[bold cyan]Resposta do Cohere:[/bold cyan]")
            console.print(Text(mensagem["text"], style="dim"))
            console.print("\n")
            
            return mensagem["text"]
        
        except requests.exceptions.HTTPError as http_err:
            console.print(f"[bold red]Erro HTTP na conexão com o Cohere: {http_err}[/bold red]")
            return f"Erro HTTP: {str(http_err)}"
        
        except requests.exceptions.RequestException as req_err:
            console.print(f"[bold red]Erro de requisição na conexão com o Cohere: {req_err}[/bold red]")
            return f"Erro de requisição: {str(req_err)}"
        
        except KeyError as key_err:
            console.print(f"[bold red]Erro ao processar a resposta do Cohere: {key_err}[/bold red]")
            return f"Erro na resposta: {str(key_err)}"
        
        except Exception as e:
            console.print(f"[bold red]Erro na conexão com o Cohere: {e}[/bold red]")
            return f"Erro: {str(e)}"
        
        
        
class FactoryConexao:
    
    def criar_conexao(self, model_name: str) -> ConexaoLLM:
        
        try:
            if model_name == 'gpt2':
                return ConexaoGPT()
            elif model_name == 'cohere':
                return ConexaoCohere()
            else:
                raise ValueError(f"Modelo {model_name} não suportado")
        
        except Exception as e:
            console.print(f"[bold red]Erro ao criar conexão: {e}[/bold red]")
            raise
        