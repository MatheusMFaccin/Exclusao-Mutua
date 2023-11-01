import threading
import random
import time

saldo = 0
num_threads = 3
recurso_compartilhado = -1
recurso_chave = [False] * num_threads

def algoritmo_de_lamport_quer_entrar(thread_id):
    recurso_chave[thread_id] = True
    max_priority = max(recurso_chave)
   

    for i in range(num_threads):
        while i != thread_id and recurso_chave[i] and (recurso_chave[i] < recurso_chave[thread_id] or (recurso_chave[i] == recurso_chave[thread_id] and i < thread_id)):
            pass

def algoritmo_de_lamport_sai(thread_id):
    recurso_chave[thread_id] = False

def depositar():
    global saldo
    while True:
        algoritmo_de_lamport_quer_entrar(0)
        valor = random.randint(1, 10)
        saldo += valor
        print(f"Depósito: +{valor}, Saldo: {saldo}")
        algoritmo_de_lamport_sai(0)
        time.sleep(0.5)

def retirar():
    global saldo
    while True:
        algoritmo_de_lamport_quer_entrar(1)
        valor = random.randint(1, 30)
        while valor > saldo:
            print("Saldo insuficiente. Aguardando depósito...")
            time.sleep(1)
        saldo -= valor
        print(f"Retirada: -{valor}, Saldo: {saldo}")
        algoritmo_de_lamport_sai(1)
        time.sleep(0.5)

def mostrarSaldo():
    while True:
        algoritmo_de_lamport_quer_entrar(2)
        print(f"Saldo atual: {saldo}")
        algoritmo_de_lamport_sai(2)
        time.sleep(1)

threads = []
threads.append(threading.Thread(target=depositar))
threads.append(threading.Thread(target=retirar))
threads.append(threading.Thread(target=mostrarSaldo))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
