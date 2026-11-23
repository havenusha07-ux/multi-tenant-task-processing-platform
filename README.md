# Multi-Tenant Task Processing Platform (Starter)

A small API for submitting and listing tasks scoped to an organization (tenant).

## Tech stack
- Python 3.11+
- FastAPI
- SQLite (starter persistence)
- Pydantic
- pytest

## Setup
```bash
python -m venv .venv
# Windows:
.venv\\Scripts\\activate
# Linux/macOS:
source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
uvicorn task_platform.api:app --reload
```
Open http://127.0.0.1:8000/docs.

## Endpoints
- `POST /tenants/{tenant_id}/tasks` — create a task
- `GET /tenants/{tenant_id}/tasks` — list tasks for that tenant

## Development status
Starter implementation with tenant-scoped queries. Add authentication, Redis-backed queues, worker processes, rate limiting, migrations, and integration tests before treating this as production-ready.
