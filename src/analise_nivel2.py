import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
    .reset_index()
    .rename(columns={'total': 'faturamento'})
)

df_faturamento_cidade = (
    df_vendas_completas.groupby('cidade')['total']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
    .rename(columns={'total': 'faturamento'})
)

df_quantidade_produto_cidade = (
    df_vendas_completas.groupby(['cidade', 'nome_produto'])['quantidade']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

df_top_produto_cidade = (
    df_quantidade_produto_cidade
    .sort_values(['cidade', 'quantidade'], ascending=[True, False])
    .groupby('cidade')
    .head(1)
    .reset_index(drop=True)
)

df_ticket_cidade = (
    df_vendas_completas.groupby('cidade')
    .agg(
        faturamento_total=('total', 'sum'),
        qtd_vendas=('total', 'count')
    )
    .reset_index()
)

df_ticket_cidade['ticket_medio'] = (
    df_ticket_cidade['faturamento_total'] / df_ticket_cidade['qtd_vendas']
)

df_ticket_cidade = df_ticket_cidade.sort_values('ticket_medio', ascending=False)

# Análise temporal
df_faturamento_mes = (
    df_vendas_completas.groupby('mes')['total']
    .sum()
    .sort_index()
    .reset_index()
    .rename(columns={'total': 'faturamento'})
)

df_vendas_mes = (
    df_vendas_completas.groupby('mes')['total']
    .count()
    .sort_index()
    .reset_index()
    .rename(columns={'total': 'qtd_vendas'})
)

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

# Gráficos
sns.set_theme(style='whitegrid')

# -------------------------------
# Faturamento por Categoria
# -------------------------------
plt.figure(figsize=(10, 6))

sns.barplot(
    data=df_faturamento_categoria,
    x='categoria',
    y='faturamento'
)

plt.title('Faturamento por Categoria')
plt.xlabel('Categoria')
plt.ylabel('Faturamento')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# -------------------------------
# Faturamento por Mês
# -------------------------------
plt.figure(figsize=(10, 6))

sns.lineplot(
    data=df_faturamento_mes,
    x='mes',
    y='faturamento',
    marker='o'
)

plt.title('Faturamento por Mês')
plt.xlabel('Mês')
plt.ylabel('Faturamento')

plt.tight_layout()
plt.show()

# -------------------------------
# Vendas por Mês
# -------------------------------
plt.figure(figsize=(10, 6))

sns.lineplot(
    data=df_vendas_mes,
    x='mes',
    y='qtd_vendas',
    marker='o'
)

plt.title('Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Quantidade de Vendas')

plt.tight_layout()
plt.show()

# -------------------------------
# Faturamento x Vendas 
# -------------------------------

plt.figure(figsize=(10, 6))
ax = sns.lineplot(
    data=df_faturamento_mes,
    x='mes',
    y='faturamento',
    marker='o',
    label='Faturamento'
)
ax2 = ax.twinx()

sns.lineplot(
    data=df_vendas_mes,
    x='mes',
    y='qtd_vendas',
    marker='o',
    color='orange',
    label='Vendas',
    ax=ax2
)

ax.set_title('Faturamento vs Vendas por Mês')
ax.set_xlabel('Mês')
ax.set_ylabel('Faturamento')
ax2.set_ylabel('Quantidade de Vendas')

 # Organização das legendas 
lines_1, labels_1 = ax.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()

ax.legend(
    lines_1 + lines_2,
    labels_1 + labels_2,
    loc='upper left'
)

plt.tight_layout()
plt.show()

# Salvando resultados 
df_faturamento_categoria.to_csv('data/processed/faturamento_categoria.csv', index=False)
df_faturamento_cidade.to_csv('data/processed/faturamento_cidade.csv', index=False)
df_quantidade_produto_cidade.to_csv('data/processed/quantidade_produto_cidade.csv', index=False)
df_top_produto_cidade.to_csv('data/processed/top_produto_cidade.csv', index=False)
df_ticket_cidade.to_csv('data/processed/ticket_cidade.csv', index=False)
df_faturamento_mes.to_csv('data/processed/faturamento_mes.csv', index=False)
df_vendas_mes.to_csv('data/processed/vendas_mes.csv', index=False)
df_faturamento_vendas.to_csv('data/processed/analise_mensal.csv', index=False)