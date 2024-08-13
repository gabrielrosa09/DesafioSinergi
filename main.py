from senha import API_KEY
import requests, json

# Conectar a API do Cohere

# headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
# link = "https://api.cohere.com/v1/chat"

# body_mensagem = {
#     "message": "Oi, cohere! Qual a capital da França?",
#     "connectors": [{"id": "web-search"}]
#   }

# body_mensagem = json.dumps(body_mensagem)

# requisicao = requests.post(link, headers=headers, data=body_mensagem)
# mensagem = requisicao.json()  

# print(mensagem["text"])

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Carregar o modelo e o tokenizador do GPT-2
model_name = 'gpt2'  # Você pode usar 'gpt2-medium', 'gpt2-large', ou 'gpt2-xl' se precisar de modelos maiores
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Função para gerar resposta
def ask_gpt2(question):
    # Tokenizar a pergunta
    inputs = tokenizer.encode(question, return_tensors='pt')
    
    # Gerar a resposta
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
    
    # Decodificar e retornar a resposta
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Perguntar algo ao GPT-2
question = "What is the capital of Germany?"
answer = ask_gpt2(question)
print(f"Pergunta: {question}")
print(f"Resposta: {answer}")
