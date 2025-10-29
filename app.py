from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)

reminders = [{"id": 1, "message": "Take a short break", "interval_min": 60}]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/reminders", methods=["GET"])
def get_reminders():
    return jsonify(reminders)

@app.route("/api/reminders", methods=["POST"])
def add_reminder():
    data = request.get_json()
    if not data or "message" not in data or "interval_min" not in data:
        return jsonify({"error": "Invalid payload"}), 400
    new_id = max((r["id"] for r in reminders), default=0) + 1
    r = {
        "id": new_id,
        "message": data["message"],
        "interval_min": int(data["interval_min"])
    }
    reminders.append(r)
    return jsonify(r), 201

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
