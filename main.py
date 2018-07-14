from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="POST">
            <label for="first_name">First Name:</label>
            <input id="first_name" type="text" name="first_name" />
            <input type="submit" />
        </form>
    </body>
</<html>
"""

@app.route("/")
def index():
    return form

# GET by default
# @app.route('/hello')
# def hello():
#     first_name = request.args.get('first_name')
#     return '<h2>Hello, {}!</h2>'.format(first_name)

# Need to specify POST
@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h2>Hello, {}!</h2>'.format(first_name)

app.run()