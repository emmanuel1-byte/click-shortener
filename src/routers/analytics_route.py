from fastapi import APIRouter

analytics = APIRouter(prefix="/api/analytics")


@analytics.get("/{url_id}", tags=["Analytics"])
def get_url_analytics():
    pass
