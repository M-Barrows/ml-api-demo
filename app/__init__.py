from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI()

    from app.routes import router
    app.include_router(router)

    return app
