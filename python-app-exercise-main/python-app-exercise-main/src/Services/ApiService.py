from sys import stderr
import json, csv, datetime, requests

TODOSURL = "https://jsonplaceholder.typicode.com/todos/"
PATH = 'storage/'
dt = datetime.datetime.fromtimestamp(0)

class ApiService:
    def __init__(self):
        pass

    def receive_todos_from_url(self,urltodos):
        response = requests.get(urltodos)
        data = response.text
        return json.loads(data)

    def read_info_from_url_to_csv(self, info_todos):
        array_len = range(len(info_todos))
        fieldnames = []
        for key in info_todos[0].keys():
            fieldnames.append(key)
        for x in array_len:
           with open(PATH + datetime.date.today().strftime("%Y_%m_%d_") + str(info_todos[x]['id']) + ".csv", "w", encoding='UTF8', newline='') as csvfile:
               writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
               writer.writeheader()
               writer.writerow(info_todos[x])

    def run(self):
        print('Running ApiService', file=stderr)
        json_data = self.receive_todos_from_url(TODOSURL)
        self.read_info_from_url_to_csv(json_data)
            # TODO: follow README.md instructions