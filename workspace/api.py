from flask import Flask, request, jsonify
from task import Task
from task_manager import TaskManager
from pagination import Pagination
from sorting import Sorting

app = Flask(__name__)
task_manager = TaskManager()
pagination = Pagination()
sorting = Sorting()

@app.route("/tasks", methods=["GET"])
def get_tasks():
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=10, type=int)
    filter_status = request.args.get("filter_status", default=None, type=bool)
    filter_due_date_start = request.args.get("filter_due_date_start", default=None, type=str)
    filter_due_date_end = request.args.get("filter_due_date_end", default=None, type=str)
    sort_by = request.args.get("sort_by", default="due_date", type=str)
    sort_order = request.args.get("sort_order", default="asc", type=str)

    filtered_tasks = task_manager.get_tasks()
    if filter_status is not None:
        filtered_tasks = [task for task in filtered_tasks if task.status == filter_status]
    if filter_due_date_start is not None:
        filtered_tasks = [task for task in filtered_tasks if task.due_date >= filter_due_date_start]
    if filter_due_date_end is not None:
        filtered_tasks = [task for task in filtered_tasks if task.due_date <= filter_due_date_end]

    sorted_tasks = sorting.sort_tasks(filtered_tasks, sort_by, sort_order)
    paginated_tasks = pagination.paginate(sorted_tasks, page, per_page)

    response = {
        "tasks": [task.__dict__ for task in paginated_tasks],
        "total_tasks": len(filtered_tasks),
        "total_pages": pagination.get_total_pages(len(filtered_tasks), per_page),
        "current_page": page,
        "per_page": per_page
    }
    return jsonify(response)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description", "")
    due_date = data.get("due_date", "")
    task = Task(name, description, due_date)
    task_id = task_manager.add_task(task)
    return jsonify({"task_id": task_id}), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def edit_task(task_id):
    data = request.get_json()
    name = data.get("name")
    description = data.get("description", "")
    due_date = data.get("due_date", "")
    if task_manager.edit_task(task_id, name, description, due_date):
        return jsonify({"message": "Task updated successfully"})
    else:
        return jsonify({"message": "Task not found"}), 404

@app.route("/tasks/<int:task_id>/complete", methods=["PUT"])
def mark_task_as_complete(task_id):
    if task_manager.mark_task_as_complete(task_id):
        return jsonify({"message": "Task marked as complete"})
    else:
        return jsonify({"message": "Task not found"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    if task_manager.delete_task(task_id):
        return jsonify({"message": "Task deleted successfully"})
    else:
        return jsonify({"message": "Task not found"}), 404

if __name__ == "__main__":
    app.run()
