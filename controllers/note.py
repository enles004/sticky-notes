from flask import Blueprint, request, redirect, url_for, render_template, jsonify

from models.note import Note
from models.user import User

blue_note = Blueprint("note", __name__)


@blue_note.get("/api/note")
def get_note():
    session_id = request.cookies.get('user_id')
    if not session_id:
        return redirect(url_for('auth.regis_u'))

    data = [{"id": note.id,
             "title": note.title,
             "description": note.description,
             "color": note.color,
             "created": note.created}
            for note in Note.get_all_note(user_id=session_id)]

    return jsonify({"status": 200,
                    "message": "Data retrieved successfully",
                    "data": data}), 200


@blue_note.post("/api/note")
def post_note():
    session_id = request.cookies.get('user_id')
    if not session_id:
        return redirect(url_for('auth.regis_u'))
    payload = request.get_json()
    title = payload["title"]
    description = payload["description"]
    color = payload["color"]
    result = Note.create_note(session_id, title, description, color)

    data = [{"id": result,
            "title": title,
            "description": description,
            "color": color}]

    return jsonify({"data": data,
                    "message": "Note created successfully!",
                    "status": "201"
                    }), 201


@blue_note.patch("/note/<int:id>")
def patch_note(id):
    session_id = request.cookies.get('user_id')
    if not session_id:
        return redirect(url_for('auth.regis_u'))
    note = Note.get_one_note(session_id=session_id, note_id=int(id))
    if not note:
        return {'message': "not found"}, 404
    payload = request.get_json()
    title = payload["title"]
    description = payload["description"]
    Note.update_note(note_id=id, title=title, description=description)
    return {"message": "updated"}, 200


@blue_note.delete("/note/<int:id>")
def delete_note(id):
    session_id = request.cookies.get('user_id')
    if not session_id:
        return redirect(url_for('auth.regis_u'))
    note = Note.get_one_note(session_id=session_id, note_id=int(id))
    if not note:
        return {'message': "not found"}, 404
    Note.delete_note(note_id=id)
    return {"message": "deleted"}, 200
