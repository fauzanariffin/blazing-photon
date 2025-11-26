from flask import Flask, render_template
from data import get_event_data

app = Flask(__name__)

@app.route('/')
def index():
    data = get_event_data()
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(debug=True)
