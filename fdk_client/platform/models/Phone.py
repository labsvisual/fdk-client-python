"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Phone(BaseSchema):
    # Billing swagger.json

    
    phone_number = fields.Str(required=False)
    
    phone_country_code = fields.Str(required=False)
    

