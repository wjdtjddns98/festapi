from datetime import date, timedelta

from pydantic import BaseModel

from app.dtos.frozen_config import FROZEN_CONFIG

MEETING_DATE_MAX_RANGE = timedelta(days=62)


class UpdateMeetingDateRangeRequest(BaseModel):
    model_config = FROZEN_CONFIG

    start_date: date
    end_date: date

    def exceed_max_range(self) -> bool:
        return self.end_date - self.start_date > MEETING_DATE_MAX_RANGE


class UpdateMeetingTitleRequest(BaseModel):
    model_config = FROZEN_CONFIG

    title: str


class UpdateMeetingLocationRequest(BaseModel):
    model_config = FROZEN_CONFIG
    location: str
