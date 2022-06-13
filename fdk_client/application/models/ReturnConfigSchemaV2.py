"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ReturnConfigSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    returnable = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    
    time = fields.Int(required=False)
    

