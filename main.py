from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crie uma instância do ChatBot
chatbot = ChatBot('JobBot')

# Crie um treinador para o chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Treine o chatbot usando o corpus padrão
trainer.train('chatterbot.corpus.portuguese')

# Adicione treinamento específico para geração de empregos
trainer.train([
    "Olá, como posso te ajudar?",
    "Estou procurando um emprego.",
    "Quais são suas qualificações?",
    "Eu sou engenheiro de software com 5 anos de experiência.",
    "Ótimo! Temos vagas disponíveis em várias empresas de tecnologia. Posso te enviar mais detalhes por e-mail?"
])
