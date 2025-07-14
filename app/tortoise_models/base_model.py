from tortoise import fields


class BaseModel:
    id = fields.BigIntField(pk=True)
    create_at = fields.DatetimeField(auto_now_add=True)
