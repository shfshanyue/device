from flask import Blueprint, render_template, request, jsonify

device = Blueprint('device', __name__)

from .model import User
from . import db

@device.route('/')
def show():
    return render_template('analysis.html')


@device.route('/anaysis', methods=['POST'])
def anaysis():
    number = request.form['number']
    file = request.files['file']
    if file.headers['Content-Type'] != 'text/plain':
        return jsonify({"success": 0})
    data = map(lambda x: int(x), file.stream.read().split())
    everage = sum(data) / len(data)
    number = int(request.form['number'])
    warn = everage > number
    return jsonify({"success": 1, "warn": warn, "everage": everage, "number": number})
