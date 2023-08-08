from flask import Flask, redirect, url_for, render_template

# Our Flask app object
app = Flask(__name__, template_folder='../templates',
            static_folder='../static')


@app.route('/')
@app.route('/home')
def index():
    """Our default routes of '/' and '/index'

    Return: The content we want to display to a user
    """

    return render_template('home.html')

@app.route('/histogram')
def histo():
    return render_template('histograms.html', title="alternate histogram title")

@app.route('/start')
def star():
    return render_template('start.html')

@app.route('/categorical')
def categ():
    return render_template('categorical.html')

@app.route('/nominal')
def nom():
    return render_template('nominal.html')

@app.route('/ordinal')
def ord():
    return render_template('ordinal.html')

@app.route('/visuals')
def visual():
    return render_template('visuals.html')

@app.route('/<path:path>')
def catch_all(path):
    """A special route that catches all other requests

    Note: Let this be your last route. Priority is defined
    by order, so placing this above other functions will
    cause catch_all() to override then.

    Return: A redirect to our index route
    """

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    app.run()
