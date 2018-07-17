from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('hello_form.html')

@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    # template = jinja_env.get_template('hello_greeting.html')
    return render_template('hello_greeting.html', name=first_name)


@app.route("/validate-time")  # GET by default
def display_time_form():
    return render_template('time_form.html')


def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


@app.route('/validate-time', methods=['POST'])
def validate_time():
    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range (0-23)'
            hours = ''
    
    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value our of range (0-59)'
            minutes = ''

    if not minutes_error and not hours_error:
        time = str(hours) + ':' +str(minutes)
        return redirect('/valid-time?time={}'.format(time))
    else:
        return render_template('time_form.html', hours_error=hours_error, 
            minutes_error=minutes_error,
            hours=hours,
            minutes=minutes)


@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return render_template('valid_time.html', time=time)


tasks = []

@app.route('/todos', methods=['POST', 'GET'])
def todos():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('todos.html', title='TODOs', tasks=tasks)


app.run()