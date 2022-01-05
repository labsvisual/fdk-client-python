"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DeletehCardRequest(BaseSchema):
    # Payment swagger.json

    
    card_id = fields.Str(required=False)
    

