import pandas as pd

# Leitura dos dados
df_clientes = pd.read_csv('data/raw/clientes.csv')
df_produtos = pd.read_csv('data/raw/produtos.csv')
df_vendas = pd.read_csv('data/raw/vendas.csv')

# Junção das tabelas
df_vendas_clientes = df_vendas.merge(df_clientes, on='id_cliente')
df_vendas_completas = df_vendas_clientes.merge(df_produtos, on='id_produto')

# Criação de métricas
df_vendas_completas['total'] = df_vendas_completas['preco'] * df_vendas_completas['quantidade']

# Limpeza e preparação dos dados
df_vendas_completas['data'] = pd.to_datetime(df_vendas_completas['data'])
df_vendas_completas['mes'] = df_vendas_completas['data'].dt.month

# Análises
df_faturamento_categoria = (
    df_vendas_completas.groupby('categoria')['total']
    .sum()
    .sort_values(ascending=False)
)

df_faturamento_cidade = (
    df_vendas_completas.groupby('cidade')['total']
    .sum()
    .sort_values(ascending=False)
)

df_quantidade_produto_cidade = (
    df_vendas_completas.groupby(['cidade', 'nome_produto'])['quantidade']
    .sum()
    .sort_values(ascending=False)
)

df_top_produto_cidade = (
    df_quantidade_produto_cidade.reset_index()
    .sort_values(['cidade', 'quantidade'], ascending=[True, False])
    .groupby('cidade')
    .head(1)
)

df_ticket_cidade = (
    df_vendas_completas.groupby('cidade')
    .agg(
        faturamento_total=('total', 'sum'),
        qtd_vendas=('total', 'count')
    )
)

df_ticket_cidade['ticket_medio'] = (
    df_ticket_cidade['faturamento_total'] / df_ticket_cidade['qtd_vendas']
)

df_ticket_cidade = df_ticket_cidade.sort_values('ticket_medio', ascending=False)

# Análise temporal
df_faturamento_mes = df_vendas_completas.groupby('mes')['total'].sum().sort_index()
df_vendas_mes = df_vendas_completas.groupby('mes')['total'].count().sort_index()

# Preparar dataframes mensais (CORREÇÃO AQUI)
df_faturamento_mes = df_faturamento_mes.reset_index()
df_vendas_mes = df_vendas_mes.reset_index()

# Ajuste de nomes
df_faturamento_mes = df_faturamento_mes.rename(columns={'total': 'faturamento'})
df_vendas_mes = df_vendas_mes.rename(columns={'total': 'qtd_vendas'})

# Merge das análises mensais
df_faturamento_vendas = df_faturamento_mes.merge(df_vendas_mes, on='mes')

df_faturamento_vendas['ticket_medio'] = (
    df_faturamento_vendas['faturamento'] / df_faturamento_vendas['qtd_vendas']
)

df_faturamento_vendas['ticket_medio'] = df_faturamento_vendas['ticket_medio'].round(2)
df_faturamento_vendas = df_faturamento_vendas.sort_values('faturamento', ascending=False)

# Exibição dos resultados
print('Faturamento por categoria:')
print(df_faturamento_categoria.head())

print('\nFaturamento por cidade:')
print(df_faturamento_cidade.head())

print('\nTop produto por cidade:')
print(df_top_produto_cidade)

print('\nFaturamento por mês:')
print(df_faturamento_mes)

print('\nVendas por mês:')
print(df_vendas_mes)

print('\nFaturamento vs Vendas por mês:')
print(df_faturamento_vendas)

print('\nTicket médio por cidade:')
print(df_ticket_cidade)

# Preparação para exportação
df_faturamento_categoria = df_faturamento_categoria.reset_index()
df_faturamento_cidade = df_faturamento_cidade.reset_index()
df_quantidade_produto_cidade = df_quantidade_produto_cidade.reset_index()
df_top_produto_cidade = df_top_produto_cidade.reset_index(drop=True)
df_ticket_cidade = df_ticket_cidade.reset_index()

# Salvando resultados
df_faturamento_categoria.to_csv('data/processed/faturamento_categoria.csv', index=False)
df_faturamento_cidade.to_csv('data/processed/faturamento_cidade.csv', index=False)
df_quantidade_produto_cidade.to_csv('data/processed/quantidade_produto_cidade.csv', index=False)
df_top_produto_cidade.to_csv('data/processed/top_produto_cidade.csv', index=False)
df_ticket_cidade.to_csv('data/processed/ticket_cidade.csv', index=False)
df_faturamento_mes.to_csv('data/processed/faturamento_mes.csv', index=False)
df_vendas_mes.to_csv('data/processed/vendas_mes.csv', index=False)
df_faturamento_vendas.to_csv('data/processed/analise_mensal.csv', index=False)