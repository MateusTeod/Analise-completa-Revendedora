# 🚗 Análise de Dados - Revendedora de Veículos

## 📌 Sobre o Projeto

Este projeto tem como objetivo simular um cenário real de análise de dados em uma revendedora de veículos, passando por todas as etapas do processo de ETL (Extração, Transformação e Carga), desde a manipulação dos dados em Python até a criação de dashboards interativos no Power BI.

O projeto foi desenvolvido para praticar conceitos de:

* Análise de Dados
* ETL com Python
* Limpeza e transformação de dados
* Modelagem para BI
* Criação de dashboards gerenciais
* Storytelling com dados

---

## 🎯 Objetivos de Negócio

Responder perguntas estratégicas como:

* Quantos veículos foram vendidos?
* Qual marca possui maior volume de vendas?
* Qual faixa de preço apresenta maior demanda?
* Qual combustível é mais vendido?
* Qual vendedor gera mais receita?
* Qual marca apresenta maior lucratividade?
* Qual a margem média das vendas?
* Qual o perfil dos veículos vendidos?

---

## 📂 Estrutura do Projeto

```text
Projeto_Revendedora/

├── dados_brutos/
│   └── used_car_sales.csv
│
├── dados_tratados/
│   └── used_car_sales_tratado.csv
│
├── notebooks/
│
├── dashboard/
│
├── documentacao/
│   └── ETL_Planejamento.md
│
└── README.md
```

---

## 📊 Dataset

Fonte dos dados:

* Used Car Sales Dataset

Características do dataset:

* 10.000 registros
* 25 colunas
* Dados de vendas de veículos
* Informações sobre estoque, vendas, vendedores e rentabilidade

---

## 🔄 Processo ETL

### Extração

* Importação do arquivo CSV utilizando Python e Pandas.
* Validação da estrutura dos dados.
* Verificação de tipos de dados.

### Transformação

* Conversão de colunas de data.
* Tratamento de registros não vendidos.
* Criação de colunas derivadas.
* Classificação por faixa de preço.
* Classificação por faixa de quilometragem.
* Cálculo de lucro por veículo.

### Carga

* Exportação da base tratada.
* Integração com Power BI para construção dos dashboards.

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Visual Studio Code
* Excel
* Power BI
* Git
* GitHub

---

## 📈 Dashboards

O dashboard será dividido em:

### Visão Geral

* Total de veículos
* Total de vendas
* Taxa de conversão
* Receita total

### Comercial

* Vendas por marca
* Vendas por modelo
* Vendas por combustível

### Estoque

* Veículos disponíveis
* Faixa de quilometragem
* Faixa de preço

### Financeiro

* Lucro total
* Margem média
* Lucro por marca

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos relacionados a:

* Limpeza de dados
* Qualidade dos dados
* ETL
* Análise exploratória
* Indicadores de negócio
* Desenvolvimento de dashboards
* Boas práticas de documentação

---

## 🚀 Próximos Passos

* Finalizar tratamento dos dados.
* Criar camada Gold para análise.
* Desenvolver dashboard completo no Power BI.
* Publicar dashboard online.
* Adicionar capturas de tela e insights obtidos.

---

## 👨‍💻 Autor

Mateus Teodoro da Silva

Estudante de Análise e Desenvolvimento de Sistemas, com foco em Análise de Dados, Business Intelligence e Desenvolvimento de Software.
