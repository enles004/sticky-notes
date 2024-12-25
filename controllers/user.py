import time
import uuid

from flask import Blueprint, request, make_response, redirect, url_for, jsonify

from models.user import User

blue_user = Blueprint('auth', __name__)


@blue_user.post("/api/cookie")
def regis_u():
    if request.cookies.get('user_id'):
        return redirect(url_for('note.get_note'))
    user_id = str(uuid.uuid4()) + str(int(time.time() * 1000))
    User.create_user(user_id)
    response = make_response(jsonify({"status": 201, "message": "User registered successfully", "user_id": user_id}), 201)
    response.set_cookie('user_id', value=user_id, max_age=10 * 365 * 24 * 60 * 60)
    return response


@blue_user.get("/api/cookie")
def get_cookie():
    return {"data": [{"user_id": request.cookies.get('user_id')}],
            "message": "User retrieved successfully!!",
            "status": 200}, 200


@blue_user.delete("/api/cookie")
def delete_cookie():
    session_id = request.cookies.get('user_id')
    User.delete_user(session_id)
    response = make_response(jsonify({"message": "cookie deleted", "status": 200}))
    response.delete_cookie('user_id')
    return response, 200


@blue_user.put("/api/cookie")
def put_not_allowed():
    return jsonify({"message": "PUT Method Not Allowed",
                    "status": "405"}), 405


@blue_user.patch("/api/cookie")
def patch_not_allowed():
    return jsonify({"message": "PATCH Method Not Allowed",
                    "status": "405"}), 405
