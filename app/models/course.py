from sqlalchemy import String, Integer, Float, Boolean, Text
from sqlalchemy.orm import Mapped,mapped_column

from app.database import Base 

class Course(Base):
    __tablename__ = "courses"
    id:Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        index = True
    )

    name:Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    description:Mapped[str | None] = mapped_column(
        Text,
        nullable=False
    )

    fees:Mapped[float] = mapped_column(
        Float,
        nullable = False
    )

    duration:Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    is_active:Mapped[bool] = mapped_column(
        Boolean,
        default = True
    )
    