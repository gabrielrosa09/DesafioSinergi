from abc import ABC, abstractmethod
from senha import API_KEY
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import requests, json

class ConexaoLLM(ABC):
    
    @abstractmethod
    def conectar(self, prompt: str) -> str:
        pass
    
class ConexaoGPT(ConexaoLLM):
    
    def conectar(self, prompt: str) -> str:
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
        
        print(f"Reposta do GPT-2: {mensagem}")
        print(f"#############################")
        
        return mensagem
    
class ConexaoCohere(ConexaoLLM):
    
    def conectar(self, prompt: str) -> str:
        headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        link = "https://api.cohere.com/v1/chat"
        
        body_mensagem = {
            "message": f"{prompt}",
            "connectors": [{"id": "web-search"}]
        }
        
        body_mensagem = json.dumps(body_mensagem)

        requisicao = requests.post(link, headers=headers, data=body_mensagem)
        mensagem = requisicao.json() 
        
        print(f"Reposta do Cohere: " + mensagem["text"])
        
        return mensagem["text"]
        
        
        
class FactoryConexao:
    def criar_conexao(self, model_name: str) -> ConexaoLLM:
        if model_name == 'gpt2':
            return ConexaoGPT()
        elif model_name == 'cohere':
            return ConexaoCohere()
        else:
            raise ValueError(f"Modelo {model_name} não suportado")
        
        
# factory = FactoryConexao()

# Para usar o GPT-2:
# conexao_gpt = factory.criar_conexao('gpt2')
# resposta_gpt = conexao_gpt.conectar("What is the capital of Germany?")
# print(resposta_gpt)

# Para usar a API da Cohere:
# conexao_cohere = factory.criar_conexao('cohere')
# resposta_cohere = conexao_cohere.conectar("What is the capital of Germany?")
# print(resposta_cohere)
