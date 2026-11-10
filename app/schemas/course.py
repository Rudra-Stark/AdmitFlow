from pydantic import BaseModel, Field, ConfigDict

class CourseBase(BaseModel):
    name:str = Field(min_length=2, max_length=100)
    description:str | None = None 
    fees:float = Field(ge=0)
    duration:int = Field(gt=0)
    is_active:bool = True

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    name:str | None = Field(default=None, min_length=2)
    description:str | None = None 
    fees:float | None = Field(default = None, ge=0)
    duration:int | None = Field(default = None, gt = 0)
    is_active:bool | None = None

class CourseResponse(CourseBase):
    id: int 

    model_config = ConfigDict(from_attributes=True)

