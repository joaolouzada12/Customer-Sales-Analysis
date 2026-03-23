import pandas as pd 

df_clientes = pd.read_csv('data/raw/clientes.csv')
df_produtos = pd.read_csv('data/raw/produtos.csv')
df_vendas = pd.read_csv('data/raw/vendas.csv')

df_vendas_clientes = df_vendas.merge(df_clientes, on='id_cliente')
df_vendas_completas = df_vendas_clientes.merge(df_produtos, on='id_produto')
df_vendas_completas['total'] = df_vendas_completas['preco'] * df_vendas_completas['quantidade']
df_total = df_vendas_completas.groupby('categoria')['total'].sum().sort_values(ascending=False)
df_total_cidade = df_vendas_completas.groupby('cidade')['total'].sum().sort_values(ascending=False)
df_total_produtos = df_vendas_completas.groupby(['cidade', 'nome_produto'])['quantidade'].sum().sort_values(ascending=False)
df_top_produtos = df_total_produtos.reset_index().sort_values(['cidade', 'quantidade'], ascending=[True, False])
df_top_produtos = df_top_produtos.groupby('cidade').head(1)




print(df_vendas_completas.head())
print(df_total.head())
print(df_total_cidade.head())
print(df_total_produtos.head())
print(df_top_produtos)

