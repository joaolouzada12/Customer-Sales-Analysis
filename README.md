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
- Average ticket (ticket médio) per city  

Business questions answered:

- Where is the company making more money?
- Which cities generate more revenue?
- What products perform best in each region?
- Which locations have higher customer spending per purchase?

## Technologies

- Python
- Pandas

## Project Structure

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

src/
  gerar_dados_nivel2.py
  analise.py

## Key Learnings

- Working with relational datasets using IDs  
- Performing joins with Pandas (`merge`)  
- Creating business metrics (revenue, ticket average)  
- Using `groupby` for analytical insights  
- Extracting top values within grouped data  
- Structuring a clean and readable data analysis pipeline  
- Exporting processed data for further use  

## Status

In progress.

Next steps:

- Add time-based analysis (monthly revenue, trends)
- Create visualizations (Matplotlib)
- Improve project documentation and storytelling