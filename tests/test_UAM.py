import os
from datetime import datetime
import time
import pytest
from playwright.sync_api import expect
from NOKIA.pages.UAM import UAM
from NOKIA.utils.common_service_file import Utils

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
role_name = "playwright_role_"+timestamp
ug_role_name = "playwright_CSP_UG_role_"+timestamp
role_delete = "playwright_role_delete_"+timestamp
user_group_name = "playwright_user_group_"+timestamp

def test_create_role(test_authenticate, request, role = role_name):

    role = UAM(test_authenticate)
    directory = request.config.run_dir
    role.create_role(role_name)
    expect(role.page.get_by_role("alert")).to_contain_text("Successfully created a new role")
    # Screenshot after creating
    role.page.screenshot(path=f"{directory}/role_create_{timestamp}.png")
    time.sleep(5)
    print(f'1. test_create_role is done with creation of {role_name}')



def test_role_global_search(test_authenticate, request):
    #Global search
    util = Utils(test_authenticate)
    directory = request.config.run_dir
    util.global_search(role_name)
    # Screenshot after global searching
    util.page.screenshot(path=f"{directory}/role_global_search_{timestamp}.png")
    time.sleep(5)

    print(f'2. test_global_search is done for {role_name}')

def test_role_local_search_view_details(test_authenticate, request):
    #filter in column
    """structure we have in our portal
    -table
        -rowgroup
            -row(header)
                -column
                -column
            -row(filter)
                -column
                -column
    -table
        -row(values)
            -cell1
            -cell2
        -row(values)
            -cell1
            -cell2
    """

    directory = request.config.run_dir
    util = Utils(test_authenticate)
    uam = UAM(test_authenticate)



    util.filter_search("Name", role_name)
    # Screenshot after filter
    util.page.screenshot(path=f"{directory}/role_local_search_{timestamp}.png")
    time.sleep(5)

    text = uam.role_view_details(role_name, "GENERAL")
    assert text == role_name
    time.sleep(5)
    uam.page.screenshot(path=f"{directory}/role_view_details_{timestamp}.png")

    print(f'3. test_local_search_view_details is done for {role_name}')



def test_role_delete(test_authenticate, request):
    uam = UAM(test_authenticate)
    util = Utils(test_authenticate)
    directory = request.config.run_dir
    uam.create_role(role_delete)
    util.global_search(role_delete)
    uam.delete_role(role_delete)
    expect(uam.page.get_by_role("alert")).to_contain_text("Successfully deleted the role")
    uam.page.screenshot(path=f"{directory}/role_delete_{timestamp}.png")
    time.sleep(10)
    print(f'4. test_delete_role is done for {role_delete}')

def test_create_user_group(test_authenticate, request):
    uam = UAM(test_authenticate)
    directory = request.config.run_dir
    uam.create_role(ug_role_name)
    uam.create_user_group(user_group_name, ug_role_name)
    expect(uam.page.get_by_role("alert")).to_contain_text("Successfully created a new user group")
    # Screenshot after creating
    uam.page.screenshot(path=f"{directory}/user_group_create_{timestamp}.png")
    time.sleep(5)
    print(f'1. test_create_user_group is done with creation of {user_group_name}')
    text = uam.check_user_group_in_role_view_details(user_group_name, ug_role_name)
    assert text == user_group_name
    uam.page.screenshot(path=f"{directory}/UG_in_role_{timestamp}.png")



def test_user_group_global_search(test_authenticate, request):
    uam = UAM(test_authenticate)
    directory = request.config.run_dir

    #Global search
    util = Utils(test_authenticate)
    directory = request.config.run_dir
    util.global_search(user_group_name)
    # Screenshot after global searching
    util.page.screenshot(path=f"{directory}/role_global_search_{timestamp}.png")
    time.sleep(5)

    print(f'2. test_global_search is done for {role_name}')



















