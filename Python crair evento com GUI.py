import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Evento:
    def __init__(self, nome, data, capacidade, estado, cidade, bairro, rua, numero, descricao=None):
        self.nome = nome
        self.data = data
        self.capacidade = capacidade
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.descricao = descricao

eventos = []

def criar_evento():
    nome = nome_entry.get()
    data = data_entry.get()
    capacidade = capacidade_entry.get()
    estado = estado_entry.get()
    cidade = cidade_entry.get()
    bairro = bairro_entry.get()
    rua = rua_entry.get()
    numero = numero_entry.get()
    descricao = descricao_entry.get()

    novo_evento = Evento(nome, data, capacidade, estado, cidade, bairro, rua, numero, descricao)
    eventos.append(novo_evento)

    messagebox.showinfo("Sucesso", "Evento criado com sucesso!")

root = tk.Tk()
root.title("Criador de Eventos")

tk.Label(root, text="Nome do evento:").grid(row=0)
nome_entry = tk.Entry(root)
nome_entry.grid(row=0, column=1)

tk.Label(root, text="Data do evento (DD/MM/AAAA):").grid(row=1)
data_entry = tk.Entry(root)
data_entry.grid(row=1, column=1)

tk.Label(root, text="Capacidade do evento:").grid(row=2)
capacidade_entry = tk.Entry(root)
capacidade_entry.grid(row=2, column=1)

tk.Label(root, text="Estado do evento:").grid(row=3)
estado_entry = tk.Entry(root)
estado_entry.grid(row=3, column=1)

tk.Label(root, text="Cidade do evento:").grid(row=4)
cidade_entry = tk.Entry(root)
cidade_entry.grid(row=4, column=1)

tk.Label(root, text="Bairro do evento:").grid(row=5)
bairro_entry = tk.Entry(root)
bairro_entry.grid(row=5, column=1)

tk.Label(root, text="Rua do evento:").grid(row=6)
rua_entry = tk.Entry(root)
rua_entry.grid(row=6, column=1)

tk.Label(root, text="Número ou nome da residência ou prédio do evento:").grid(row=7)
numero_entry = tk.Entry(root)
numero_entry.grid(row=7, column=1)

tk.Label(root, text="Descrição do evento (opcional):").grid(row=8)
descricao_entry = tk.Entry(root)
descricao_entry.grid(row=8, column=1)

tk.Button(root, text="Criar Evento", command=criar_evento).grid(row=9, column=1)

root.mainloop()