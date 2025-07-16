import uuid
from typing import Optional

from tortoise.exceptions import DoesNotExist

from app.tortoise_models.meeting import MeetingModel
from app.utils.base62 import Base62


async def service_create_meeting_mysql() -> MeetingModel:
    return await MeetingModel.create_meeting(Base62.encode(uuid.uuid4().int))


async def service_get_meeting_mysql(url_code: str) -> Optional[MeetingModel]:
    try:
        return await MeetingModel.get(url_code=url_code)
    except DoesNotExist:
        return None
