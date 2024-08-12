from senha import API_KEY
import requests, json, cohere

co = cohere.Client(API_KEY)

response = co.chat(
	message="hello world!"
)

print(response)

# headers = {
#     "Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"
# }

# link = "https://api.openai.com/v1/chat/completions"
# id_modelo = "gpt-3.5-turbo"

# body_mensagem = {
#     "model": id_modelo,
#     "message": [{"role": "user", "content": "escreva um email para o meu chefe sobre a previsão do dolar nos proximos 2 meses."}]
# }

# body_mensagem = json.dumps(body_mensagem)

# requisicao = requests.post(link, headers=headers, data=body_mensagem)

# print(requisicao)
# print(requisicao.text)

# resposta = requisicao.json()
# mensagem = resposta["choices"][0]["message"]["content"]