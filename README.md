# Relational Sales Analysis

This is an intermediate-level data analysis project using Python and Pandas.

The dataset is simulated and structured in a relational format, requiring joins between multiple tables before performing analysis — similar to real-world business scenarios.

## Project Overview

This project simulates a real-world data analysis workflow using relational datasets.

The data is organized into three main tables:

* clients
* products
* sales

The objective is to transform raw transactional data into meaningful business insights through data processing, aggregation, and analysis.

---

## Data Pipeline

1. Data ingestion (CSV files)
2. Data merging (relational joins)
3. Feature engineering (creating new metrics)
4. Data analysis (groupby operations)
5. Data export (processed outputs)

---

## Analysis Performed

After merging the datasets and creating the `total` column, the following analyses were performed:

* Revenue by category
* Revenue by city
* Quantity of products sold by city
* Top-selling product per city
* Average ticket per city

### Time-based Analysis

* Revenue per month
* Number of sales per month
* Monthly comparison between revenue and sales volume
* Average ticket per month

These analyses provide a clear view of sales performance across different dimensions, including geography, product categories, and time.

---
### Data Visualization

To better understand the patterns in the data, visualizations were created using Seaborn and Matplotlib:

* Bar chart: Revenue by category
* Line chart: Revenue over time
* Line chart: Number of sales over time
* Combined line chart: Revenue vs number of sales (dual-axis)

These visualizations help highlight trends, compare performance across dimensions, and support more accurate business interpretations.

## Key Insights

* The analysis shows that revenue distribution varies significantly across categories, indicating differences in product value and demand.
* Some cities generate higher revenue not necessarily due to volume, but due to higher average ticket size.
* Revenue and number of sales do not always grow together, highlighting variations in customer purchasing behavior.
* Certain months show higher revenue even with fewer sales, suggesting higher-value transactions during those periods.

These findings demonstrate how combining multiple datasets can uncover patterns in customer behavior and business performance.

---

## Technologies & Tools

* Python
* Pandas
* CSV (data storage)

---

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
```
