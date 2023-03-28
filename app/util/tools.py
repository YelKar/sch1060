import json
from os import listdir

from flask import url_for, request

from app.util.constants import docs_path
from app import app, database


@app.route(
    '/get_url_for/',
    defaults={'endpoint_': None},
    methods=["POST", "GET"]
)
@app.route(
    "/get_url_for/<string:endpoint_>",
    methods=["POST", "GET"]
)
def get_url_for(endpoint_=None):
    args = json.loads(request.data.decode())
    return url_for(endpoint_ or "index", **args)


@app.add_template_global
def get_documents():
    return list(
        ".".join(name.split(".")[:-1])
        for name
        in listdir(docs_path)
    )


@app.add_template_global
def db(*bool_filters, **filters):
    query = database.Student.query
    if bool_filters:
        return query.filter(*bool_filters)
    elif filters:
        return query.filter_by(**filters)
    return query
