# fastapi/routes/design_routes.py
from fastapi import APIRouter
from fastapi.models.project_models import DesignRequest
from fastapi.services.design_service import generate_design_preview

router = APIRouter()

@router.post("/preview")
def design_preview(request: DesignRequest):
    """
    Generate a design preview image for a room
    """
    image_url = generate_design_preview(request)
    return {"status": "success", "image_url": image_url}
