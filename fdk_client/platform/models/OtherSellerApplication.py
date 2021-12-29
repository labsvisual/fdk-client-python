"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .OtherSellerCompany import OtherSellerCompany




class OtherSellerApplication(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    domain = fields.Str(required=False)
    
    company = fields.Nested(OtherSellerCompany, required=False)
    
    opt_type = fields.Str(required=False)
    

