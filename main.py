from flask import Flask, render_template, request, jsonify
from core.weather import weather

app = Flask(__name__)

@app.route("/<appid>")
def forecast(appid: str):
    list_units = ["standard", "metric", "imperial"]
    q = request.args.get('q')
    units = request.args.get('units')
    if units not in list_units:
        units = "standard"

    results = weather(q, appid, units)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)