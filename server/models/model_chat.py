"""chats database model"""
from .db import db


class ChatModel(db.Model):
    """model of chats to retrieve user chat list"""
    __tablename__ = "chats"

    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, foreign_key="users.id")
    user2_id = db.Column(db.Integer, foreign_key="users.id")
    
    def json(self) -> dict:
        """return jsonify chat settings"""
        return {
            "id": self.id,
            "user1_id": self.user1_id,
            "user2_id": self.user2_id
        }
    
    @classmethod
    def has_users_chat(cls, user1_id: int, user2_id: int) -> bool:
        """
        return True if users (user1, user2) has chat

        :user1_id: ID of user1 to retrieve
        :user2_id: ID of user2 to retrieve
        """

        query = cls.query.filter(
            cls.user1_id == min(user1_id, user2_id),
            cls.user2_id == max(user1_id, user2_id)
        ).first_or_404()

        return bool(query)
