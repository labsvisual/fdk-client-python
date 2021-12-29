"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ListingPriceFeature(BaseSchema):
    # Configuration swagger.json

    
    value = fields.Str(required=False)
    

