from flask_login import login_required, logout_user

from flask import Blueprint, redirect, render_template, url_for

from app.models.posts import Post

index_p = Blueprint('index', __name__)


@index_p.route('/')
@login_required
def index():
    posts = Post.query.all()
    return render_template('indexCss.html', post= posts)
