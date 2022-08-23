"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .PromotionSchedule import PromotionSchedule


class PromotionPartialUpdate(BaseSchema):
    # Cart swagger.json

    
    archive = fields.Boolean(required=False)
    
    schedule = fields.Nested(PromotionSchedule, required=False)
    

