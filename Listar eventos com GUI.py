import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime, timedelta
import random
import json
import os

class Evento:
    def __init__(self, nome, data, capacidade, vagas_disponiveis, estado, cidade, bairro, rua, numero, descricao=None):
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
        self.preco = random.randint(50, 200)
        self.reservas = []

eventos = [
    Evento("Google I/O", (datetime.now() + timedelta(days=10)).strftime('%d/%m/%Y'), 100, random.randint(1, 100), "São Paulo", "São Paulo", "Vila Mariana", "Rua Vergueiro", "Edifício A, Andar " + str(random.randint(1, 10)), "Evento de tecnologia organizado pelo Google."),
    Evento("Apple WWDC", (datetime.now() + timedelta(days=20)).strftime('%d/%m/%Y'), 200, random.randint(1, 200), "Rio de Janeiro", "Rio de Janeiro", "Copacabana", "Avenida Atlântica", "Edifício B, Andar " + str(random.randint(1, 10)), "Conferência Mundial de Desenvolvedores da Apple."),
    Evento("Microsoft Build", (datetime.now() + timedelta(days=30)).strftime('%d/%m/%Y'), 300, random.randint(1, 300), "Minas Gerais", "Belo Horizonte", "Savassi", "Avenida do Contorno", "Edifício C, Andar " + str(random.randint(1, 10)), "Evento de desenvolvedores da Microsoft."),
    Evento("Facebook F8", (datetime.now() + timedelta(days=40)).strftime('%d/%m/%Y'), 400, random.randint(1, 400), "Rio Grande do Sul", "Porto Alegre", "Moinhos de Vento", "Rua Padre Chagas", "Edifício D, Andar " + str(random.randint(1, 10)), "Conferência de desenvolvedores do Facebook."),
    Evento("Amazon re:Invent", (datetime.now() + timedelta(days=50)).strftime('%d/%m/%Y'), 500, random.randint(1, 500), "Bahia", "Salvador", "Barra", "Avenida Oceânica", "Edifício E, Andar " + str(random.randint(1, 10)), "Evento global de computação em nuvem hospedado pela Amazon Web Services.")
]

def reservar_vaga(evento):
    if evento.vagas_disponiveis > 0:
        evento.vagas_disponiveis -= 1
        messagebox.showinfo("Reserva", "Vaga reservada com sucesso!")
    else:
        messagebox.showinfo("Reserva", "Desculpe, não há vagas disponíveis para este evento.")

def cancelar_reserva(evento):
    if evento.vagas_disponiveis < evento.capacidade:
        evento.vagas_disponiveis += 1
        messagebox.showinfo("Cancelar Reserva", "Reserva cancelada com sucesso!")
    else:
        messagebox.showinfo("Cancelar Reserva", "Desculpe, não há reservas para cancelar para este evento.")

def visualizar_detalhes_evento():
    # Exibe a lista de eventos disponíveis
    eventos_str = "\n".join([f"{i+1}. {evento.nome}" for i, evento in enumerate(eventos)])
    messagebox.showinfo("Eventos disponíveis", eventos_str)

    escolha = simpledialog.askinteger("Escolha um evento", "Escolha um evento para visualizar seus detalhes (insira o número correspondente):", minvalue=1, maxvalue=len(eventos))
    if escolha is not None:
        evento = eventos[escolha - 1]
        messagebox.showinfo("Detalhes do evento", f"\nDetalhes do evento:\nNome: {evento.nome}\nData: {evento.data}\nCapacidade: {evento.capacidade}\nVagas disponíveis: {evento.vagas_disponiveis}\nLocalização: {evento.estado}, {evento.cidade}, {evento.bairro}, {evento.rua}, {evento.numero}\nDescrição: {evento.descricao if evento.descricao else 'Nenhuma'}")

        if messagebox.askyesno("Reserva", "Você gostaria de reservar uma vaga para este evento?"):
            reservar_vaga(evento)
        elif messagebox.askyesno("Cancelar Reserva", "Você gostaria de cancelar uma reserva para este evento?"):
            cancelar_reserva(evento)

root = tk.Tk()
root.title("Visualizador de Eventos")

tk.Button(root, text="Visualizar Detalhes do Evento", command=visualizar_detalhes_evento).pack()

root.mainloop()