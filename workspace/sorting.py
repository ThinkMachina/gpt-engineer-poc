from operator import attrgetter

class Sorting:
    def sort_tasks(self, tasks, sort_by, sort_order):
        if sort_by == "id":
            tasks.sort(key=attrgetter("id"), reverse=(sort_order == "desc"))
        elif sort_by == "name":
            tasks.sort(key=attrgetter("name"), reverse=(sort_order == "desc"))
        elif sort_by == "due_date":
            tasks.sort(key=attrgetter("due_date"), reverse=(sort_order == "desc"))
        return tasks
