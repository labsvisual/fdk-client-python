"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ActionPageParams(BaseSchema):
    # Rewards swagger.json

    
    slug = fields.List(fields.Str(required=False), required=False)
    

