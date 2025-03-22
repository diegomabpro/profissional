# Configuração no GCP

Este guia detalha os passos necessários para configurar o ambiente no Google Cloud Platform (GCP) e executar o pipeline de ETL.

---

## Passos para Configuração

### 1. **Criar um Projeto no GCP**
   - Acesse o [Console do GCP](https://console.cloud.google.com/).
   - Crie um projeto com o ID `bigqueryBTC`.

### 2. **Ativar as APIs Necessárias**
   - No Console do GCP, ative as seguintes APIs:
     - **Google Cloud Storage (GCS)**
     - **BigQuery**
     - **Pub/Sub**
     - **Cloud Scheduler**

### 3. **Criar um Bucket no GCS**
   - Navegue até o [Google Cloud Storage](https://console.cloud.google.com/storage).
   - Crie um bucket chamado `bigquerybtc-bucket`.
   - Dentro do bucket, crie duas pastas:
     - `raw/`: Para armazenar os dados brutos.
     - `trusted/`: Para armazenar os dados transformados.

### 4. **Criar um Dataset no BigQuery**
   - Navegue até o [BigQuery](https://console.cloud.google.com/bigquery).
   - Crie um dataset chamado `bigquerybtc_dataset`.
   - Execute os scripts SQL (`create_raw.sql`, `create_trusted.sql`, `create_refined.sql`) para criar as tabelas.

### 5. **Configurar o Pub/Sub**
   - Navegue até o [Pub/Sub](https://console.cloud.google.com/cloudpubsub).
   - Crie um tópico chamado `bigquerybtc-topic`.

### 6. **Configurar o Cloud Scheduler**
   - Navegue até o [Cloud Scheduler](https://console.cloud.google.com/cloudscheduler).
   - Crie um job chamado `bigquerybtc-etl-job`.
   - Configure a frequência de execução (por exemplo, `0 0 * * *` para diariamente à meia-noite).
   - Defina o alvo do job (por exemplo, um Cloud Function ou Cloud Run).

### 7. **Configurar o Ambiente Local**
   - Instale as dependências do projeto:
      pip install -r scripts/requirements.txt
   - Coloque o arquivo `credenciais.json` na pasta `credentials/`.
   - Defina a variável de ambiente:
      export GOOGLE_APPLICATION_CREDENTIALS="credentials/credenciais.json"

---

## Solução de Problemas

- **Erros de Autenticação**: Verifique se as credenciais estão corretas e se a variável de ambiente está configurada.
- **Falhas no Pipeline**: Consulte os logs do GCP ou as mensagens de erro no Pub/Sub.
- **Problemas de Agendamento**: Verifique a configuração do Cloud Scheduler e a URL de acionamento.

---

## Próximos Passos

- **Monitoramento**: Configure alertas e dashboards para monitorar o pipeline.
- **Otimização**: Ajuste as configurações de recursos (por exemplo, memória e CPU) para melhorar o desempenho.
- **Expansão**: Adicione novas fontes de dados ou transformações ao pipeline.