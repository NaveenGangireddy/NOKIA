from datetime import datetime
import time
import pytest
from playwright.sync_api import expect
from NOKIA.utils.common_service_file import Utils

class UAM:
    def __init__(self, page):
        self.page = page
    def create_role(self, role_name):
        self.page.get_by_role("button", name= "Administration").click()
        self.page.get_by_role("button", name= "Roles").click()
        self.page.get_by_role("button", name= "Create New Role").click()
        self.page.get_by_role("textbox", name= "Name").fill(role_name)
        self.page.locator("[aria-labelledby='address-country']").click()
        self.page.get_by_role("option", name= "CSP").click()
        self.page.get_by_placeholder("Description").fill("tested from playwright")
        self.page.get_by_role("checkbox", name= "action").click()
        self.page.get_by_role("button", name= "CREATE").click()
        self.page.get_by_role("alert").wait_for(state="visible")

    def role_view_details(self, name, tab):
        self.page.get_by_role("button", name= "Administration").click()
        self.page.get_by_role("button", name= "Roles").click()
        roles_table = self.page.get_by_role("table").nth(1)
        row_selected = roles_table.get_by_role("row").nth(0)
        row_selected.get_by_role("button", name="View Details").click()
        tablist = self.page.get_by_role("tablist").nth(0)
        tablist.get_by_role("tab", name = tab).click()
        general_panel = self.page.get_by_role("tabpanel", name=tab)
        para = general_panel.get_by_role("paragraph").nth(1)
        text = para.inner_text().strip()
        return  text


    def delete_role(self, role_name):
        self.page.get_by_role("button", name= "Administration").click()
        self.page.get_by_role("button", name= "Roles").click()
        roles_table = self.page.get_by_role("table").nth(1)
        row_selected = roles_table.get_by_role("row").nth(0)
        row_selected.get_by_role("button", name="Delete").click()
        self.page.on("dialog", lambda dialog: dialog.accept()) # confirms the dialog
        dialog = self.page.get_by_role("dialog")
        dialog.get_by_role("button", name="DELETE").click()
        self.page.get_by_role("alert").wait_for(state="visible")

    def create_user_group(self, user_group_name, role_name):
        self.page.get_by_role("button", name="Administration").click()
        self.page.get_by_role("button", name="User Groups").click()
        self.page.get_by_role("button", name="Create New User Group").click()
        self.page.get_by_role("textbox").first.fill(user_group_name)
        self.page.locator("[aria-labelledby='address-country']").click()
        self.page.get_by_role("option", name="CSP").click()
        self.page.get_by_role("textbox", name="Description").fill("tested from playwright")
        self.page.get_by_role("button", name="NEXT").click()
        self.page.get_by_role("button", name="NEXT").click()
        self.page.locator("[aria-labelledby='address-country']").click()
        self.page.get_by_role("option", name=role_name).click()
        self.page.get_by_role("button", name="NEXT").click()
        self.page.get_by_role("button", name="CREATE").click()
        self.page.get_by_role("alert").wait_for(state="visible")

    def check_user_group_in_role_view_details(self, user_group_name, role_name):
        utils = Utils(page=self.page)
        # check whether user group is updated in roles view details
        self.page.get_by_role("button", name="Administration").click()
        self.page.get_by_role("button", name="Roles").click()
        utils.global_search(role_name)
        text = self.role_view_details(user_group_name, "USER GROUPS")
        return text
    




