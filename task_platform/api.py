from fastapi import FastAPI
from pydantic import BaseModel, Field
from .storage import create_task, list_tasks

app = FastAPI(title="Multi-Tenant Task Platform", version="0.1.0")

class TaskRequest(BaseModel):
    title: str = Field(min_length=1, max_length=200)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tenants/{tenant_id}/tasks")
def submit_task(tenant_id: str, payload: TaskRequest):
    return create_task(tenant_id, payload.title)

@app.get("/tenants/{tenant_id}/tasks")
def get_tasks(tenant_id: str):
    return list_tasks(tenant_id)
