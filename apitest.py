import json, requests

params = {
    "id" : "1427692106",
    "fav_repository" : "https://github.com/prglee6274/MyRepository",
    "nick_name" : "opensource",
    "type" : "telegram",
    "branch" : "master"
}

content = requests.get("http://margarets.pythonanywhere.com/api/", params=params)


content = json.loads(content.content)

content = str(content)

content2 = content[1:len(content)-1]

content2 = json.loads(content.content)
tmp = content2.get("commit").get("author").get("name")

print(content2)