# Importando as bibliotecas necessárias
from datetime import datetime, timedelta
import random
import json
import os

# Definindo a classe Evento
class Evento:
    def __init__(self, nome, data, capacidade, vagas_disponiveis, estado, cidade, bairro, rua, numero, descricao=None):
        # Inicializando as propriedades da classe
        self.nome = nome
        self.data = data
        self.capacidade = capacidade
        self.vagas_disponiveis = vagas_disponiveis
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.descricao = descricao
        self.preco = random.randint(50, 200)  # Adiciona um preço aleatório para cada evento
        self.reservas = []  # Adiciona uma lista para armazenar as reservas

    # Método para retornar uma representação de string do objeto Evento
    def __str__(self):
        return (
            f'Nome do evento: {self.nome}\n'
            f'Data do evento: {self.data}\n'
            f'Capacidade do evento: {self.capacidade}\n'
            f'Vagas disponíveis: {self.vagas_disponiveis}\n'
            f'Localização: {self.estado}, {self.cidade}, {self.bairro}, {self.rua}, {self.numero}\n'
            f'Descrição: {self.descricao}\n' if self.descricao else ''
        )

def carregar_dados():
    """
    Carrega todos os dados do sistema (eventos, reservas, etc.) de um arquivo.
    """
    try:
        # Verifica se o arquivo de dados existe
        if os.path.exists('dados.json'):
            # Abre o arquivo de dados
            with open('dados.json', 'r') as arquivo:
                # Carrega os dados do arquivo
                dados = json.load(arquivo)

            # Converte os dados de volta para objetos Evento
            eventos = [Evento(**evento) for evento in dados]
        else:
            # Se o arquivo de dados não existir, retorna a lista original de eventos
            eventos = [
                Evento("Google I/O", (datetime.now() + timedelta(days=10)).strftime('%d/%m/%Y'), 100, random.randint(1, 100), "São Paulo", "São Paulo", "Vila Mariana", "Rua Vergueiro", "Edifício A, Andar " + str(random.randint(1, 10)), "Evento de tecnologia organizado pelo Google."),
                Evento("Apple WWDC", (datetime.now() + timedelta(days=20)).strftime('%d/%m/%Y'), 200, random.randint(1, 200), "Rio de Janeiro", "Rio de Janeiro", "Copacabana", "Avenida Atlântica", "Edifício B, Andar " + str(random.randint(1, 10)), "Conferência Mundial de Desenvolvedores da Apple."),
                Evento("Microsoft Build", (datetime.now() + timedelta(days=30)).strftime('%d/%m/%Y'), 300, random.randint(1, 300), "Minas Gerais", "Belo Horizonte", "Savassi", "Avenida do Contorno", "Edifício C, Andar " + str(random.randint(1, 10)), "Evento de desenvolvedores da Microsoft."),
                Evento("Facebook F8", (datetime.now() + timedelta(days=40)).strftime('%d/%m/%Y'), 400, random.randint(1, 400), "Rio Grande do Sul", "Porto Alegre", "Moinhos de Vento", "Rua Padre Chagas", "Edifício D, Andar " + str(random.randint(1, 10)), "Conferência de desenvolvedores do Facebook."),
                Evento("Amazon re:Invent", (datetime.now() + timedelta(days=50)).strftime('%d/%m/%Y'), 500, random.randint(1, 500), "Bahia", "Salvador", "Barra", "Avenida Oceânica", "Edifício E, Andar " + str(random.randint(1, 10)), "Evento global de computação em nuvem hospedado pela Amazon Web Services.")
            ]

        print("Dados carregados com sucesso!")
        return eventos

    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")
        return None

