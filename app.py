from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/test")
def test():
    return jsonify({"status": "ok"})
@app.route("/api/stations")
def stations():
    return jsonify([
        {"name": "Station A", "bikes": 5, "stands": 10},
        {"name": "Station B", "bikes": 0, "stands": 20}
    ])

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)