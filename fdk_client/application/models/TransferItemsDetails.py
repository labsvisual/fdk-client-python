"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class TransferItemsDetails(BaseSchema):
    # Payment swagger.json

    
    display_name = fields.Str(required=False)
    
    logo_large = fields.Str(required=False)
    
    logo_small = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    id = fields.Int(required=False)
    

