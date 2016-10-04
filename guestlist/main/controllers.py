from flask import Blueprint
from flask import request
from flask import render_template
import fileReadWrite

main = Blueprint('main', __name__)


@main.route('/')
def form_home():
    return render_template("name.html")

@main.route('/', methods=['POST'])
def new_guest():
    newguest = request.form['name']
    fileReadWrite.addName(newguest, "guestlist.txt")
    guestlist = fileReadWrite.listOfNames("guestlist.txt")
    return render_template("newguest.html", guests=guestlist)
