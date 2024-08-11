from app.handlers.handlers_cm import router_cm
from app.handlers.handlers_txt import router_txt


def setup_routes(dp):
    dp.include_router(router_cm)
    dp.include_router(router_txt)