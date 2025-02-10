from fastapi import FastAPI

from conversor_moedas_fast_api.routers import v1_routers


def create_app() -> FastAPI:
    app = FastAPI(
        title='Conversor De Moedas',
        version='0.1.0',
        description='API para Converter Moedas',
    )
    app.include_router(v1_routers)

    return app


app = create_app()
