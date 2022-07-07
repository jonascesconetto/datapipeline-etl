# Importações necessárias
from airflow import DAG
import airflow.utils.dates
from airflow.operators.bash import BashOperator

# Definição da Classe DAG
dag = DAG(
    dag_id="01_hello_world", #Tem que ser único
    description="A primeira DAG de teste do airflow",
    start_date=airflow.utils.dates.days_ago(14),
    schedule_interval=None,
)

# BashOperator do Airflow
task_echo_message = BashOperator(
    task_id="echo_message",
    bash_command="echo Hello World!",
    dag=dag,
)

task_echo_message
