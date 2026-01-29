from project_yougile import ProjectsApi

base_url = 'https://ru.yougile.com/api-v2/'
api = ProjectsApi(base_url)

def test_create_project_positive():
    body_before = api.get_list_project()
    assert body_before.status_code == 200
    assert len(body_before.json()["content"]) > 0
    title = "Testing"
    result = api.create_project(title)
    assert result.status_code == 201
    assert "id" in result.json()
    body_after = api.get_list_project()
    assert body_after.status_code == 200


def test_cteate_project_negativi():
    title = ""
    result = api.create_project(title)
    assert result.status_code == 400


def test_to_change_project_positive():
    title = "NewTest"
    result = api.create_project(title)
    assert result.status_code == 201
    id_project = result.json()["id"]
    result_change = api.to_change_project("Test", id_project)
    id_new = result_change.json()["id"]
    assert result_change.status_code == 200
    result_get = api.get_by_id(id_new)
    assert result_get.status_code == 200
    assert result_get.json()["title"] == "Test"


def test_to_change_project_negative():
    title = "OneTest"
    api.create_project(title)
    id_project = ""
    result_new = api.to_change_project("TwoTest", id_project)
    assert result_new.status_code == 400