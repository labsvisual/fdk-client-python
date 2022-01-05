"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class DefaultCurrency(BaseSchema):
    # Configuration swagger.json

    
    ref = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

