from flask import send_file
from app import app


@app.route('/get/scripts/<path:filename>')
def scripts(filename):
    return send_file(f"static/scripts/{filename}")


@app.route('/get/styles/<path:filename>')
def styles(filename):
    return send_file(f"static/styles/{filename}")


@app.route('/fonts/<path:filename>')
def fonts(filename):
    return send_file(f"static/fonts/{filename}")
