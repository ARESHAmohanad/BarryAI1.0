import nltk
import random
import requests
import json
from nltk.chat.util import Chat, reflections

API_KEY = "sk-proj-qDwNy8YneUOrhRLd86wZT3BlbkFJnuimG0T8yQPJU1RlOZFm"
API_URL = "https://api.openai.com/v1/engines/gpt-4/completions"

# Definindo pares de padroes e respostas
patterns = [
    (r'como posso me proteger contra (.*)',
    ['Voce pode se proteger contra {0} usando um bom software antivirus e mantendo seu sistema sempre atualizado.',
    'Certifique-se de ter um firewall ativo e evite clicar em links suspeitos ou baixar arquivos de fontes nao confiaveis.']),

    (r'eu fui hackeado',
    ['Sinto muito ouvir isso. Entre em contato com as autoridades de seguranca cibernetica imediatamente e altere suas senhas o mais rapido possivel.']),

    (r'(.*) (ataque|vulnerabilidade) (.*)',
    ['Voce pode aprender mais sobre {1} em sites confiaveis de seguranca cibernetica. Mantenha-se informado sobre as ultimas ameacas e atualizacoes de seguranca.']),

    (r'obrigado',
    ['De nada!', 'Estou aqui para ajudar.']),

    (r'(.*)',
    ['Desculpe, nao entendi. Voce poderia reformular sua pergunta?'])
]

# Funcao para fazer a solicitacao a API GPT-4
def gpt4_request(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150,
        "n": 1,
        "stop": None,
        "temperature": 0.7,
    }
    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()['choices'][0]['text'].strip()
    else:
        return "Desculpe, nao consegui processar sua solicitacao no momento."

# Criando o chatbot
def cyber_security_bot():
    print("Ola! Eu sou um chatbot de seguranca cibernetica. Como posso ajudar voce hoje?")
    chatbot = Chat(patterns, reflections)
    while True:
        try:
            user_input = raw_input("> ")  # Use raw_input() para Python 2
            if user_input.lower() in ['sair', 'exit', 'quit']:
                print("Ate logo!")
                break
            response = chatbot.respond(user_input)
            if response:
                print(response)
            else:
                # Se nao houver resposta padrao, use a API GPT-4
                gpt4_response = gpt4_request(user_input)
                print(gpt4_response)
        except KeyboardInterrupt:
            print("Ate logo!")
            break

if __name__ == "__main__":
    cyber_security_bot()
