"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PaymentModeLogo import PaymentModeLogo




class IntentApp(BaseSchema):
    # Payment swagger.json

    
    code = fields.Str(required=False)
    
    package_name = fields.Str(required=False)
    
    logos = fields.Nested(PaymentModeLogo, required=False)
    
    display_name = fields.Str(required=False)
    

