from __future__ import annotations

from tortoise import Model, fields

from app.tortoise_models.base_model import BaseModel


class MeetingModel(BaseModel, Model):
    url_code = fields.CharField(max_length=255, unique=True)

    class Meta:
        table = "meeting"

    @classmethod
    async def create_meeting(cls, url_code: str) -> "MeetingModel":
        return await cls.create(url_code=url_code)

    @classmethod
    async def get_by_url_code(cls, url_code: str) -> "MeetingModel | None":
        return await cls.filter(url_code=url_code).get_or_none()
