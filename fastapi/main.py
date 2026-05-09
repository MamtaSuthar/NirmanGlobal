# fastapi/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routes
from fastapi.routes.ai_routes import router as ai_router
from fastapi.routes.design_routes import router as design_router

app = FastAPI(
    title="Interior AI API",
    description="FastAPI endpoints for interior design suggestions",
    version="1.0.0"
)

# Allow CORS (so your Django front-end can call FastAPI)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(ai_router, prefix="/ai", tags=["AI"])
app.include_router(design_router, prefix="/design", tags=["Design"])

@app.get("/")
def root():
    return {"message": "Welcome to Interior AI API"}