def reservar_vaga(evento):
    """
    Permite ao usuário reservar uma vaga em um evento específico.
    """
    # Verifica se há vagas disponíveis
    if evento.vagas_disponiveis > 0:
        # Solicita ao usuário que insira seus dados
        nome = input("Por favor, insira seu nome completo: ")
        data_nascimento = input("Por favor, insira sua data de nascimento (dd/mm/aaaa): ")

        # Solicita ao usuário que escolha uma forma de pagamento
        while True:
            forma_pagamento = input("Por favor, escolha uma forma de pagamento (1 - Cartão de Crédito, 2 - Cartão de Débito, 3 - PIX): ")
            if forma_pagamento in ['1', '2', '3']:
                break
            else:
                print("Por favor, insira um número válido correspondente a uma das formas de pagamento listadas.")

        # Adiciona um valor lógico aleatório para o pagamento do ingresso
        pagamento_realizado = random.choice([True, False])
        if pagamento_realizado:
            print("Pagamento realizado com sucesso!")
            # Atualiza a quantidade de vagas disponíveis
            evento.vagas_disponiveis -= 1
            # Adiciona a reserva à lista de reservas do evento
            evento.reservas.append(nome)
            print("Reserva confirmada! Obrigado por comprar seu ingresso para o evento.")
        else:
            print("O pagamento falhou. Por favor, tente novamente.")
    else:
        print("Desculpe, não há vagas disponíveis para este evento.")

def cancelar_reserva(evento):
    """
    Permite ao usuário cancelar uma reserva previamente feita.
    """
    # Solicita ao usuário que insira seu nome
    nome = input("Por favor, insira seu nome completo: ")

    # Verifica se o usuário tem uma reserva para o evento
    if nome in evento.reservas:
        # Remove a reserva da lista de reservas do evento
        evento.reservas.remove(nome)
        # Atualiza a quantidade de vagas disponíveis
        evento.vagas_disponiveis += 1
        print("Reserva cancelada com sucesso!")
    else:
        print("Você não tem uma reserva para este evento.")

def salvar_dados():
    """
    Salva todos os dados do sistema (eventos, reservas, etc.) em um arquivo.
    """
    # Coleta todos os dados do sistema que precisam ser salvos
    dados = [evento.__dict__ for evento in eventos]

    # Converte os dados em uma string JSON
    dados_json = json.dumps(dados)

    # Abre o arquivo onde os dados serão salvos
    with open('dados.json', 'w') as arquivo:
        # Escreve os dados no arquivo
        arquivo.write(dados_json)

    print("Dados salvos com sucesso!")

def visualizar_detalhes_evento():
    """
    Exibe todos os detalhes de um evento específico.
    """
    while True:  # Adiciona um loop para permitir que o usuário visualize vários eventos
        # Exibe a lista de eventos disponíveis
        print("Eventos disponíveis:")
        for i, evento in enumerate(eventos, 1):
            print(f"{i}. {evento.nome}")

        # Solicita ao usuário que escolha um evento para visualizar seus detalhes
        while True:
            escolha = input("Escolha um evento para visualizar seus detalhes (insira o número correspondente): ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(eventos):
                evento = eventos[int(escolha) - 1]
                break
            else:
                print("Por favor, insira um número válido correspondente a um dos eventos listados.")

        # Exibe os detalhes do evento escolhido
        print(f"\nDetalhes do evento:\nNome: {evento.nome}\nData: {evento.data}\nCapacidade: {evento.capacidade}\nVagas disponíveis: {evento.vagas_disponiveis}\nLocalização: {evento.estado}, {evento.cidade}, {evento.bairro}, {evento.rua}, {evento.numero}\nDescrição: {evento.descricao if evento.descricao else 'Nenhuma'}")

             # Pergunta ao usuário se ele deseja reservar uma vaga ou cancelar uma reserva para o evento
        while True:
            acao = input("Você deseja reservar uma vaga ou cancelar uma reserva para este evento? (r - Reservar, c - Cancelar, n - Nenhuma): ")
            if acao.lower() == 'r':
                reservar_vaga(evento)
                break
            elif acao.lower() == 'c':
                cancelar_reserva(evento)
                break
            elif acao.lower() == 'n':
                break
            else:
                print("Por favor, insira 'r' para reservar uma vaga, 'c' para cancelar uma reserva ou 'n' para voltar à lista de eventos.")

        # Pergunta ao usuário se ele deseja visualizar outro evento
        continuar = input("Você deseja visualizar outro evento? (s/n): ")
        if continuar.lower() == 'n':
            break

    # Chama a função salvar dados para salvar os dados do sistema
    salvar_dados()

# Carrega os dados do sistema
eventos = carregar_dados()

# Chama a função visualizar_detalhes_evento
visualizar_detalhes_evento()