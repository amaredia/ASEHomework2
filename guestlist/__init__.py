from flask import Flask
from guestlist.main.controllers import main
from guestlist.admin.controllers import admin

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')