# class Roles:
#     def __init__(self, page):
#         self.page = page
#
#     def create_role(self, role_name):
#         self.page.get_by_role("button", name= "Administration").click()
#         self.page.get_by_role("button", name= "Roles").click()
#         self.page.get_by_role("button", name= "Create New Role").click()
#         self.page.get_by_role("textbox", name= "Name").fill(role_name)
#         self.page.locator("[aria-labelledby='address-country']").click()
#         self.page.get_by_role("option", name= "CSP").click()
#         self.page.get_by_placeholder("Description").fill("tested from playwright")
#         self.page.get_by_role("checkbox", name= "action").click()
#         self.page.get_by_role("button", name= "CREATE").click()
#         self.page.get_by_role("alert").wait_for(state="visible")
#
#
#     def global_search(self, keyword):
#         self.page.get_by_role("searchbox", name="Search").fill(keyword)
#         self.page.get_by_role("searchbox", name="Search").press("Enter")
#         time.sleep(10)
#
#     def get_column_index(self, column_name):
#         header_row = self.page.get_by_role("rowgroup").first.get_by_role("row").nth(0)
#         headers = header_row.get_by_role("columnheader")
#         for i in range(headers.count()):
#             if column_name in headers.nth(i).inner_text():
#                 return i
#         return -1
#
#     def filter_search(self, column_name, keyword):
#
#         idx = self.get_column_index(column_name)
#
#         filter_row = self.page.get_by_role("rowgroup").first.get_by_role("row").nth(1)
#         filterbox = filter_row.get_by_role("textbox", name="Filter").nth(idx - 1)
#         filterbox.fill(keyword)
#         filterbox.press("Enter")
#         time.sleep(6)
#         filter_row.get_by_role("button", name="Search columns").click()
#         time.sleep(10)
#
#     def view_details_row(self, name, tab):
#         roles_table = self.page.get_by_role("table").nth(1)
#         row_selected = roles_table.get_by_role("row").nth(0)
#         row_selected.get_by_role("button", name="View Details").click()
#         tablist = self.page.get_by_role("tablist").nth(0)
#         tablist.get_by_role("tab", name = tab).click()
#         general_panel = self.page.get_by_role("tabpanel", name=tab)
#         para = general_panel.get_by_role("paragraph").nth(1)
#         text = para.inner_text().strip()
#         return  text
#
#     def delete_role(self, role_name):
#
#         roles_table = self.page.get_by_role("table").nth(1)
#         row_selected = roles_table.get_by_role("row").nth(0)
#         row_selected.get_by_role("button", name="Delete").click()
#         self.page.on("dialog", lambda dialog: dialog.accept()) # confirms the dialog
#         dialog = self.page.get_by_role("dialog")
#         dialog.get_by_role("button", name="DELETE").click()
#         self.page.get_by_role("alert").wait_for(state="visible")
#
# class User_group(Roles):
#     def __init__(self, page):
#         super().__init__(page)
#         self.page = page
#
#     def create_user_group(self, user_group_name, role_name):
#         self.page.get_by_role("button", name="Administration").click()
#         self.page.get_by_role("button", name="User Groups").click()
#         self.page.get_by_role("button", name="Create New User Group").click()
#         self.page.get_by_role("textbox").first.fill(user_group_name)
#         self.page.locator("[aria-labelledby='address-country']").click()
#         self.page.get_by_role("option", name="CSP").click()
#         self.page.get_by_role("textbox", name="Description").fill("tested from playwright")
#         self.page.get_by_role("button", name="NEXT").click()
#         self.page.get_by_role("button", name="NEXT").click()
#         self.page.locator("[aria-labelledby='address-country']").click()
#         self.page.get_by_role("option", name=role_name).click()
#         self.page.get_by_role("button", name="NEXT").click()
#         self.page.get_by_role("button", name="CREATE").click()
#         self.page.get_by_role("alert").wait_for(state="visible")
#
#     def check_user_group_in_role_view_details(self, user_group_name, role_name):
#         role = User_group(page=self.page)
#         # check whether user group is updated in roles view details
#         self.page.get_by_role("button", name="Administration").click()
#         self.page.get_by_role("button", name="Roles").click()
#         role.global_search(role_name)
#         text = role.view_details_row(user_group_name, "USER GROUPS")
#         return text
#         time.sleep(5)
#











