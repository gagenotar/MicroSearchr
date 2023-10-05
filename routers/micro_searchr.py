from fastapi import APIRouter, Depends
from schemas.micro_searchr import MicroSearchrResponse
from services.micro_searchr import MicroSearchrService, get_micro_searchr_service

router = APIRouter()


@router.get("/search", response_model=MicroSearchrResponse)
def search_query(
        q: str,
        micro_searchr_service: MicroSearchrService = Depends(get_micro_searchr_service)
) -> MicroSearchrResponse:
    return NotImplementedError
