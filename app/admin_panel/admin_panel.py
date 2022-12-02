import os

from flask import render_template, request

from app import app


@app.route('/listdir')
def listdir():
    formats = {
        ".py": "python",
        ".js": "javascript",
        ".css": "css",
        ".html": "html"
    }
    route = request.args.get("route")
    file_text = ""
    file_resolution = os.path.splitext(route)[-1]
    if file_resolution:
        with open(route) as file:
            file_text = file.read()
    return render_template(
        "listdir.html",
        route=route,
        spl_route=route.split("/"),
        listdir=os.listdir(route) if not file_resolution else [],
        file_text=file_text,
        file_format="" if not file_resolution else formats.get(file_resolution)
    )
