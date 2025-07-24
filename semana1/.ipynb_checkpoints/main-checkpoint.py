import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display
import ollama
print("Ollama instalado correctamente")

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3"

# Crea una lista de mensajes utilizando el mismo formato que usamos para OpenAI

messages = [
    {"role": "user", "content": "Describe algunas de las aplicaciones comerciales de la IA generativa."}
]

payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

response = ollama.chat(model=MODEL, messages=messages)

print(response['message']['content'])