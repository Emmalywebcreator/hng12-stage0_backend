from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/",methods=["GET"])
def get_info():
    response = {
        "email": "emmyprime2015@gmail.com",
        "current_date": datetime.now(pytz.UTC).isoformat(),
        "github_url": "https://github.com/Emmalywebcreator/"
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    