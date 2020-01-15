from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
#    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p><a href="/sida2" title=Síða 2 </a> |Siða2|
    <a href="/sida3" titles=siða 3 </a> |siða3| </p>
    </a></p>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400">
    """ #.format(time=the_time)
@app.route('/sida2')
def page2():
    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <p><a href="/" titles=heimasiða </a>|siða1| 
    <a href="/sida3" titles=siða3 </a> |siða3</p>
    <img src="http://loremflickr.com/600/400">
    """

@app.route('/sida3')
def page3():
    return render_template('man1.html')
if __name__ == '__main__':

    app.run(debug=True, use_reloader=True)