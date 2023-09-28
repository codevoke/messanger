"""primary model - messages"""
from datetime import datetime

from .db import db


class MessageModel(db.Model):
    """Model of messanges to create, keep, modify and delete them"""
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(2000))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    chat_id = db.Column(db.Integer, foreign_key="chats.id")


    def json(self) -> dict:
        """return json view of retrieved message"""
        return {
             "id": self.id,
             "message": self.message,
             "timestamp": self.timestamp,
             "chat_id": self.chat_id
         }


    def put(self, new_message:str) -> None:
        """mofidy message text"""
        self.message = new_message + " (ред.)"
