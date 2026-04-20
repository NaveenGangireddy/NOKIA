import time

class Utils:
    def __init__(self, page):
        self.page = page

    def global_search(self, keyword):
        self.page.get_by_role("searchbox", name="Search").fill(keyword)
        self.page.get_by_role("searchbox", name="Search").press("Enter")
        time.sleep(10)

    def get_column_index(self, column_name):
        header_row = self.page.get_by_role("rowgroup").first.get_by_role("row").nth(0)
        headers = header_row.get_by_role("columnheader")
        for i in range(headers.count()):
            if column_name in headers.nth(i).inner_text():
                return i
        return -1

    def filter_search(self, column_name, keyword):

        idx = self.get_column_index(column_name)

        filter_row = self.page.get_by_role("rowgroup").first.get_by_role("row").nth(1)
        filterbox = filter_row.get_by_role("textbox", name="Filter").nth(idx - 1)
        filterbox.fill(keyword)
        filterbox.press("Enter")
        time.sleep(6)
        filter_row.get_by_role("button", name="Search columns").click()
        time.sleep(10)

