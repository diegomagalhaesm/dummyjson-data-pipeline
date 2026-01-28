# DummyJSON Data Pipeline – ETL com Python e PostgreSQL

Projeto de pipeline de dados completo (ETL) que consome dados dinâmicos de uma API pública, realiza tratamento e normalização e carrega os dados em um banco PostgreSQL para análise posterior e construção de dashboards.

Este projeto foi desenvolvido com foco em boas práticas de Engenharia de Dados Júnior e Análise de Dados.

---

## 📌 Objetivo

Demonstrar, na prática, a construção de um pipeline de dados moderno:

* Extração de dados via API REST
* Transformação e limpeza com Python
* Carga estruturada em banco relacional
* Organização modular do código
* Uso de variáveis de ambiente
* Preparação para análise e BI

---

## 🧱 Arquitetura do Pipeline

[![](https://mermaid.ink/img/pako:eNo9kU1PwkAQhv_KZk6aFOx3uz2YAMUEg1rFky2Htbu0RHaXTLdBJPx324LOaWaf5905zAlKzQUksNnpQ1kzNGT5VijS1SSfZAuStlIeH1cvz2syGt2TaT7_NshKQ0YkO5paq_XFng54lr8jU81Go-wFpjhrrsJsENJ8qRnv2Op1OdmVtZDHK08HPs9vMt2YCkUn3F7RfEAPeaYPAsl0Qe5Iypr6UzPkzRosqHDLITHYCgukQMn6EU59ugDTLREFJF3LGX4VUKhzl9kz9aG1_Iuhbqsakg3bNd3U7jkzIt2yCpn8f0WhuMCZbpWBxAns4RNITvANiRuO_SAMXUrdIHKjILLg2EvxOIpp6NiO78V-aHtnC36GtfaY-h6NaRD51KauY3sWCL41Gp8uFxkOc_4FWSJ8Ug?type=png)](https://mermaid.live/edit#pako:eNo9kU1PwkAQhv_KZk6aFOx3uz2YAMUEg1rFky2Htbu0RHaXTLdBJPx324LOaWaf5905zAlKzQUksNnpQ1kzNGT5VijS1SSfZAuStlIeH1cvz2syGt2TaT7_NshKQ0YkO5paq_XFng54lr8jU81Go-wFpjhrrsJsENJ8qRnv2Op1OdmVtZDHK08HPs9vMt2YCkUn3F7RfEAPeaYPAsl0Qe5Iypr6UzPkzRosqHDLITHYCgukQMn6EU59ugDTLREFJF3LGX4VUKhzl9kz9aG1_Iuhbqsakg3bNd3U7jkzIt2yCpn8f0WhuMCZbpWBxAns4RNITvANiRuO_SAMXUrdIHKjILLg2EvxOIpp6NiO78V-aHtnC36GtfaY-h6NaRD51KauY3sWCL41Gp8uFxkOc_4FWSJ8Ug)
---

## 🛠 Tecnologias utilizadas

* Python 3.14+
* Requests
* Pandas
* SQLAlchemy
* PostgreSQL
* Power BI (dashboards)
* Git & GitHub

---

## 📁 Estrutura do projeto

```
dummyjson-data-pipeline/
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── db/
│   └── schema.sql
│
├── logs/
├── dashboards/
├── main.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Configuração do ambiente

### 1. Clonar o projeto

```bash
git clone https://github.com/seu-usuario/dummyjson-data-pipeline.git
cd dummyjson-data-pipeline
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar banco de dados

Criar banco no PostgreSQL:

```sql
CREATE DATABASE dummy_pipeline;
```

Executar o script:

```sql
\i db/schema.sql
```

### 5. Configurar conexão

No arquivo `config.py`:

```python
DB_URL = "postgresql://usuario:senha@localhost:5432/dummy_pipeline"
```

---

## ▶️ Executar pipeline

```bash
python main.py
```

---

## 📊 Dashboards

Os dashboards são desenvolvidos no Power BI a partir da tabela `fact_orders`.

Indicadores sugeridos:

* Total de pedidos
* Receita total
* Ticket médio
* Pedidos por status
* Pedidos por data
* Top clientes
* Top produtos

Arquivo PBIX armazenado na pasta:

```
dashboards/
```

---

## 🧠 Conceitos aplicados

* ETL (Extract, Transform, Load)
* Modelagem analítica
* Normalização de dados
* Qualidade de dados
* Pipelines
* SQL
* Versionamento
* Boas práticas de projeto

---

## 🚀 Próximos aprimoramentos

* Incremental Load
* Logs estruturados
* Dockerização
* Orquestração (Airflow / Prefect)
* Testes automatizados
* CI/CD

---

## 👤 Autor

Diego Magalhães Menezes
Analista de Dados em transição | SQL | Python | BI

LinkedIn: [https://www.linkedin.com/in/diegomagalhaesmenezes/](https://www.linkedin.com/in/diegomagalhaesmenezes/)

---

## 📄 Licença

Projeto livre para fins educacionais e portfólio.
