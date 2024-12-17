import time
import uuid

from flask import Blueprint, request, make_response, render_template, redirect, url_for

from models.user import User

blue_user = Blueprint('auth', __name__)


@blue_user.get("/")
def dashboard():
    return render_template("index.html"), 200


@blue_user.get("/regis_cookie")
def regis_u():
    if request.cookies.get('user_id'):
        return redirect(url_for('note.get_note'))
    user_id = str(uuid.uuid4()) + str(int(time.time() * 1000))
    User.create_user(user_id)
    response = make_response(redirect(url_for('note.get_note')))
    response.set_cookie('user_id', value=user_id, max_age=10 * 365 * 24 * 60 * 60)
    return response, 200


@blue_user.get("/get_cookie")
def get_cookie():
    return {"data": request.cookies.get('user_id')}, 200


@blue_user.delete("/cookie")
def delete_cookie():
    session_id = request.cookies.get('user_id')
    User.delete_user(session_id)
    response = make_response({"message": "cookie deleted"})
    response.delete_cookie('user_id')
    return response, 200
