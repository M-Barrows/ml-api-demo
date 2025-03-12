from fastapi import FastAPI, Request
from app.routes import basic, model_router
import joblib

def create_app() -> FastAPI:
    app = FastAPI()

    model = joblib.load("./model/model.joblib")

    @app.middleware("http")
    async def add_model_to_request(request:Request, call_next):
        request.state.model = model
        response = await call_next(request)
        return response
    app.include_router(basic)
    app.include_router(model_router)
    return app
