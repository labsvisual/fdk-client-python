"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GetShareCartLinkRequest(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    

