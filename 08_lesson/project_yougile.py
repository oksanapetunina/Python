import requests

TOKEN = ""


class ProjectsApi:

    def __init__(self, url):
        self.url = url

    # список проектов
    def get_list_project(self):
        my_headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content - Type": "application / json"
        }
        response = requests.get(self.url+'projects', headers=my_headers)
        return response

    # создание проекта
    def create_project(self, title):
        id_pass = {
            "title": title
        }
        my_headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content - Type": "application / json"
        }
        response = requests.post(self.url+'projects',
                                 json=id_pass, headers=my_headers)
        return response

    # получить по id
    def get_by_id(self, id):
        my_headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content - Type": "application / json"
        }
        response = requests.get(self.url + 'projects/' + id,
                                headers=my_headers)
        return response

    # изменить название проекта по id
    def to_change_project(self, new_title, id):
        body = {
            "title": new_title
        }
        my_headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content - Type": "application / json"
        }
        response = requests.put(self.url + 'projects/' + id, json=body,
                                headers=my_headers)
        return response