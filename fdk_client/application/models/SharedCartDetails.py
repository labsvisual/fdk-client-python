"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class SharedCartDetails(BaseSchema):
    # Cart swagger.json

    
    user = fields.Dict(required=False)
    
    token = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    source = fields.Dict(required=False)
    

