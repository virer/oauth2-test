from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    print(request.headers)
    user = request.headers.get('X-Forwarded-User')
    return "<p>Hello {0}, welcome !</p><hr>\n<pre>{1}</pre>".format(user, request.headers)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")