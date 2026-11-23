import sqlite3
from pathlib import Path

DB_PATH = Path("tasks.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, tenant_id TEXT NOT NULL, title TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'queued')"
        )

def create_task(tenant_id: str, title: str):
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            "INSERT INTO tasks(tenant_id, title) VALUES (?, ?)", (tenant_id, title)
        )
        return {"id": cursor.lastrowid, "tenant_id": tenant_id, "title": title, "status": "queued"}

def list_tasks(tenant_id: str):
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        rows = conn.execute(
            "SELECT id, title, status FROM tasks WHERE tenant_id = ? ORDER BY id DESC", (tenant_id,)
        ).fetchall()
    return [{"id": row[0], "title": row[1], "status": row[2]} for row in rows]
