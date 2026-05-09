# fastapi/services/design_service.py
from fastapi.models.project_models import DesignRequest

def generate_design_preview(request: DesignRequest):
    """
    Here you can integrate AI image generation for room design
    For now, return a placeholder URL
    """
    return "/static/previews/sample_room.jpg"
