from aiogram import Router
from . import admin

router = Router()

router.include_routers(
    admin.router,
)