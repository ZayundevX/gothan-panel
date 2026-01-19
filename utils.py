import json
import random
import re
import os

DB_FILE = "database.json"

NOMES = ["Lucas", "Pedro", "João", "Matheus", "Gabriel", "Rafael", "Bruno"]
SOBRENOMES = ["Silva", "Santos", "Oliveira", "Pereira", "Costa", "Rodrigues"]
CIDADES = ["São Paulo", "Rio de Janeiro", "Salvador", "Fortaleza", "Recife", "Curitiba"]

def load_db():
    if not os.path.exists(DB_FILE):
        save_db({"cpf": {}, "ip": {}})
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(db):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

def cpf_valido(cpf):
    return bool(re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf))

def ip_valido(ip):
    pattern = r"^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"
    return bool(re.match(pattern, ip))

def gerar_dados_cpf(cpf, db):
    if cpf in db["cpf"]:
        return db["cpf"][cpf]

    random.seed(cpf)
    nome = random.choice(NOMES)
    sobrenome = random.choice(SOBRENOMES)

    dados = {
        "nome": f"{nome} {sobrenome}",
        "cidade": random.choice(CIDADES),
        "idade": random.randint(18, 80),
        "filiacao": f"{random.choice(NOMES)} {sobrenome}"
    }

    db["cpf"][cpf] = dados
    save_db(db)
    return dados

def gerar_localizacao_ip(ip, db):
    if ip in db["ip"]:
        return db["ip"][ip]

    random.seed(ip)
    dados = {
        "lat": round(random.uniform(-33.75, 5.27), 6),
        "lon": round(random.uniform(-73.99, -34.79), 6)
    }

    db["ip"][ip] = dados
    save_db(db)
    return dados
