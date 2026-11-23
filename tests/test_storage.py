from task_platform.storage import create_task, list_tasks

def test_tasks_are_scoped_by_tenant():
    create_task("tenant-a", "first")
    create_task("tenant-b", "second")
    assert len(list_tasks("tenant-a")) == 1
    assert list_tasks("tenant-a")[0]["title"] == "first"
