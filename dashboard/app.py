from flask import Flask, render_template
import json

app = Flask(__name__)

ALERT_FILE = "../alerts.json"

def load_alerts():
    alerts = []
    try:
        with open(ALERT_FILE, "r") as f:
            for line in f:
                alerts.append(json.loads(line))
    except FileNotFoundError:
        pass
    return alerts

@app.route("/")
def index():
    alerts = load_alerts()
    high = len([a for a in alerts if a["severity"] == "High"])
    medium = len([a for a in alerts if a["severity"] == "Medium"])
    low = len([a for a in alerts if a["severity"] == "Low"])

    return render_template(
        "index.html",
        total=len(alerts),
        high=high,
        medium=medium,
        low=low,
        alerts=alerts[-10:]
    )

if __name__ == "__main__":
    app.run(debug=True)
