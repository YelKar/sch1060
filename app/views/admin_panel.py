import json
import os

from flask import render_template, request

from app import app

formats = {
    ".py": "python",
    ".js": "javascript",
    ".css": "css",
    ".html": "html"
}


@app.route('/listdir')
def listdir():
    route = request.args.get("route") or "."
    file_text = ""
    file_resolution = os.path.splitext(route)[-1]
    if file_resolution:
        with open(route, "r", encoding="utf-8") as file:
            file_text = file.read()
    return render_template(
        "listdir.html",
        route=route,
        spl_route=route.split("/"),
        listdir=os.listdir(route) if not file_resolution else [],
        file_text=file_text,
        file_format="" if not file_resolution else formats.get(file_resolution),
        is_file=lambda name="": os.path.isfile(os.path.join(route, name))
    )


@app.route('/save_file', methods=['POST'])
def save_file():
    file = json.loads(request.data)
    filename = "./" + "/".join(
        (
            *map(
                lambda x: x.strip(),
                file["file"].split("/")
            ),
        )[1:]
    )
    content = file["content"]
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    return "OK"
