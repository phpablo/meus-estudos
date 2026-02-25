from airflow.decorators import dag,task
from airflow.models.baseoperator import chain
from pendulum import datetime

@dag(
  'my_dag_fixed',
  schedule="@daily",
  start_date=datetime(2026,1,1),
  catchup=False,
  description="This tag does...something",
  tags=["team_a", "source_a"],
  max_consecutive_failed_dag_runs=3,
)
def my_dag():
  

  @task
  def task_a():
    print("This is task A")
    return "Data from task A"
  @task
  def task_b():
    print("This is task B")
  @task
  def task_c():
    print("This is task C") 
  @task
  def task_d():
    print("This is task D")
  @task
  def task_e():
    print("This is task E")
  
  chain(task_a(), [task_b(),task_c()],[task_d(),task_e()])
  
my_dag()