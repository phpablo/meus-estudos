from airflow.decorators import dag, task
from pendulum import datetime

# Enviando por uma task só, uma lista de valores no formato JSON e usando tipo moderno de sem usar manualmente o ti.xcom
# Já que minha task_a vai só me passar um valor, eu retorno por ela , logo, atribuo a uma var e na task_b eu passo essa var como argumento
# o aiflow entende que o return é um xcom_push, e a task_b recebendo a como argumento, entende que é um ti.xcom_pull automaticamente
@dag(
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=['exemplo_json_xcom']
)
def xcom_dag():

    @task
    def task_a():
        # No TaskFlow, o que você der 'return' vira XCom automaticamente
        vals = {
            "val_1": 4,
            "val_2": 3
        }
        return vals

    @task
    def task_b(dados_recebidos):
        # O Airflow já entrega o dicionário pronto aqui
        print(f"Valores recebidos: {dados_recebidos}")
        print(f"Valor 1 é: {dados_recebidos['val_1']}")
        print(f"Valor 2 é: {dados_recebidos['val_2']}")

    # A mágica do TaskFlow: passamos o retorno de uma como argumento da outra
    # O Airflow entende a dependência e faz o XCom Pull sozinho
    dados = task_a()
    task_b(dados)

xcom_dag()

##############################################################################################

# Envia uma dag com duas tarefas fazendo push e uma fazendo Pull, de multiplos valores, passando como argumento no pull, uma lista de tasks, que possuem a mesma key e ordenando a chamada das tasks baseado nas suas dependencias

# @dag
# def xcom_dag():

#   @task
#   def task_a(ti):
#     val = 42
#     ti.xcom_push(key="my_key",value=val)

#   @task
#   def task_c(ti):
#     val = 43
#     ti.xcom_push(key="my_key",value=val)

#   @task
#   def task_b(ti):
#     vals =ti.xcom_pull(task_ids=["task_a","task_c"],key="my_key")
#     print(vals)

#   task_a() >> task_c() >> task_b()

# xcom_dag()


##############################################################################################
# This is a sample DAG to demonstrate the use of Airflow's TaskFlow API. It defines a simple workflow with multiple tasks that are executed in a specific order. The DAG is scheduled to run daily, starting from January 1, 2026, and it will not catch up on missed runs. The tasks include printing values and demonstrating task dependencies using the chain function.
# @dag(
#   'my_dag_fixed',
#   schedule="@daily",
#   start_date=datetime(2026,1,1),
#   catchup=False,
#   description="This tag does...something",
#   tags=["team_a", "source_a"],
#   max_consecutive_failed_dag_runs=3,
# )
# def my_dag():
  

#   @task
#   def task_a():
#     val = {
#       "key1": 42,
#       "key2": 43
#     }
#     return val
  
#   @task
#   def task_b(**val):
#     print(val)  
  
#   @task
#   def task_c():
#     print("This is task C") 
  
#   @task
#   def task_d():
#     print("This is task D")
  
#   @task
#   def task_e():
#     print("This is task E")
  
#   task_a() >> task_b(task_a()) 
 
#  # chain(task_a(), [task_b(),task_c()],[task_d(),task_e()])
  
# my_dag()