from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    city: Mapped[str] = mapped_column(String(100), nullable=True)
    abbreviation: Mapped[str | None] = mapped_column(String(3), nullable=True)
    api_web_nhle_abr: Mapped[str | None] = mapped_column(String(3), index=True, nullable=True)
    api_nhle_id: Mapped[int | None] = mapped_column(unique=True, index=True, nullable=True)
    conference: Mapped[str] = mapped_column(String(50), nullable=True)
    division: Mapped[str] = mapped_column(String(50), nullable=True)
