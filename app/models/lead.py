from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped,mapped_column

from app.database import Base 

class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key = True,
        index = True
    )

    student_name: Mapped[str] = mapped_column(
        String(100),
        nullable = False 
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable = False
    )

    course_id: Mapped[int] = mapped_column(
            Integer,
            ForeignKey("courses.id"),
            nullable = False
        )

    status: Mapped[str] = mapped_column(
            String(30),
            default = "new"
        )
