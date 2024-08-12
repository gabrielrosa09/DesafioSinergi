from senha import API_KEY
import requests, json, cohere

co = cohere.Client(API_KEY)

response = co.chat(
	message=""
)

print(response)
