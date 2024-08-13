from app.handlers.start import router_start
from app.handlers.name import router_name


def setup_routes(dp):
    dp.include_router(router_start)
    dp.include_router(router_name)


# ... other imports ...