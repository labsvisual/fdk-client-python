"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ActionQuery import ActionQuery


class ProductAction(BaseSchema):
    # Cart swagger.json

    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    query = fields.Nested(ActionQuery, required=False)
    

