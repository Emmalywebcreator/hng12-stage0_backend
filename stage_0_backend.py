from flask import Flask, Response
import pytz
from datetime import datetime
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_info():
    response = {
        "email": "emmyprime@gmail.com",
        "current_datetime": datetime.now(pytz.UTC).isoformat(),
        "github_url": "https://github.com/Emmalywebcreator"
    }
    
    return Response(
        json.dumps(response, sort_keys=False),
        mimetype="application/json"
    ), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)