from sqlalchemy import Integer, String, DateTime, func, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime

from database.connection import Base

class Conversations(Base):
  __tablename__ = "conversations"

  id: Mapped[int] = mapped_column(Integer, primary_key=True)

  server_id: Mapped[int] = mapped_column(String, index=True)
  channel_id: Mapped[int] = mapped_column(Integer, index=True)

  created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

class Messages(Base):
  __tablename__ = "messages"

  id: Mapped[int] = mapped_column(primary_key=True)
  
  conversation_id: Mapped[int] = mapped_column(ForeignKey("conversations.id"), index=True)

  role: Mapped[str] = mapped_column(String)
  content: Mapped[str | None] = mapped_column(String, nullable=True)

  tool_calls: Mapped[list | None] = mapped_column(JSON, nullable=True)
  tool_call_id: Mapped[str | None] = mapped_column(String, nullable=True)

  created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
