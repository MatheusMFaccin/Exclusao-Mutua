import threading
import random
import time

saldo = 0
num_threads = 3

# Variáveis para o algoritmo de Maekawa
fila_de_espera = [0] * num_threads
num_processos = 3
permissoes = [0] * num_threads

# Função para verificar se um processo pode acessar o recurso
def pode_acessar(thread_id):
    for i in range(num_threads):
        if i != thread_id and fila_de_espera[i] == 1:
            return False
    return True

# Função para solicitar permissões
def solicitar_permissoes(thread_id):
    fila_de_espera[thread_id] = 1
    for i in range(num_threads):
        if i != thread_id:
            while fila_de_espera[i] == 1:
                pass
    permissoes[thread_id] = 1

# Função para liberar permissões
def liberar_permissoes(thread_id):
    permissoes[thread_id] = 0
    fila_de_espera[thread_id] = 0

def depositar():
    global saldo
    while True:
        thread_id = 0
        solicitar_permissoes(thread_id)
        valor = random.randint(1, 10)
        saldo += valor
        print(f"Depósito: +{valor}, Saldo: {saldo}")
        liberar_permissoes(thread_id)
        time.sleep(0.5)
        

def retirar():
    global saldo
    while True:
        thread_id = 1
        solicitar_permissoes(thread_id)
        valor = random.randint(1, 30)
        while valor > saldo:
            print("Saldo insuficiente. Aguardando depósito...")
            liberar_permissoes(thread_id)
            time.sleep(1)
            
        saldo -= valor
        print(f"Retirada: -{valor}, Saldo: {saldo}")
        liberar_permissoes(thread_id)
        time.sleep(0.5)

def mostrarSaldo():
    while True:
        thread_id = 2
        solicitar_permissoes(thread_id)
        print(f"Saldo atual: {saldo}")
        liberar_permissoes(thread_id)
        time.sleep(1)

threads = []
threads.append(threading.Thread(target=depositar))
threads.append(threading.Thread(target=retirar))
threads.append(threading.Thread(target=mostrarSaldo))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
