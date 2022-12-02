import requests


def post():
    with requests.post("http://127.0.0.1:5000/post", json={
        "x": 5
    }) as res:
        print(res.text)


def delete():
    with requests.delete("http://127.0.0.1:5000/delete/50080997685686") as res:
        print(res.text)


def get():
    with requests.get("http://127.0.0.1:5000/async") as res:
        print(res.text)


get()
