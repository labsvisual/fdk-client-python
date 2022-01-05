"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class GstDetails(BaseSchema):
    # Order swagger.json

    
    brand_calculated_amount = fields.Float(required=False)
    
    gst_fee = fields.Str(required=False)
    
    gst_tag = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    value_of_good = fields.Float(required=False)
    
    gst_tax_percentage = fields.Float(required=False)
    
    is_default_hsn_code = fields.Boolean(required=False)
    

