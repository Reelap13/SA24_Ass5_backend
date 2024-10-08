from sqlalchemy import Table, Column, Integer, String, Text, ForeignKey, MetaData
from database import metadata

users = Table(
    "users",
    metadata,
    Column("username", Text, primary_key=True)
)

messages = Table(
    "messages",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String(400), nullable=False)
)

user_messages = Table(
    "user_messages",
    metadata,
    Column("username", Text, ForeignKey("users.username"), nullable=False), 
    Column("message_id", Integer, ForeignKey("messages.id"), nullable=False)
)

likes = Table(
    "likes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", Text, ForeignKey("users.username"), nullable=False),
    Column("message_id", Integer, ForeignKey("messages.id"), nullable=False)
)