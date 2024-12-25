from sqlalchemy import update, delete, text, Column, String, Integer, func, DateTime, Text, ForeignKey

from database import Base
from database import connection
from models.user import User


class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String(255))
    description = Column(Text)
    color = Column(String(255))
    created = Column(DateTime, default=func.now())

    @classmethod
    def get_one_note(cls, session_id, note_id):
        try:
            db = connection()
            sql = text("SELECT * "
                       "FROM notes n "
                       "JOIN users u on u.id = n.user_id "
                       "WHERE u.session_id = :session_id "
                       "AND n.id = :note_id")
            data = db.execute(sql, {"session_id": session_id, "note_id": note_id}).fetchone()
            db.commit()
            db.remove()
            return data
        except Exception as e:
            raise Exception(f'err{e}')

    @classmethod
    def get_all_note(cls, user_id):
        try:
            db = connection()
            check_user = db.query(User).filter(User.session_id == user_id).first()
            if check_user:
                data = db.query(Note).filter(Note.user_id == check_user.id).order_by(Note.created.asc()).all()
                db.remove()
                return data
            raise Exception("User is not valid")
        except Exception as e:
            raise Exception(f"err: {e}")

    @classmethod
    def create_note(cls, user_id, title, description, color):
        try:
            db = connection()
            check_user = db.query(User).filter(User.session_id == user_id).first()
            if check_user:
                sql = text(
                    "INSERT INTO notes (user_id, title, description, color) VALUES (:user_id, :title, :description, :color) RETURNING id, created;")
                result = db.execute(sql, {"user_id": check_user.id, "title": title, "description": description,
                                          "color": color})
                note = result.fetchone()
                db.commit()
                db.remove()
                return note
            raise Exception("User is not valid")
        except Exception as e:
            raise Exception(f"err: {e}")

    @classmethod
    def update_note(cls, note_id, title, description):
        try:
            db = connection()
            stmt = update(Note).where(Note.id == note_id).values(title=title, description=description)
            db.execute(stmt)
            db.commit()
            db.remove()
        except Exception as e:
            raise Exception(f'err: {e}')

    @classmethod
    def delete_note(cls, note_id):
        try:
            db = connection()
            stmt = delete(Note).where(Note.id == note_id)
            db.execute(stmt)
            db.commit()
            db.remove()
        except Exception as e:
            raise Exception(f'err: {e}')
