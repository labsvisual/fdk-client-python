"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Card import Card






class ListCardsResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Nested(Card, required=False), required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    

