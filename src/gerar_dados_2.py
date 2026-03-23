##################
# GERAR CLIENTES #
##################

import pandas as pd
import random

cidades = ['Belém', 'Manaus', 'Ananindeua', 'Marabá', 'Santarém']

clientes = []

for i in range(1, 301):
    
    cliente = {
        'id_cliente': i,
        'nome_cliente': f'Cliente_{i}',
        'cidade': random.choice(cidades),
        'idade': random.randint(18, 60)
    }
    
    clientes.append(cliente)

df_clientes = pd.DataFrame(clientes)

df_clientes.to_csv('data/raw/clientes.csv', index=False)

print(df_clientes.head())

##################
# GERAR PRODUTOS #
##################

import pandas as pd

produtos = [
    {'id_produto': 1, 'nome_produto': 'Óleo de motor', 'categoria': 'Lubrificação', 'preco': 120},
    {'id_produto': 2, 'nome_produto': 'Lubrificante', 'categoria': 'Lubrificação', 'preco': 80},
    {'id_produto': 3, 'nome_produto': 'Pneu', 'categoria': 'Pneus', 'preco': 500},
    {'id_produto': 4, 'nome_produto': 'Aditivo', 'categoria': 'Fluidos', 'preco': 50},
    {'id_produto': 5, 'nome_produto': 'Filtro de óleo', 'categoria': 'Manutenção', 'preco': 40},
    {'id_produto': 6, 'nome_produto': 'Bateria', 'categoria': 'Elétrica', 'preco': 350},
    {'id_produto': 7, 'nome_produto': 'Fluido de freio', 'categoria': 'Fluidos', 'preco': 60},
    {'id_produto': 8, 'nome_produto': 'Palheta', 'categoria': 'Manutenção', 'preco': 30}
]

df_produtos = pd.DataFrame(produtos)

df_produtos.to_csv('data/raw/produtos.csv', index=False)

print(df_produtos.head())

# =========================
# GERAR VENDAS
# =========================

vendas = []

for i in range(1, 1001):
    venda = {
        'id_venda': i,
        'id_cliente': random.randint(1, 300),
        'id_produto': random.randint(1, 8),
        'data': f"2026-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}",
        'quantidade': random.randint(1, 5)
    }
    
    vendas.append(venda)

df_vendas = pd.DataFrame(vendas)

df_vendas.to_csv('data/raw/vendas.csv', index=False)

print(df_vendas.head())