"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EntityMeta(BaseSchema):
    # Feedback swagger.json

    
    order_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

