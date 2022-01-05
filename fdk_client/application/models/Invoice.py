"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Invoice(BaseSchema):
    # Order swagger.json

    
    updated_date = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    
    label_url = fields.Str(required=False)
    

