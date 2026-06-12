Regra ETL-01
| Coluna         | Problema          | Ação                             |
| -------------- | ----------------- | -------------------------------- |
| Purchased Date | Texto             | Converter para Data              |
| Sold Date      | Texto             | Converter para Data              |
| Sold Date      | Possui 1970-01-01 | Tratar conforme regra de negócio |

Regra ETL-02

Problema:
Foram identificados 213 registros onde a data de venda era anterior à data de compra.

Validação:
Os registros apresentavam inconsistência temporal e não representavam um cenário de negócio válido.

Ação:
Removidos da camada Silver.

Impacto:
213 registros removidos (2,13% da base).