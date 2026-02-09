from pydantic import BaseModel, UUID4
from typing import Optional, List

class WeaveBase(BaseModel):
    name: str
    description: str
    min_ar: float
    max_ar: float
    picture: str
    tutorial_link: str
    multi_ringsize: bool
    
# class WeaveCreate(WeaveBase):
