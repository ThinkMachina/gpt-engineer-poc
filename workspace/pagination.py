class Pagination:
    def paginate(self, tasks, page, per_page):
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        return tasks[start_index:end_index]

    def get_total_pages(self, total_items, per_page):
        return (total_items + per_page - 1) // per_page
