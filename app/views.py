from flask import render_template, request, abort

from app import app
from app.logger import logger

files_route = "static/files/{}"
deleted = []

@app.route('/')
def index():
    # logger.sending("qwerty")
    return render_template("index.html")


@app.route('/post', methods=['GET', 'POST'])
def post():
    x = float(request.json["x"])
    result = "{x} ** 2 = {x_x}".format(x=x, x_x=x*x)
    print("Sent {res}".format(res=result))
    return result


@app.route('/delete/<int:num>', methods=["GET", "DELETE"])
def delete(num):
    if num in deleted:
        return abort(404)
    deleted.append(num)
    return "{} deleted".format(num)


@app.route('/async')
async def async_route():
    return "OK"

from app.admin_panel import admin_panel
