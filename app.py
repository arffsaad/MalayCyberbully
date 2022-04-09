import tf
from flask import Flask, request, jsonify

# main
app = Flask(__name__) # define app name

# POST to "check" api endpoint

@app.post("/check")
def check():
    req = request.get_json()
    text = []
    text.append(req['captions'])
    final = tf.cyb(text)
    return final, 200
