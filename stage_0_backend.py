from flask import Flask, Response
from datetime import datetime
import pytz
import json
from collections import OrderedDict

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_info():
    response = OrderedDict([
        ("email", "emmyprime2015@gmail.com"),
        ("current_datetime", datetime.now(pytz.UTC).isoformat()),
        ("github_url", "https://github.com/Emmalywebcreator/")
    ])
    
    # Use json.dumps() to manually serialize and set Content-Type
    return Response(json.dumps(response), mimetype="application/json"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
