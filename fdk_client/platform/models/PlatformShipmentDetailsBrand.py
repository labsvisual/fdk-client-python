"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class PlatformShipmentDetailsBrand(BaseSchema):
    # Order swagger.json

    
    credit_note_allowed = fields.Boolean(required=False)
    
    brand_name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    is_virtual_invoice = fields.Boolean(required=False)
    
    created_on = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    

