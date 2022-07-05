"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RedirectURL import RedirectURL




class RedirectToAggregatorResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(RedirectURL, required=False)
    
    success = fields.Boolean(required=False)
    

