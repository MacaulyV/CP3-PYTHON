# Importando as bibliotecas necessárias
import re
from datetime import datetime
from rich import print

# Definindo a classe Evento
class Evento:
    def __init__(self, nome, data, capacidade, estado, cidade, bairro, rua, numero, descricao=None):
        # Inicializando as propriedades da classe
        self.nome = nome
        self.data = data
        self.capacidade = capacidade
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.descricao = descricao

    # Método para retornar uma representação de string do objeto Evento
    def __str__(self):
        return (
            f'Nome do evento: {self.nome}\n'
            f'Data do evento: {self.data}\n'
            f'Capacidade do evento: {self.capacidade}\n'
            f'Estado do evento: {self.estado}\n'
            f'Cidade do evento: {self.cidade}\n'
            f'Bairro do evento: {self.bairro}\n'
            f'Rua do evento: {self.rua}\n'
            f'Número ou nome da residência ou prédio do evento: {self.numero}\n'
            f'Descrição do evento: {self.descricao}\n' if self.descricao else ''
        )

# Criando uma lista para armazenar todos os eventos
eventos = []

# Definindo a função para criar um novo evento
def criar_evento():
    """
    Cria um novo evento e o armazena no sistema.
    """ 
    print("[bold yellow]Bem-vindo ao assistente de criação de eventos![/bold yellow]")
    print("Vamos começar criando um novo evento.")
    print("----------------------------------------")
    
    # Solicita ao usuário que insira o nome do evento e valida a entrada
    while True:
        nome = input("Nome do evento: ")
        if nome.isalpha() and len(nome) <= 50:
            break
        else:
            print("[bold red]Por favor, insira um nome válido contendo apenas letras e com no máximo 50 caracteres.[/bold red]")
    
    # Solicita ao usuário que insira a data do evento e valida a entrada
    while True:
        data = input("Data do evento (DD/MM/AAAA): ")
        try:
            data_evento = datetime.strptime(data, '%d/%m/%Y')
            data_atual = datetime.now()
            data_limite = datetime.strptime('31/12/2024', '%d/%m/%Y')
            if data_evento.date() < data_atual.date():
                print("[bold red]A data do evento não pode ser anterior à data atual.[/bold red]")
            elif data_evento.date() > data_limite.date():
                print("[bold red]A data do evento não pode ser posterior a 31/12/2024.[/bold red]")
            else:
                break
        except ValueError:
            print("[bold red]Por favor, insira uma data válida no formato DD/MM/AAAA.[/bold red]")
    
    # Solicita ao usuário que insira a capacidade do evento e valida a entrada
    while True:
        print("Por favor, escolha uma das seguintes opções de capacidade até: 50, 100, 200, 500, 1000 pessoas")
        try:
            capacidade = float(input("Capacidade do evento:"))
            if capacidade in [50, 100, 200, 500, 1000]:
                break
            else:
                print("[bold red]Por favor, insira uma das capacidades sugeridas.[/bold red]")
        except ValueError:
            print("[bold red]Por favor, insira um número válido para a capacidade.[/bold red]")
    
    # Solicita ao usuário que insira a localização do evento e valida a entrada
    while True:
        print("Agora você vai inserir os dados do endereço do evento.")
        continuar = input("Você deseja continuar? (s/n): ")
        if continuar.lower() == 'n':
            print("[bold red]Não é possível criar um evento sem inserir uma localização.[/bold red]")
            return
        elif continuar.lower() == 's':
            # input do estado
            while True:
                estado = input("Estado do evento: ")
                if all(x.isalpha() or x.isspace() for x in estado) and len(estado) <= 20:
                    break
                else:
                    print("[bold red]Por favor, insira um estado válido contendo apenas letras e espaços, e com no máximo 20 caracteres.[/bold red]")
            # input da cidade       
            while True:
                cidade = input("Cidade do evento: ")
                if all(x.isalpha() or x.isspace() for x in cidade) and len(cidade) <= 30:
                    break
                else:
                    print("[bold red]Por favor, insira uma cidade válida contendo apenas letras e espaços, e com no máximo 30 caracteres.[/bold red]")
            # input do bairro
            while True:
                bairro = input("Bairro do evento: ")
                if all(x.isalpha() or x.isspace() for x in bairro) and len(bairro) <= 50:
                    break
                else:
                    print("[bold red]Por favor, insira um bairro válido contendo apenas letras e espaços, e com no máximo 50 caracteres.[/bold red]")
            # input da rua
            while True:
                rua = input("Rua do evento: ")
                if all(x.isalpha() or x.isspace() for x in rua) and len(rua) <= 50:
                    break
                else:
                    print("[bold red]Por favor, insira uma rua válida contendo apenas letras e espaços, e com no máximo 50 caracteres.[/bold red]")
              # input da residencia ou local
            while True:
                numero = input("Número ou nome da residência ou prédio do evento: ")
                if len(numero) <= 20:
                    break
                else:
                    print("[bold red]Por favor, insira um número ou nome válido para a residência ou prédio do evento, com no máximo 20 caracteres.[/bold red]")
            break
        else:
            print("[bold red]Por favor, insira 's' para continuar ou 'n' para parar.[/bold red]")
    
    # Solicita ao usuário que insira uma descrição do evento e valida a entrada
    descricao = None
    while True:
        print("Agora você pode adicionar uma descrição ao seu evento (opcional).")
        continuar = input("Você deseja adicionar uma descrição? (s/n): ")
        if continuar.lower() == 'n':
            break
        elif continuar.lower() == 's':
            while True:
                descricao = input("Descrição do evento (máximo de 200 caracteres): ")
                if len(descricao) <= 200:
                    break
                else:
                    print("[bold red]Por favor, insira uma descrição com no máximo 200 caracteres.[/bold red]")
            break
        else:
            print("[bold red]Por favor, insira 's' para continuar ou 'n' para parar.[/bold red]")
    
    # Confirma a criação do evento com o usuário
    while True:
        print("Você está prestes a criar um evento com os seguintes detalhes:")
        print(f'Nome: {nome}\nData: {data}\nCapacidade: {capacidade}\nLocalização: {estado}, {cidade}, {bairro}, {rua}, {numero}\nDescrição: {descricao if descricao else "Nenhuma"}')
        continuar = input("Você deseja prosseguir com a criação do evento? (s/n): ")
        if continuar.lower() == 'n':
            print("[bold red]A criação do evento foi cancelada.[/bold red]")
            return
        elif continuar.lower() == 's':
            break
        else:
            print("[bold red]Por favor, insira 's' para continuar ou 'n' para parar.[/bold red]")
    
    # Cria um novo objeto Evento e adiciona à lista de eventos
    novo_evento = Evento(nome, data, capacidade, estado, cidade, bairro, rua, numero, descricao)
    eventos.append(novo_evento)
    print("[bold green]Evento criado com sucesso![/bold green]")

# Chama a função criar_evento
criar_evento()
