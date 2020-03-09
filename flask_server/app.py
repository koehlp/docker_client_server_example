from flask import Flask, render_template, request, jsonify, Markup,flash
import os
import random
import time
import numpy as np
import cv2
import json

import socket


def print_ip_adress():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)


app = Flask(__name__)
app.secret_key = "super secret key"



@app.route("/")
def index():
    return render_template('index.html')

@app.route('/videoframe', methods=['POST'])
def upload():

    #videoframe = request.files.get('videoframe', '')

    file = request.files['videoframe'].read()  ## byte file
    framename = request.files['framename'].read().decode("utf-8")   ## byte file
    npimg = np.frombuffer(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    print(img.shape)

    response = app.response_class(
        response=json.dumps({'img.shape': img.shape, 'framename' : framename}),
        status=200,
        mimetype='application/json'
    )

    return response


if __name__ == "__main__":
    print_ip_adress()

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8888)))
