import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep} {nome}, Clica o link => https://www.linkedin.com/in/deivid-bertapele-5b9368101/{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep} {nome}, Clica o link  => https://myportfolio-flask.herokuapp.com/{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep} {nome}, Clica o link  => https://github.com/DeividBertapele{os.linesep}')
    else:
        print(f'Digite apenas 1,2 ou 3')
    
    
def start():
    # Apresentar o chatbot
    print('Seja Bem vindo ao Canal do DBCODE')
    
    # Perguntar seu nome
    nome = input('Digite o seu nome? '{os.linesep})
    
    # Perguntar seu email
    email = input('Digite o seu email?'{os.linesep})
    
    while True:
        # Mostrar o menu de opções
        resposta = input(
            f'O que você gostaria de saber do meu perfil?{os.linesep}[1] - Linkedin{os.linesep}[2] - Meu portfolio{os.linesep}[3] - Github{os.linesep}')
        
        # Processar a resoista enviada
        processar_resposta(resposta, nome)



if __name__ == "__main__":
    start()