from fastapi import APIRouter

from .v1.converter_router import router as converter_router

v1_routers = APIRouter(prefix='/conversor_moedas_fast_api/v1')

v1_routers.include_router(
    converter_router, prefix='/converter', tags=['converter']
)
