from transformers import T5Tokenizer, T5ForConditionalGeneration
from senha import API_KEY
import requests, json

# Conectar a API do Cohere

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.cohere.com/v1/chat"

body_mensagem = {
    "message": "Oi, cohere! Quem inventou a lampada?",
    "connectors": [{"id": "web-search"}]
  }

body_mensagem = json.dumps(body_mensagem)

requisicao = requests.post(link, headers=headers, data=body_mensagem)
mensagem = requisicao.json()  

print(mensagem["text"])

# Conectar a API do T5

# tokenizer = T5Tokenizer.from_pretrained("google-t5/t5-small")
# model = T5ForConditionalGeneration.from_pretrained("google-t5/t5-small")

# input_ids = tokenizer("The <extra_id_0> walks in <extra_id_1> park", return_tensors="pt").input_ids
# labels = tokenizer("<extra_id_0> cute dog <extra_id_1> the <extra_id_2>", return_tensors="pt").input_ids

# # the forward function automatically creates the correct decoder_input_ids
# loss = model(input_ids=input_ids, labels=labels).loss
# print(loss.item())
