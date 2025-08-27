from aiogram import Router
from . import group
from . import admin

router = Router()

router.include_routers(
    admin.router,
    group.router,
)