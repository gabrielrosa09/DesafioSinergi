from senha import API_KEY
import requests, json

# Conectar a API do Cohere

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.cohere.com/v1/chat"

body_mensagem = {
    "message": "Oi, cohere! Qual a capital da França?",
    "connectors": [{"id": "web-search"}]
  }

body_mensagem = json.dumps(body_mensagem)

requisicao = requests.post(link, headers=headers, data=body_mensagem)
mensagem = requisicao.json()  

print(mensagem["text"])

# from transformers import AutoModelForCausalLM, AutoTokenizer

# # Carregando o modelo e o tokenizador
# model = AutoModelForCausalLM.from_pretrained("gpt2")
# tokenizer = AutoTokenizer.from_pretrained("gpt2")

# # Definindo a pergunta
# question = "What is the capital of France?"
# prompt = f"Question: {question} Answer:"

# # Convertendo o prompt em IDs de tokens
# input_ids = tokenizer(prompt, return_tensors="pt").input_ids

# # Gerando a resposta
# gen_tokens = model.generate(
#     input_ids,
#     do_sample=True,
#     temperature=0.9,
#     max_length=50,
#     pad_token_id=tokenizer.eos_token_id
# )
# gen_text = tokenizer.batch_decode(gen_tokens, skip_special_tokens=True)[0]

# print(gen_text)
