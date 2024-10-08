from fastapi import APIRouter
from .user_router import router as user_router
from .message_router import router as message_router
from .like_router import router as like_router
from .feed_router import router as feed_router

router = APIRouter()

router.include_router(user_router, prefix="")
router.include_router(message_router, prefix="")
router.include_router(feed_router, prefix="")
router.include_router(like_router, prefix="")