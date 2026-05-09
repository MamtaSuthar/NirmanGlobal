# fastapi/models/project_models.py
from pydantic import BaseModel
from typing import List, Optional

class StyleRecommendation(BaseModel):
    style_name: str
    description: str
    images: List[str]  # URLs to images

class DesignRequest(BaseModel):
    room_type: str
    budget: Optional[float] = None
    preferences: Optional[List[str]] = None
