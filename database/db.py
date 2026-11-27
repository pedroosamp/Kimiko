from database.connection import SessionLocal
from database.models import Messages

def save_message(conversation_id: int, role: str, content: str):
  with SessionLocal() as db:
    message = Messages(
      conversation_id = conversation_id,
      role = role,
      content = content,
    )
    db.add(message)
    db.commit()

    return message.id