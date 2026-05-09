# fastapi/routes/ai_routes.py
from fastapi import APIRouter
from fastapi.models.project_models import DesignRequest, StyleRecommendation
from fastapi.services.ai_service import get_style_recommendations

router = APIRouter()

@router.post("/recommendation")
def recommend_style(request: DesignRequest):
    """
    Get interior design style recommendations
    """
    result = get_style_recommendations(request)
    return {"status": "success", "data": result}
