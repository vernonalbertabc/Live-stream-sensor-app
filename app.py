# Reference
#https://www.youtube.com/watch?v=e68S9x3Rh_0&ab_channel=soumilshah1995

from flask import Flask, jsonify,request,render_template,make_response
import numpy as np
import time
import json
import random

app = Flask(__name__)

@app.route("/")
def main():
    
    return render_template("index.html")


@app.route("/data",methods=["GET","POST"])
def get():
    data = [time.time()*100,np.sin(time.time())*100 + random.random()*100]
    response = make_response(json.dumps(data))
    response.content_type = "application/json"

    return response

if __name__ == "__main__":
    app.run()


