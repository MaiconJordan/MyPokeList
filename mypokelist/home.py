from flask import Blueprint

b_home = Blueprint('/home', __name__)


@b_home.route('/')
def get_home():
    return '<h1>joga a pagina aqui</h1>'
