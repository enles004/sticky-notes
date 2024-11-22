from sqlalchemy import Column, String, Integer, DateTime, func, text
from sqlalchemy.orm import relationship, joinedload

from database import Base
from database import connection


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    session_id = Column(String(60), nullable=False)
    created = Column(DateTime, default=func.now())
    notes = relationship("Note", backref="user", cascade="all, delete", passive_deletes=True, lazy="joined")

    @classmethod
    def get_user(cls, session_id):
        try:
            db = connection()
            data = db.query(User).options(joinedload(User.notes)).filter(User.session_id == session_id).first()
            db.remove()
            return data
        except Exception as e:
            raise Exception(f'err: {e}')

    @classmethod
    def create_user(cls, session_id):
        try:
            db = connection()
            sql = text("INSERT INTO users (session_id) VALUES (:session_id)")
            db.execute(sql, {"session_id": session_id})
            db.commit()
            db.remove()
        except Exception as e:
            raise Exception(f"An error occurred while inserting user with session_id {session_id}: {str(e)}")

    @classmethod
    def delete_user(cls, session_id):
        try:
            db = connection()
            db.query(User).filter(User.session_id == session_id).delete()
            db.commit()
        except Exception as e:
            raise Exception(f"An error occurred while deleting user with session_id {session_id}: {str(e)}")
