# Projeto bigqueryBTC: Pipeline de ETL com BigQuery e Automação no GCP

Este projeto implementa um pipeline de ETL (Extract, Transform, Load) para processar dados históricos de Bitcoin (BTC) da Yahoo Finance API, armazená-los no Google Cloud Storage (GCS), transformá-los e carregá-los no BigQuery. O pipeline é automatizado usando **Cloud Scheduler** para execução periódica e **Pub/Sub** para notificações de status.

---

## Estrutura do Projeto

📂 bigqueryBTC/
├── 📂 scripts/ # Scripts Python para ETL e automação
│ ├── extract.py # Extrai dados da Yahoo Finance API e salva no GCS
│ ├── transform.py # Limpa e transforma os dados
│ ├── load.py # Carrega os dados no BigQuery
│ ├── etl_pipeline.py # Orquestra o pipeline de ETL
│ ├── pubsub.py # Envia notificações via Pub/Sub
│ ├── scheduler.py # Configura o Cloud Scheduler
│ ├── config.py # Configurações globais do projeto
│ └── requirements.txt # Dependências do projeto
├── 📂 sql/ # Scripts SQL para criação das tabelas no BigQuery
│ ├── create_raw.sql # Cria a tabela RAW
│ ├── create_trusted.sql # Cria a tabela TRUSTED
│ ├── create_refined.sql # Cria a tabela REFINED
├── 📂 docs/ # Documentação do projeto
│ ├── README.md # Este arquivo
│ ├── setup.md # Passos para configuração no GCP
│ ├── architecture.md # Arquitetura do pipeline
├── 📂 credentials/ # Pasta para armazenar credenciais
│ └── credenciais.json # Chave de serviço do GCP
└── .gitignore # Ignora arquivos sensíveis

---

## Pré-requisitos

- **Conta no GCP**: Acesse o [Google Cloud Platform](https://cloud.google.com/) e crie um projeto.
- **APIs Ativadas**: Ative as APIs do GCS, BigQuery, Pub/Sub e Cloud Scheduler.
- **Python 3.8+**: Certifique-se de ter o Python instalado.
- **Chave de Serviço**: Gere uma chave de serviço no GCP e salve-a como `credenciais.json` na pasta `credentials/`.

---

## Como Executar

1. **Instale as Dependências**:
   pip install -r scripts/requirements.txt

2. **Configure as Credenciais**:
   Defina a variável de ambiente:
      export GOOGLE_APPLICATION_CREDENTIALS="credentials/credenciais.json"

3. **Execute o pipeline**:
   Para execução manual:
      python scripts/etl_pipeline.py

   Para execução automática, configure o cloud scheduler:
      python scripts/scheduler.py

---

## Documentação Adicional
[Configuração no GCP](setup.md): Passos detalhados para configurar o ambiente no GCP.

[Arquitetura do Pipeline](architecture.md): Explicação detalhada da arquitetura e fluxo de dados.

---