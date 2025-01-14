"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CreditDetail(BaseSchema):
    # Payment swagger.json

    
    signup_url = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    
    is_registered = fields.Boolean(required=False)
    

