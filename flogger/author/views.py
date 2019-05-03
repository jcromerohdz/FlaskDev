from flask import Blueprint, render_template

from author.models import Author
from author.form import RegisterForm

author_app = Blueprint('author_app', __name__)

@author_app.route('/register', methods=['GET', 'POST'])
def register():
    # return 'Author registration'
    from = RegisterForm()
    return render_template('author/register.html', form=form)