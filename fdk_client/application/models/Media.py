"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Meta import Meta






class Media(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Nested(Meta, required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    

