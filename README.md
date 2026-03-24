# Relational Sales Analysis

This is an intermediate-level data analysis project using Python and Pandas.

The dataset is simulated and structured in a relational format, requiring joins between multiple tables before performing analysis — similar to real-world business scenarios.

## Project Overview

The data is organized into three main tables:

- clients
- products
- sales

The goal of this project is to simulate a real data workflow, where datasets must be combined and transformed before extracting insights.

## Data Pipeline

1. Data ingestion (CSV files)
2. Data merging (relational joins)
3. Feature engineering (creating new metrics)
4. Data analysis (groupby operations)
5. Data export (processed outputs)

## Analysis Performed

After merging the datasets and creating the `total` column, the following analyses were performed:

- Revenue by category  
- Revenue by city  
- Quantity of products sold by city  
- Top-selling product per city  
- Average ticket per city  

### Time-based Analysis

- Revenue per month  
- Number of sales per month  
- Monthly comparison between revenue and sales volume  
- Average ticket per month  

These analyses allow deeper business insights such as identifying peak sales periods, understanding customer behavior over time, and comparing volume vs revenue performance.

## Technologies

- Python
- Pandas

## Project Structure

```plaintext
data/
  raw/
    clients.csv
    products.csv
    sales.csv

  processed/
    faturamento_categoria.csv
    faturamento_cidade.csv
    quantidade_produto_cidade.csv
    top_produto_cidade.csv
    ticket_cidade.csv
    faturamento_mes.csv
    vendas_mes.csv
    analise_mensal.csv

src/
  gerar_dados_nivel2.py
  analise_nivel2.py