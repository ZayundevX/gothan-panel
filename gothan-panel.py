import time
from banner import show_banner
from utils import *

def menu():
    print("[ 1 ] - Puxar Dados por CPF")
    print("[ 2 ] - Localização Por IP")
    print("[ 3 ] - Sair\n")
    return input("Escolher - ")

def opcao_cpf():
    cpf = input("Insira o CPF: ")
    if not cpf_valido(cpf):
        print("CPF inválido.")
        time.sleep(2)
        return

    db = load_db()
    dados = gerar_dados_cpf(cpf, db)

    print(f"\nNOME COMPLETO: {dados['nome']}")
    print(f"CIDADE: {dados['cidade']}")
    print(f"IDADE: {dados['idade']}")
    print(f"FILIAÇÃO: {dados['filiacao']}\n")
    input("Pressione ENTER para voltar...")

def opcao_ip():
    ip = input("Insira o IP: ")
    if not ip_valido(ip):
        print("IP inválido.")
        time.sleep(2)
        return

    print("Procurando Localização Via IP...")
    time.sleep(4)

    db = load_db()
    loc = gerar_localizacao_ip(ip, db)

    print(f"\nCOORDENADAS: {loc['lat']}, {loc['lon']}\n")
    input("Pressione ENTER para voltar...")

def main():
    while True:
        show_banner()
        escolha = menu()

        if escolha == "1":
            opcao_cpf()
        elif escolha == "2":
            opcao_ip()
        elif escolha == "3":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.")
            time.sleep(2)

if __name__ == "__main__":
    main()
