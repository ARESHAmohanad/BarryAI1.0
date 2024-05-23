import nltk
import random
from nltk.chat.util import Chat, reflections

# Definindo pares de padrões e respostas
patterns = [
    (r'como posso me proteger contra (.*)',
    ['Você pode se proteger contra {0} usando um bom software antivírus e mantendo seu sistema sempre atualizado.',
    'Certifique-se de ter um firewall ativo e evite clicar em links suspeitos ou baixar arquivos de fontes não confiáveis.']),

    (r'eu fui hackeado',
    ['Sinto muito ouvir isso. Entre em contato com as autoridades de segurança cibernética imediatamente e altere suas senhas o mais rápido possível.']),

    (r'(.*) (ataque|vulnerabilidade) (.*)',
    ['Você pode aprender mais sobre {1} em sites confiáveis de segurança cibernética. Mantenha-se informado sobre as últimas ameaças e atualizações de segurança.']),

    (r'obrigado',
    ['De nada!', 'Estou aqui para ajudar.']),

    (r'(.*)',
    ['Desculpe, não entendi. Você poderia reformular sua pergunta?'])
]

# Criando o chatbot
def cyber_security_bot():
    print("Olá! Eu sou um chatbot de segurança cibernética. Como posso ajudar você hoje?")
    chatbot = Chat(patterns, reflections)
    while True:
        try:
            user_input = input("> ")
            response = chatbot.respond(user_input)
            print(response)
        except KeyboardInterrupt:
            print("Até logo!")
            break

if __name__ == "__main__":
    cyber_security_bot()
