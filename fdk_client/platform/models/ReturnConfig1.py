"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ReturnConfig1(BaseSchema):
    # Catalog swagger.json

    
    unit = fields.Str(required=False)
    
    time = fields.Int(required=False)
    
    returnable = fields.Boolean(required=False)
    

