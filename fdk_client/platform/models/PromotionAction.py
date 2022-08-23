"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PromotionAction(BaseSchema):
    # Cart swagger.json

    
    action_type = fields.Str(required=False)
    
    action_date = fields.Str(required=False)
    

