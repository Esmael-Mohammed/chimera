import uuid
from sqlalchemy import Column, String, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector
from .db import Base

class Trend(Base):
    __tablename__ = "trends"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    source = Column(String, nullable=False)
    keyword = Column(String, nullable=False)
    score = Column(Float, nullable=False)
    embedding = Column(Vector(1536))
    ingested_at = Column(DateTime(timezone=True), server_default=func.now())


class ContentMetadata(Base):
    __tablename__ = "content_metadata"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    trend_id = Column(UUID(as_uuid=True), ForeignKey("trends.id"))
    platform = Column(String, nullable=False)
    content_url = Column(String, nullable=False)
    caption = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class AgentState(Base):
    __tablename__ = "agent_state"

    agent_id = Column(String, primary_key=True)
    last_run = Column(DateTime(timezone=True))
    checkpoint = Column(JSONB)
    status = Column(String)
