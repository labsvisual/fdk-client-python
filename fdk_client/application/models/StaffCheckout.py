"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class StaffCheckout(BaseSchema):
    # Cart swagger.json

    
    user = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    

