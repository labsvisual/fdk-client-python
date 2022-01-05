"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ReturnConfig(BaseSchema):
    # Catalog swagger.json

    
    returnable = fields.Boolean(required=False)
    
    time = fields.Int(required=False)
    
    unit = fields.Str(required=False)
    

