from fastapi import APIRouter


router = APIRouter(prefix="/user", tags=["User"])


@router.get("/")
async def get_user():
    pass


@router.post("/")
async def create_user():
    pass


@router.delete("/")
async def delete_user():
    pass


@router.patch("/")
async def partial_update_user():
    pass


@router.put("/")
async def ful_update_user():
    pass
