## First steps with Apache Airflow
<!-- Este repositório contém os códigos utilizados durante curso de Data Pipelines com Apache Airflow. -->
### Requisitos
- Necessidade de separar os dados do ambiente OLTP para o ambiente OLAP
- Todas as tarefas devem ser executadas diariamente
- Todo o processo deve ser notificado
- O ambiente de stage deve ser limpo
- Todos os logs devem ser mantidos
## 💻 Principais Tecnologias, Softwares e Bibliotecas
- Docker
- Python
- Apache AirFlow (Data Pipeline)
- MySQL
- Postgres
## ⚙ Instalação e configuração de ambiente
### Docker
  - Seguir a [documentação](https://docs.docker.com/engine/install/) oficial
### Container - Apache AirFlow
  - `Observação: `Abra o terminal em um diretório raiz para subir seu container com Airflow, dessa forma não perdemos os arquivos de DAGs gerados caso seja necessário algumas reinstalação ou configuração adicional do container.
  - Crie container com seguinte comando em seu terminal:
    ```bash
    docker run -d -p 8080:8080 -v "$PWD/airflow/dags:/opt/airflow/dags/" \
    --entrypoint=/bin/bash \
    --name airflow apache/airflow:2.1.1-python3.8 \
    -c '(\
    airflow db init && \
    airflow users create --username <nome de usuário> --password <sua senha> --firstname <Seu nome> --lastname <Seu Nome> --role Admin --email <Seu e-mail>); \
    airflow webserver & \
    airflow scheduler\
    '
    ```
  - Verificando o container em execução.
    ```bash
    docker container ls
    ```
  - Verificando os logs do container
    ```bash
    docker container logs airflow
    ```
  - Se nenhum erro aparecer, acesse a interface web do Apache Airflow pelo endereço:
    
    **https://localhost:8080**
### Container - MySQL/MariaDB (OLTP)
- `Observação: `Assim como na criação do container do Airflow é importante abrir o terminal em um diretório raiz para subir o container.
- Crie o container con o seguinte comando em seu terminal:
  ```bash
  docker run -d --name mysql_oltp -p "3306:3306" -v "$PWD/data:/home/" -e MYSQL_ROOT_PASSWORD=airflow mysql
  ou
  docker run -d --name mariadb_oltp -p "3306:3306" -v "$PWD/data:/home" -e MARIADB_ROOT_PASSWORD=airflow mariadb:latest
  ```
- Verificando o container em execução.
  ```bash
  docker container ls
  ```
- Verificar o mapeamento dos volumes
  ```bash
  docker container exec -it mysql_oltp bash
  ls /home/
  ```
- Conectar com o MySQL/MariaDB dentro do container
  ```bash
  mysql -u root -pairflow
  ```
- Listar os bancos de dados
    ```bash
  show databases;
  ```
- Instalar e configurar recursos adicionais
  - Acesse o container pelo seguinte comando
    ```bash
    docker container exec -it mysql_oltp bash
    ```
  - Executar o seguinte comando
      ```bash
    apt-get update && apt-get install vim iputils-ping -y
    ```
- Carregar dados 
  - Acesse o container pelo seguinte comando
    ```bash
    docker container exec -it mysql_oltp bash
    ```
  - Acessar o diretório `/home/dbs`, e executar o seguinte comando:
    ```bash
    mysql -u root -pairflow < employees.sql
    ```
  - Conectar com o MySQL/MariaDB dentro do container
    ```bash
    mysql -u root -pairflow
    ```
  - Listar os bancos de dados
    ```bash
    show databases;
    ```
### Container - PostgreSQL (OLAP)
- `Observação: `Assim como na criação do container do Airflow é importante abrir o terminal em um diretório raiz para subir o container.
- Crie o container con o seguinte comando em seu terminal:
  ```bash
  docker run --name postgresql_olap -e POSTGRES_PASSWORD=airflow -d postgres
  ```
- Verificando o container em execução.
  ```bash
  docker container ls
  ```
- Conectar com o PostgreSQL dentro do container
  ```bash
  docker container exec -it postgresql_olap bash
  ```
  ```bash
  psql -h localhost -U postgres
  ```
- Listar os bancos de dados
  ```bash
  SELECT datname FROM pg_database;
  ```
- Criar o banco de dados `employees`
  ```bash
  CREATE DATABASE employees;
  ```