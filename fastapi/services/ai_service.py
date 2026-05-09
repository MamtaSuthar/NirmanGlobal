# fastapi/services/ai_service.py
from fastapi.models.project_models import DesignRequest, StyleRecommendation

def get_style_recommendations(request: DesignRequest):
    # Placeholder logic, can call AI model here
    sample_styles = [
        StyleRecommendation(
            style_name="Modern Minimalist",
            description="Clean lines, neutral colors, minimal furniture",
            images=["/static/styles/modern1.jpg", "/static/styles/modern2.jpg"]
        ),
        StyleRecommendation(
            style_name="Rustic",
            description="Warm tones, wooden furniture, cozy atmosphere",
            images=["/static/styles/rustic1.jpg"]
        )
    ]
    return sample_styles
