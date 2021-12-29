"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Details import Details


class MarketPlaceSttributes(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(Details, required=False), required=False)
    

