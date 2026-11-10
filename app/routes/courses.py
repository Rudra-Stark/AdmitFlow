from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.course import Course
from app.schemas.course import (
    CourseCreate,
    CourseUpdate,
    CourseResponse
)

router = APIRouter(
    prefix = "/courses",
    tags = ["Courses"]
)

# --------Create - Add a course---------------

@router.post("/",
             response_model=CourseResponse,
             status_code = status.HTTP_201_CREATED
             )
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):
    new_course = Course(**course.model_dump())

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course

#----------Read - Get all courses--------------

@router.get("/",response_model = list[CourseResponse])
def get_courses(
    db: Session = Depends(get_db)
):
    return db.query(Course).all()

#----------Read - Get one course----------------

@router.get("/{course_id}", response_model = CourseResponse)
def get_course(
    course_id:int,
    db: Session = Depends(get_db)
):
    course = db.get(Course, Course_id)

    if course is None:
        raise HTTPException(
            status_code = 404,
            detail = "Course not found"
        )
    return course

#----------Update - Modify a Course---------------
@router.patch("/{course_id}", response_model = CourseResponse)
def update_course(
    course_id:int,
    course_data:CourseUpdate,
    db:Session = Depends(get_db)
):
    course = db.get(Course, course_id)

    if course is None:
        raise HTTPException(
            status_code = 404,
            detail = "Course not found"
        )

    updates = course_data.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)
    return course

#------------Delete - Remove a Course----------------

@router.delete(
    "/{course_id}",
    status_code = status.HTTP_204_NO_CONTENT
)
def delete_course(
    course_id:int,
    db:Session = Depends(get_db)
):
    course = db.get(Course, course_id)

    if course is None:
        raise HTTPException(
            status_code = 404,
            detail = "Course not found"
        )
    db.delete(course)
    db.commit()
