"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class LocationDefaultCurrency(BaseSchema):
    # Common swagger.json

    
    name = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

