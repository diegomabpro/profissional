# Arquitetura do Pipeline de Dados - bigqueryBTC

Este documento descreve a arquitetura do pipeline de ETL (Extract, Transform, Load) desenvolvido para processar dados históricos de Bitcoin (BTC) da Yahoo Finance API, armazená-los no Google Cloud Storage (GCS), transformá-los e carregá-los no BigQuery. O pipeline é automatizado usando **Cloud Scheduler** para execução periódica e **Pub/Sub** para notificações de status.

---

## Visão Geral

O pipeline é dividido em três camadas principais:

1. **RAW**: Armazena os dados brutos extraídos da fonte.
2. **TRUSTED**: Contém os dados limpos e normalizados.
3. **REFINED**: Apresenta os dados prontos para análise, com agregações e cálculos.

O fluxo de dados segue o processo ETL clássico, com etapas de extração, transformação e carga, além de notificações e agendamento automático.

---

## Componentes do Pipeline

### 1. **Extração**
- **Fonte de Dados**: Yahoo Finance API (dados históricos de Bitcoin).
- **Ferramenta**: Script Python (`extract.py`).
- **Processo**:
  - O script baixa os dados da API.
  - Salva os dados brutos no Google Cloud Storage (GCS) na camada **RAW** (`bigquerybtc-bucket/raw`).

### 2. **Transformação**
- **Ferramenta**: Script Python (`transform.py`).
- **Processo**:
  - Carrega os dados brutos do GCS.
  - Realiza a limpeza e normalização dos dados.
  - Salva os dados processados no GCS na camada **TRUSTED** (`bigquerybtc-bucket/trusted`).

### 3. **Carga**
- **Ferramenta**: Script Python (`load.py`).
- **Processo**:
  - Carrega os dados transformados do GCS para o BigQuery.
  - Organiza os dados em três camadas no BigQuery:
    - **RAW**: Tabela `bigquerybtc_raw` com os dados brutos.
    - **TRUSTED**: Tabela `bigquerybtc_trusted` com os dados limpos e normalizados.
    - **REFINED**: Tabela `bigquerybtc_refined` com dados prontos para análise.

### 4. **Notificações**
- **Ferramenta**: Script Python (`pubsub.py`).
- **Processo**:
  - Publica mensagens no tópico `bigquerybtc-topic` do **Pub/Sub** indicando o status da execução do pipeline (sucesso ou falha).

### 5. **Agendamento**
- **Ferramenta**: Script Python (`scheduler.py`).
- **Processo**:
  - Configura o **Cloud Scheduler** para executar o pipeline periodicamente.
  - O scheduler aciona o script `etl_pipeline.py`, que orquestra todo o processo de ETL.

---

## Diagrama de Arquitetura

```plaintext
Yahoo Finance API
        ↓
    [Extract]
        ↓
    GCS (bigquerybtc-bucket/raw)
        ↓
    [Transform]
        ↓
    GCS (bigquerybtc-bucket/trusted)
        ↓
    [Load]
        ↓
    BigQuery (bigquerybtc_dataset)
        ↓
    [Pub/Sub] → Notificações no tópico bigquerybtc-topic
        ↓
    [Cloud Scheduler] → Execução Automática