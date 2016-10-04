from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def form_home():
    return render_template("name.html")

@app.route('/newguest.html', methods=['POST'])
def new_guest():
    newguest = request.form['name']
    #add new guest using angel's function
    #populate guestlist using angel's function
    guestlist = ['laura\n','angel\n','howon\n']
    return render_template("newguest.html", guests=guestlist)

@app.route('/guestlist.html')
def guest_list():
    #populate guestlist using angel's function
    return render_template("guestlist.html", guests=guestlist)

if __name__ == '__main__':
    app.run()

