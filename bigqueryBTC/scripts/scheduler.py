from google.cloud import scheduler_v1
from google.cloud.scheduler_v1.types import Job, HttpTarget
from config import PROJECT_ID

def create_scheduler_job(project_id: str, location: str, job_name: str, schedule: str, url: str):
    client = scheduler_v1.CloudSchedulerClient()
    parent = f"projects/{project_id}/locations/{location}"
    job = Job(
        name=f"{parent}/jobs/{job_name}",
        http_target=HttpTarget(
            uri=url,
            http_method="POST",
        ),
        schedule=schedule,
    )
    client.create_job(parent=parent, job=job)

if __name__ == "__main__":
    location = "us-central1"
    job_name = "bigquerybtc-etl-job"
    schedule = "0 0 * * *"
    url = "https://sua-cloud-function-url"
    create_scheduler_job(PROJECT_ID, location, job_name, schedule, url)